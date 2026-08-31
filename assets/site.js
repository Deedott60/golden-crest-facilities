/* Shared site behaviour: year stamp + accessible mobile navigation. */
(function () {
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  var btn = document.getElementById('menuBtn');
  var links = document.getElementById('navlinks');
  if (!btn || !links) return;

  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    links.classList.toggle('open', !open);
    btn.setAttribute('aria-label', open ? 'Open navigation menu' : 'Close navigation menu');
  });
  links.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      links.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && links.classList.contains('open')) {
      links.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
      btn.focus();
    }
  });
})();
