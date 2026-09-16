/* ETS-BZH — interactions légères (vanilla, sans dépendance) */
(function () {
  "use strict";

  /* ------------------------------------------------------------------
   * Endpoint de réception des formulaires.
   * Laisser vide ("") => bascule automatique sur un envoi par e-mail
   * (ouverture du client mail du visiteur, pré-rempli).
   * Renseigner une URL (Formspree, API interne, Netlify Forms…) pour
   * un envoi direct en POST JSON.
   * ---------------------------------------------------------------- */
  var FORM_ENDPOINT = "";
  var EMAIL = "contact@etablissement-breizh.fr";

  /* ---------- Menu mobile ---------- */
  var burger = document.querySelector(".burger");
  var nav = document.getElementById("nav-principal");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---------- Formulaires de devis ---------- */
  var LABELS = {
    nom: "Nom", telephone: "Téléphone", email: "E-mail", ville: "Ville",
    departement: "Département", prestation: "Type d'intervention",
    urgence: "Urgence", message: "Message"
  };

  function champs(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) {
      if (k === "_gotcha" || k === "consentement") return;
      if (typeof v === "string" && v.trim() !== "") data[k] = v.trim();
    });
    return data;
  }

  function afficherMessage(form, type, texte) {
    var box = form.querySelector(".form-msg");
    if (!box) return;
    box.className = "form-msg form-msg--" + type;
    box.textContent = texte;
    box.setAttribute("role", "status");
    box.scrollIntoView({ block: "nearest" });
  }

  function envoyerParMail(form, data) {
    var corps = Object.keys(data).map(function (k) {
      return (LABELS[k] || k) + " : " + data[k];
    }).join("\n");
    var sujet = "Demande de devis ETS-BZH" + (data.departement ? " — " + data.departement : "");
    window.location.href = "mailto:" + EMAIL +
      "?subject=" + encodeURIComponent(sujet) +
      "&body=" + encodeURIComponent(corps + "\n\n— Envoyé depuis ets-bzh.fr");
    afficherMessage(form, "ok",
      "Votre messagerie s'ouvre avec la demande pré-remplie. Pour une urgence, appelez directement le 02 20 06 00 75.");
  }

  Array.prototype.forEach.call(document.querySelectorAll("form[data-devis]"), function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      // Anti-spam : champ piège masqué
      var piege = form.querySelector('input[name="_gotcha"]');
      if (piege && piege.value !== "") return;

      if (!form.checkValidity()) { form.reportValidity(); return; }

      var data = champs(form);
      data.page = document.title;

      var btn = form.querySelector('button[type="submit"]');
      var libelle = btn ? btn.textContent : "";

      if (!FORM_ENDPOINT) { envoyerParMail(form, data); return; }

      if (btn) { btn.disabled = true; btn.textContent = "Envoi en cours…"; }
      fetch(FORM_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        form.reset();
        afficherMessage(form, "ok",
          "Demande envoyée. Un technicien ETS-BZH vous rappelle sous 30 minutes ouvrées.");
      }).catch(function () {
        afficherMessage(form, "err",
          "L'envoi a échoué. Appelez-nous au 02 20 06 00 75 ou écrivez à " + EMAIL + ".");
      }).finally(function () {
        if (btn) { btn.disabled = false; btn.textContent = libelle; }
      });
    });
  });

  /* ---------- Barre d'action collante (ordinateur) ----------
     Elle n'apparaît qu'une fois le formulaire du haut passé : tant qu'il est
     visible, elle ferait doublon. */
  var barre = document.getElementById("barre-fixe");
  var hero = document.querySelector(".hero");
  var basDePage = document.querySelector(".confiance") || document.querySelector(".footer");
  if (barre && hero && "IntersectionObserver" in window) {
    var heroVisible = true, finVisible = false;
    function majBarre() { barre.hidden = heroVisible || finVisible; }

    new IntersectionObserver(function (e) {
      heroVisible = e[0].isIntersecting; majBarre();
    }, { rootMargin: "-120px 0px 0px 0px" }).observe(hero);

    // masquée au pied de page : les mêmes appels s'y trouvent déjà, et la
    // barre viendrait recouvrir le contenu de fin de page
    if (basDePage) {
      new IntersectionObserver(function (e) {
        finVisible = e[0].isIntersecting; majBarre();
      }, { rootMargin: "0px 0px -40px 0px" }).observe(basDePage);
    }
  }

  /* ---------- Emplacements photo ----------
     Si le fichier n'existe pas encore dans assets/img/photos/, on affiche le
     cadre d'attente à la place de l'image cassée. Deux mécanismes, car ce
     script est différé et certaines erreurs surviennent avant son exécution :
       1. on inspecte l'état des images déjà traitées ;
       2. on écoute les erreurs suivantes (l'événement « error » ne remontant
          pas, l'écoute se fait en phase de capture). */
  function marquerVide(img) {
    var fig = img.closest ? img.closest(".photo") : null;
    if (fig) fig.classList.add("photo--vide");
  }

  function verifierPhotos() {
    Array.prototype.forEach.call(document.querySelectorAll(".photo__img"), function (img) {
      if (img.complete) {
        if (img.naturalWidth === 0) marquerVide(img);
      } else {
        img.addEventListener("error", function () { marquerVide(img); });
      }
    });
  }

  document.addEventListener("error", function (e) {
    var img = e.target;
    if (!img || img.tagName !== "IMG") return;
    if ((" " + img.className + " ").indexOf(" photo__img ") === -1) return;
    marquerVide(img);
  }, true);

  verifierPhotos();
  window.addEventListener("load", verifierPhotos);

  /* ---------- Année automatique ---------- */
  Array.prototype.forEach.call(document.querySelectorAll("[data-annee]"), function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
