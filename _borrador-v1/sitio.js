// Filtros de fichas y botón "Copiar referencia".
(function () {
  var botones = document.querySelectorAll("[data-filtro]");
  var tarjetas = document.querySelectorAll("#lista-fichas [data-tipo]");
  botones.forEach(function (b) {
    b.addEventListener("click", function () {
      var f = b.getAttribute("data-filtro");
      botones.forEach(function (o) { o.setAttribute("aria-pressed", String(o === b)); });
      tarjetas.forEach(function (t) {
        t.hidden = !(f === "todas" || t.getAttribute("data-tipo") === f);
      });
    });
  });

  document.querySelectorAll("[data-copiar]").forEach(function (b) {
    var original = b.textContent;
    b.addEventListener("click", function () {
      var el = document.getElementById(b.getAttribute("data-copiar"));
      if (!el) return;
      var listo = function () {
        b.textContent = "Referencia copiada";
        setTimeout(function () { b.textContent = original; }, 2000);
      };
      var seleccionar = function () {
        var r = document.createRange();
        r.selectNodeContents(el);
        var s = window.getSelection();
        s.removeAllRanges();
        s.addRange(r);
        b.textContent = "Texto seleccionado: cópialo";
        setTimeout(function () { b.textContent = original; }, 2500);
      };
      try {
        navigator.clipboard.writeText(el.textContent.trim()).then(listo, seleccionar);
      } catch (e) {
        seleccionar();
      }
    });
  });
})();
