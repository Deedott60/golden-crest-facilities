#!/usr/bin/env python3
"""Tiny localhost-only shared progress API for the founders checklist."""

from __future__ import annotations

import json
import os
import re
import tempfile
import threading
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HOST = "127.0.0.1"
PORT = int(os.environ.get("CHECKLIST_SYNC_PORT", "3231"))
DATA = Path(os.environ.get("CHECKLIST_SYNC_DATA", "/var/lib/janitorial-checklist/progress.json"))
MAX_BODY = 16_384
KEY_RE = re.compile(r"^[a-z0-9-]+::[mk]$")
LOCK = threading.Lock()


def load_state() -> dict[str, bool]:
    try:
        raw = json.loads(DATA.read_text(encoding="utf-8"))
        state = raw.get("state", {}) if isinstance(raw, dict) else {}
        return {k: v for k, v in state.items() if KEY_RE.fullmatch(k) and isinstance(v, bool)}
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def save_state(state: dict[str, bool]) -> None:
    DATA.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "state": state,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    fd, tmp = tempfile.mkstemp(prefix="progress-", suffix=".json", dir=DATA.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, separators=(",", ":"), sort_keys=True)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, DATA)
        os.chmod(DATA, 0o600)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


class Handler(BaseHTTPRequestHandler):
    server_version = "ChecklistSync/1"

    def log_message(self, fmt: str, *args: object) -> None:
        return

    def send_json(self, status: int, payload: dict[str, object]) -> None:
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path != "/progress":
            self.send_json(404, {"error": "not_found"})
            return
        with LOCK:
            self.send_json(200, {"state": load_state()})

    def do_POST(self) -> None:
        if self.path != "/progress":
            self.send_json(404, {"error": "not_found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length < 1 or length > MAX_BODY:
            self.send_json(413, {"error": "invalid_size"})
            return
        try:
            payload = json.loads(self.rfile.read(length))
        except (json.JSONDecodeError, UnicodeDecodeError):
            self.send_json(400, {"error": "invalid_json"})
            return
        key = payload.get("key") if isinstance(payload, dict) else None
        done = payload.get("done") if isinstance(payload, dict) else None
        if not isinstance(key, str) or not KEY_RE.fullmatch(key) or not isinstance(done, bool):
            self.send_json(400, {"error": "invalid_mark"})
            return
        with LOCK:
            state = load_state()
            state[key] = done
            save_state(state)
            self.send_json(200, {"ok": True, "state": state})


if __name__ == "__main__":
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
