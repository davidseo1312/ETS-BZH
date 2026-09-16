# -*- coding: utf-8 -*-
"""
Générateur statique du site ETS-BZH.

    python3 tools/build.py

Produit à la racine du dépôt :
  · 12 landing pages (3 activités × 4 départements)
  · index.html, contact.html, mentions-legales.html, cgu.html, 404.html
  · sitemap.xml, robots.txt
"""
import hashlib
import json
import os
import re
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import (SITE, DEPARTEMENTS, ACTIVITES, REASSURANCE, ETAPES, STATS,  # noqa: E402
                  PHOTOS_ACCUEIL, PHOTO_EQUIPE, PHOTO_CONTACT, LOGOS)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEL = SITE["tel"]
TEL_LIEN = SITE["tel_lien"]
EMAIL = SITE["email"]
BASE = SITE["url"]
TODAY = date.today().isoformat()


def empreinte(chemin):
    """Empreinte courte d'un fichier statique, ajoutée à son URL.

    Sans cela, un navigateur peut continuer à servir l'ancienne feuille de style
    après une mise en ligne : le HTML est à jour, le CSS non, et la page casse.
    """
    with open(os.path.join(ROOT, chemin), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def taille_png(chemin):
    """Dimensions natives d'un PNG, lues dans son en-tête IHDR (sans dépendance).

    Elles servent d'attributs width/height : le navigateur connaît le rapport
    d'aspect avant le chargement et ne décale pas la mise en page.
    """
    with open(os.path.join(ROOT, chemin), "rb") as f:
        entete = f.read(24)
    return int.from_bytes(entete[16:20], "big"), int.from_bytes(entete[20:24], "big")


CSS = "assets/css/style.css?v=" + empreinte("assets/css/style.css")
JS = "assets/js/main.js?v=" + empreinte("assets/js/main.js")

# « des Côtes-d'Armor », « du Finistère », …
DE = {"22": "des Côtes-d'Armor", "29": "du Finistère",
      "35": "d'Ille-et-Vilaine", "56": "du Morbihan"}

ACT = {a["key"]: a for a in ACTIVITES}
DEPT = {d["num"]: d for d in DEPARTEMENTS}


# ---------------------------------------------------------------- utilitaires
def url_landing(act, dept):
    return "%s-%s-%s.html" % (act["slug"], dept["slug"], dept["num"])


def fmt(txt, act=None, dept=None):
    """Interpolation des jetons éditoriaux."""
    if dept:
        txt = (txt.replace("{art}", dept["article"])
                  .replace("{Art}", dept["article_maj"])
                  .replace("{dept}", dept["nom"])
                  .replace("{num}", dept["num"])
                  .replace("{du_dept}", DE[dept["num"]])
                  .replace("{prefecture}", dept["prefecture"])
                  .replace("{contexte}", dept["contexte"])
                  .replace("{axes}", dept["axes"])
                  .replace("{ville1}", dept["villes"][0])
                  .replace("{ville2}", dept["villes"][1])
                  .replace("{ville3}", dept["villes"][2]))
    if act:
        txt = (txt.replace("{pro_pluriel}", act["pro_pluriel"])
                  .replace("{pro}", act["pro"])
                  .replace("{activite}", act["nom_court"].lower()))
    return txt.replace("{tel}", TEL)


def clean(txt):
    """Version texte brut (pour les balises meta et le JSON-LD)."""
    return (txt.replace("&nbsp;", " ").replace("&amp;", "&")
               .replace("&lt;", "<").replace("&gt;", ">")
               .replace("&#39;", "'").replace("&quot;", '"'))


SVG = {
    "tel": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1l-2.3 2.2z"/></svg>',
    "mail": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M2 5h20v14H2z" opacity=".25"/><path d="M2 5h20v14H2V5zm2 2v.5l8 5 8-5V7H4zm16 10V9.9l-8 5-8-5V17h16z"/></svg>',
    "pin": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
    "form": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 3h16v18H4z" opacity=".2"/><path d="M5 2h14v20H5V2zm2 2v16h10V4H7zm2 3h6v2H9V7zm0 4h6v2H9v-2zm0 4h4v2H9v-2z"/></svg>',
}

ICONES = {
    "degorgement": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11zm0 3.6C10.4 7.8 8 11.3 8 13a4 4 0 0 0 8 0c0-1.7-2.4-5.2-4-7.4z"/></svg>',
    "plomberie": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 4h7v4H6v3h7v-3h-1V4h9v4h-3v3a2 2 0 0 1-2 2h-5v7H6v-7a2 2 0 0 1-2-2V8H3V4z"/></svg>',
    "electricite": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6l1-8z"/></svg>',
}


# ------------------------------------------------------------------ fragments
def head(titre, description, canonical, extra_json=None, mots_cles=""):
    jsonld = ""
    for bloc in (extra_json or []):
        jsonld += ('\n  <script type="application/ld+json">%s</script>'
                   % json.dumps(bloc, ensure_ascii=False, separators=(",", ":")))
    kw = ('\n  <meta name="keywords" content="%s">' % mots_cles) if mots_cles else ""
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titre}</title>
  <meta name="description" content="{description}">{kw}
  <link rel="canonical" href="{BASE}/{canonical}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
  <meta name="author" content="{SITE['nom']}">
  <meta name="theme-color" content="#005580">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE['nom']}">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:title" content="{titre}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{BASE}/{canonical}">
  <meta property="og:image" content="{BASE}/assets/img/logo.jpg">
  <meta property="og:image:width" content="680">
  <meta property="og:image:height" content="460">
  <meta property="og:image:alt" content="Logo ETS-BZH">
  <meta name="twitter:card" content="summary">
  <link rel="icon" href="assets/img/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="assets/img/logo-emblem.png">
  <link rel="preload" href="assets/fonts/barlow-400.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/barlow-condensed-700.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{CSS}">
  <link rel="preconnect" href="{BASE}">{jsonld}
</head>
<body>
<a class="sr-only" href="#contenu">Aller au contenu principal</a>"""


def topbar():
    return f"""
<div class="topbar">
  <div class="container topbar__inner">
    <ul class="topbar__list">
      <li><span class="dot dot--live"></span> Urgences 24h/24 &amp; 7j/7</li>
      <li>Devis gratuit sans engagement</li>
      <li>Garantie décennale</li>
    </ul>
    <ul class="topbar__list">
      <li>{SVG['pin']} Bretagne&nbsp;: 22 · 29 · 35 · 56</li>
      <li>{SVG['mail']} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
    </ul>
  </div>
</div>"""


def nav_zones():
    """Menu déroulant des 12 landing pages."""
    out = []
    for act in ACTIVITES:
        liens = "".join(
            '<a href="%s">%s (%s)</a>' % (url_landing(act, d), d["nom"], d["num"])
            for d in DEPARTEMENTS)
        out.append('<li class="has-sub"><a href="#">%s ▾</a>'
                   '<div class="sub"><strong>%s par département</strong>%s</div></li>'
                   % (act["nom_court"], act["nom_court"], liens))
    return "".join(out)


def header(courant=""):
    def cur(k):
        return ' aria-current="page"' if courant == k else ""
    return f"""
<header class="header">
  <div class="container header__inner">
    <a class="logo" href="index.html">
      <img class="logo__mark" src="assets/img/logo-emblem.png" width="52" height="52"
           alt="Logo ETS-BZH, plomberie, dégorgement, électricité et canalisations en Bretagne">
      <span class="logo__txt">
        <span class="logo__name">ETS-BZH</span>
        <span class="logo__tag">{SITE['baseline_courte']}</span>
      </span>
    </a>

    <nav class="nav" id="nav-principal" aria-label="Navigation principale">
      <ul style="display:contents">
        <li><a href="index.html"{cur('accueil')}>Accueil</a></li>
        {nav_zones()}
        <li><a href="contact.html"{cur('contact')}>Contact</a></li>
      </ul>
    </nav>

    <div class="header__cta">
      <button class="burger" type="button" aria-label="Ouvrir le menu"
              aria-expanded="false" aria-controls="nav-principal"><span></span></button>
      <a class="tel-btn" href="tel:{TEL_LIEN}" data-cta="header">
        {SVG['tel']}<span class="tel-btn__txt"><span class="tel-btn__long">Appeler le </span>{TEL}</span>
      </a>
    </div>
  </div>
</header>"""


def ariane(items):
    lis = ""
    for i, (label, href) in enumerate(items):
        if href and i < len(items) - 1:
            lis += '<li><a href="%s">%s</a></li>' % (href, label)
        else:
            lis += '<li aria-current="page">%s</li>' % label
    return ('\n<nav class="ariane" aria-label="Fil d\'Ariane"><div class="container">'
            '<ol>%s</ol></div></nav>' % lis)


def formulaire(idp, titre, soustitre, bouton, dept=None, act=None, court=False,
               message=False):
    """Formulaire de rappel / devis.

    court   : version compacte (bandeau CTA de fin de page)
    message : ajoute un champ libre (page contact)
    """
    opts_dept = "".join(
        '<option value="%s (%s)"%s>%s (%s)</option>'
        % (d["nom"], d["num"], " selected" if dept and d["num"] == dept["num"] else "",
           d["nom"], d["num"])
        for d in DEPARTEMENTS)
    opts_presta = "".join(
        '<option value="%s"%s>%s</option>'
        % (clean(a["nom"]), " selected" if act and a["key"] == act["key"] else "",
           clean(a["nom"]))
        for a in ACTIVITES)

    bloc_presta = "" if court else f"""
        <div class="field">
          <label for="{idp}-presta">Type d'intervention</label>
          <select id="{idp}-presta" name="prestation">{opts_presta}
            <option value="Autre / je ne sais pas">Autre / je ne sais pas</option>
          </select>
        </div>"""

    bloc_urgence = "" if court else f"""
        <div class="field">
          <label for="{idp}-urgence">Degré d'urgence</label>
          <select id="{idp}-urgence" name="urgence">
            <option>Urgence immédiate (intervention aujourd'hui)</option>
            <option>Sous 48 h</option>
            <option>Demande de devis, sans urgence</option>
          </select>
        </div>"""

    bloc_message = f"""
        <div class="field">
          <label for="{idp}-msg">Décrivez votre problème <span style="font-weight:600;text-transform:none;letter-spacing:0;color:var(--gris-clair)">(facultatif)</span></label>
          <textarea id="{idp}-msg" name="message"
                    placeholder="Ex. : WC bouché depuis ce matin, maison individuelle, accès par le garage."></textarea>
        </div>""" if message else ""


    return f"""
<div class="form-card">
  <div class="form-card__head">
    <h2>{titre}</h2>
    <p>{soustitre}</p>
  </div>
  <div class="form-card__body">
    <form data-devis id="{idp}" novalidate>
      <p class="form-msg" aria-live="polite"></p>
      <div class="field-row">
        <div class="field">
          <label for="{idp}-nom">Nom <span class="req">*</span></label>
          <input id="{idp}-nom" name="nom" type="text" autocomplete="name"
                 placeholder="Votre nom" required>
        </div>
        <div class="field">
          <label for="{idp}-tel">Téléphone <span class="req">*</span></label>
          <input id="{idp}-tel" name="telephone" type="tel" autocomplete="tel"
                 inputmode="tel" pattern="[0-9 +().-]{{9,}}" placeholder="06 00 00 00 00" required>
        </div>
      </div>
      <div class="field-row">
        <div class="field">
          <label for="{idp}-ville">Ville <span class="req">*</span></label>
          <input id="{idp}-ville" name="ville" type="text" autocomplete="address-level2"
                 placeholder="{dept['prefecture'] if dept else 'Votre commune'}" required>
        </div>
        <div class="field">
          <label for="{idp}-dept">Département</label>
          <select id="{idp}-dept" name="departement">{opts_dept}</select>
        </div>
      </div>{bloc_presta}{bloc_urgence}{bloc_message}
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"
             aria-hidden="true" style="position:absolute;left:-9999px;opacity:0">
      <label class="consent">
        <input type="checkbox" name="consentement" required>
        <span>J'accepte d'être recontacté par ETS-BZH au sujet de ma demande.
          Mes données ne sont utilisées que pour ce rappel
          (<a href="mentions-legales.html">mentions légales</a>).</span>
      </label>
      <button class="btn btn--primary btn--bloc" type="submit">{bouton}</button>
      <p class="form-note">Réponse sous 30 minutes ouvrées · Urgence&nbsp;? Appelez le
        <a href="tel:{TEL_LIEN}">{TEL}</a></p>
    </form>
  </div>
</div>"""


def bandeau_stats():
    cases = "".join(
        '<div class="stat"><div class="stat__num">%s</div><div class="stat__lbl">%s</div></div>'
        % (n, l) for n, l in STATS)
    return ('\n<section class="stats" aria-label="ETS-BZH en chiffres">'
            '<div class="stats__grid">%s</div></section>' % cases)


def bloc_etapes(titre="Comment ça se passe&nbsp;?", intro=""):
    steps = "".join(
        '<div class="step"><div class="step__n">Étape %d</div><h3>%s</h3><p>%s</p></div>'
        % (i + 1, t, d) for i, (t, d) in enumerate(ETAPES))
    return f"""
<section class="section section--fond">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Notre méthode</span>
      <h2>{titre}</h2>
      <p class="lead">{intro}</p>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>"""


def bloc_reassurance(dept=None):
    lieu = (" %s %s" % (dept["article"], dept["nom"])) if dept else " en Bretagne"
    cards = "".join(
        '<div class="card"><div class="card__num">%02d</div><h3>%s</h3><p>%s</p></div>'
        % (i + 1, t, d) for i, (t, d) in enumerate(REASSURANCE))
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Pourquoi ETS-BZH</span>
      <h2>Pourquoi choisir ETS-BZH{lieu}&nbsp;?</h2>
      <p class="lead">Une entreprise bretonne, des techniciens salariés qui connaissent le
        terrain, et des engagements écrits sur chaque intervention.</p>
    </div>
    <div class="grid grid--4">{cards}</div>
  </div>
</section>"""


def cta_final(titre, texte, idp, dept=None, act=None):
    return f"""
<section class="cta" id="devis">
  <div class="container cta__grid">
    <div>
      <h2>{titre}</h2>
      <p>{texte}</p>
      <a class="cta__tel" href="tel:{TEL_LIEN}" data-cta="cta-final">
        {SVG['tel']} {TEL}
      </a>
      <p class="cta__dispo">Ligne directe · 24h/24 et 7j/7 · Devis gratuit sans engagement</p>
    </div>
    {formulaire(idp, "Être rappelé rapidement", "Réponse sous 30 minutes ouvrées",
                "Obtenir un Devis Gratuit", dept=dept, act=act, court=True)}
  </div>
</section>"""


def bandeau_avis(legende):
    """Bandeau de note moyenne, estampillé Google Reviews."""
    contenu = f"""
    <img class="avis-note__logo" src="assets/img/logo-google-reviews.png"
         alt="Google Reviews" width="300" height="121" loading="lazy">
    <span class="avis-note__sep" aria-hidden="true"></span>
    <span class="avis-note__bloc">
      <span class="avis-note__chiffre"><strong>4,8</strong>/5</span>
      <span class="avis-note__etoiles" aria-hidden="true">★★★★★</span>
    </span>
    <span class="avis-note__txt">{legende}<br>sur les 12 derniers mois</span>"""
    if SITE.get("google_avis"):
        return ('<a class="note-globale" href="%s" target="_blank" rel="noopener">%s</a>'
                % (SITE["google_avis"], contenu))
    return '<div class="note-globale">%s</div>' % contenu


def bandeau_confiance():
    """Bandeau de logos affiché sur toutes les pages, juste avant le pied de page.
    Fond clair obligatoire : les logos comportent du texte noir."""
    logos = "".join(
        '<img class="confiance__logo" src="assets/img/%s" alt="%s" '
        'style="--h:%dpx;--dy:%s" width="%d" height="%d" loading="lazy">'
        % ((f, alt, h, dy) + taille_png("assets/img/" + f))
        for f, alt, h, dy in LOGOS)
    return f"""
<section class="confiance" aria-label="Qualifications et assurance">
  <div class="container confiance__logos">{logos}</div>
</section>
"""


def footer():
    def colonne(act):
        return "".join('<li><a href="%s">%s %s (%s)</a></li>'
                       % (url_landing(act, d), act["nom_court"], d["nom"], d["num"])
                       for d in DEPARTEMENTS)

    return bandeau_confiance() + f"""
<footer class="footer">
  <div class="container">
    <div class="footer__marque">
      <p class="footer__nom">ETS-BZH</p>
      <p class="footer__accroche">Dépannage et travaux en plomberie, dégorgement de
        canalisations et électricité sur les Côtes-d'Armor, le Finistère,
        l'Ille-et-Vilaine et le Morbihan.</p>
      <a class="footer__tel" href="tel:{TEL_LIEN}">{SVG['tel']} {TEL}</a>
      <ul class="footer__contacts">
        <li>{SVG['mail']} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{SVG['pin']} Intervention 24h/24 et 7j/7 en Bretagne</li>
      </ul>
    </div>

    <div class="footer__grid">
      <div>
        <h3>{ACT['degorgement']['nom_court']}</h3>
        <ul>{colonne(ACT['degorgement'])}</ul>
      </div>

      <div>
        <h3>{ACT['plomberie']['nom_court']}</h3>
        <ul>{colonne(ACT['plomberie'])}</ul>
      </div>

      <div>
        <h3>{ACT['electricite']['nom_court']}</h3>
        <ul>{colonne(ACT['electricite'])}</ul>
      </div>

      <div>
        <h3>Zones d'intervention</h3>
        <ul>
          <li>Côtes-d'Armor (22) — Saint-Brieuc, Lannion, Dinan</li>
          <li>Finistère (29) — Brest, Quimper, Morlaix</li>
          <li>Ille-et-Vilaine (35) — Rennes, Saint-Malo, Fougères</li>
          <li>Morbihan (56) — Vannes, Lorient, Pontivy</li>
        </ul>
      </div>
    </div>

    <div class="footer__bas">
      <span>© <span data-annee>2026</span> ETS-BZH — Tous droits réservés.</span>
      <nav class="footer__legal" aria-label="Liens légaux">
        <a href="index.html">Accueil</a>
        <a href="contact.html">Contact</a>
        <a href="mentions-legales.html">Mentions légales</a>
        <a href="cgu.html">CGU</a>
      </nav>
    </div>
  </div>
</footer>

<div class="mobile-bar">
  <a class="mobile-bar__tel" href="tel:{TEL_LIEN}" data-cta="mobile">{SVG['tel']} Appeler</a>
  <a class="mobile-bar__devis" href="#devis">{SVG['form']} Devis gratuit</a>
</div>

<script src="{JS}" defer></script>
</body>
</html>"""


# ---------------------------------------------------------------- photos
# Chaque emplacement pointe vers assets/img/photos/<fichier>.
# Tant que le fichier n'existe pas, un cadre d'attente s'affiche à sa place
# (voir assets/js/main.js). Déposez la photo sous ce nom exact : elle apparaît.

SVG_APPAREIL = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" '
                'width="30" height="30"><path d="M9 3h6l1.5 2H21v14H3V5h4.5L9 3zm3 5a5 5 0 1 0 '
                '0 10 5 5 0 0 0 0-10zm0 2a3 3 0 1 1 0 6 3 3 0 0 1 0-6z"/></svg>')


def photo(fichier, alt, legende="", large=False):
    """Emplacement photo remplaçable. `large` = format 3/2 au lieu de 4/3."""
    cap = ('<figcaption class="photo__legende">%s</figcaption>' % legende) if legende else ""
    ratio = "3 / 2" if large else "4 / 3"
    return f"""
<figure class="photo">
  <div class="photo__cadre" style="aspect-ratio:{ratio}">
    <img class="photo__img" src="assets/img/photos/{fichier}" alt="{alt}"
         loading="lazy" decoding="async">
    <div class="photo__attente">
      {SVG_APPAREIL}
      <span class="photo__aide">Emplacement photo</span>
      <code class="photo__nom">photos/{fichier}</code>
    </div>
  </div>
  {cap}
</figure>"""


def galerie(photos, eyebrow, titre, intro, colonnes=None):
    """Galerie photo. Sans `colonnes`, la grille s'adapte : 3 colonnes si le
    nombre de photos est un multiple de 3, 4 sinon — jamais de ligne bancale."""
    if colonnes is None:
        colonnes = 3 if len(photos) % 3 == 0 else 4
    items = "".join(photo(f, a, l) for f, a, l in photos)
    return f"""
<section class="section section--pale">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{titre}</h2>
      <p class="lead">{intro}</p>
    </div>
    <div class="grid grid--{colonnes}">{items}</div>
  </div>
</section>"""


# ------------------------------------------------------------------- JSON-LD
def ld_business(act=None, dept=None):
    zones = [{"@type": "AdministrativeArea", "name": "%s (%s)" % (d["nom"], d["num"])}
             for d in DEPARTEMENTS]
    if dept:
        zones = [{"@type": "AdministrativeArea", "name": "%s (%s)" % (dept["nom"], dept["num"])}]
    nom = SITE["nom"]
    if act and dept:
        nom = "%s — %s %s" % (SITE["nom"], clean(act["nom_court"]), dept["nom"])
    data = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "Plumber" if (act and act["key"] != "electricite")
                  else "Electrician" if act else "HomeAndConstructionBusiness"],
        "name": nom,
        "description": clean(act["accroche"]) if act else
                       "Plomberie, dégorgement de canalisations et électricité en Bretagne.",
        "telephone": TEL_LIEN,
        "email": EMAIL,
        "url": BASE + "/" + (url_landing(act, dept) if (act and dept) else "index.html"),
        "image": BASE + "/assets/img/logo.jpg",
        "priceRange": "€€",
        "address": {"@type": "PostalAddress", "addressRegion": "Bretagne",
                    "addressCountry": "FR"},
        "areaServed": zones,
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                          "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59"}],
    }
    if act:
        data["makesOffer"] = [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": clean(t),
                                               "description": clean(d)}}
            for t, d in act["prestations"]]
    return data


def ld_faq(act, dept):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": clean(fmt(q, act, dept)),
             "acceptedAnswer": {"@type": "Answer", "text": clean(fmt(r, act, dept))}}
            for q, r in act["faq"]],
    }


def ld_ariane(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": clean(label),
             "item": BASE + "/" + (href or "")}
            for i, (label, href) in enumerate(items)],
    }


import re as _re

# « & » isolé -> « &amp; » (HTML valide), sans toucher aux entités existantes.
_AMP = _re.compile(r"&(?!(?:#[0-9]+|#x[0-9a-fA-F]+|[a-zA-Z][a-zA-Z0-9]*);)")
_SCRIPT = _re.compile(r"(<script\b.*?</script>)", _re.S)


def echapper_amp(html):
    """Échappe les & en dehors des blocs <script> (contenu brut, non parsé)."""
    return "".join(
        part if part.lower().startswith("<script") else _AMP.sub("&amp;", part)
        for part in _SCRIPT.split(html))


def ecrire(nom, contenu):
    if nom.endswith(".html"):
        contenu = echapper_amp(contenu)
    with open(os.path.join(ROOT, nom), "w", encoding="utf-8") as f:
        f.write(contenu.strip() + "\n")
    print("  ✓ %-46s %6d o" % (nom, len(contenu)))


# ============================================================ LANDING PAGES
def page_landing(act, dept):
    url = url_landing(act, dept)
    d_nom, d_num = dept["nom"], dept["num"]
    art = dept["article"]
    du = DE[d_num]
    activite = clean(act["nom_court"]).lower()

    h1 = "%s %s %s (%s)" % (act["h1"], art, d_nom, d_num)
    titre = "%s %s (%s) — Urgence 24/7 | ETS-BZH" % (act["nom_court"], d_nom, d_num)
    desc = clean("%s %s %s (%s) : intervention d'urgence 7j/7, devis gratuit, artisans "
                 "qualifiés et garantie décennale. Appelez le %s."
                 % (act["metier"], art, d_nom, d_num, TEL))[:300]
    mots = clean("%s %s, %s %s, %s %s, dépannage urgence %s"
                 % (act["nom_court"], d_nom, act["pro"], d_nom, act["nom_court"], d_num,
                    dept["prefecture"])) + ", " + clean(act["mots_cles"])

    fil = [("Accueil", "index.html"),
           ("%s %s" % (act["nom_court"], d_nom), url)]

    # --- Prestations -------------------------------------------------------
    prestas = "".join(
        '<article class="presta"><div class="presta__ico">%02d</div>'
        '<div><h3>%s</h3><p>%s</p></div></article>' % (i + 1, t, d)
        for i, (t, d) in enumerate(act["prestations"]))

    # --- Urgences ----------------------------------------------------------
    urgences = "".join('<li><span class="tick">!</span><span>%s</span></li>' % u
                       for u in act["urgences"])

    # --- Tarifs ------------------------------------------------------------
    lignes = "".join('<tr><td>%s</td><td>%s</td></tr>' % (t, p) for t, p in act["tarifs"])

    # --- Avis --------------------------------------------------------------
    villes_avis = [dept["villes"][0], dept["villes"][1], dept["villes"][3]]
    avis = ""
    for (txt, nom, note), ville in zip(act["avis"], villes_avis):
        avis += ('<article class="avis"><div class="avis__stars" aria-label="%d étoiles sur 5">'
                 '%s</div><p class="avis__txt">« %s »</p><div class="avis__auteur">'
                 '<span class="avis__ini" aria-hidden="true">%s</span><span>'
                 '<span class="avis__nom">%s</span><br><span class="avis__ville">%s (%s)</span>'
                 '</span></div></article>'
                 % (note, "★" * note, txt, nom[0], nom, ville, d_num))

    # --- Villes ------------------------------------------------------------
    villes = "".join('<li><span class="tick">▪</span><span>%s %s</span></li>'
                     % (act["nom_court"], v) for v in dept["villes"])

    # --- FAQ ---------------------------------------------------------------
    faq = "".join(
        '<details%s><summary>%s</summary><div class="faq__body">%s</div></details>'
        % (" open" if i == 0 else "", fmt(q, act, dept), fmt(r, act, dept))
        for i, (q, r) in enumerate(act["faq"]))

    # --- Contenu SEO -------------------------------------------------------
    prose = "".join("<p>%s</p>" % fmt(p, act, dept) for p in act["prose"])
    for h3, items in act["prose_h3"]:
        prose += "<h3>%s</h3><ul>%s</ul>" % (
            fmt(h3, act, dept), "".join("<li>%s</li>" % i for i in items))

    # --- Maillage interne --------------------------------------------------
    autres_act = "".join(
        '<a href="%s">%s %s (%s)</a>' % (url_landing(a, dept), a["nom_court"], d_nom, d_num)
        for a in ACTIVITES if a["key"] != act["key"])
    autres_dept = "".join(
        '<a href="%s">%s %s (%s)</a>' % (url_landing(act, d), act["nom_court"], d["nom"], d["num"])
        for d in DEPARTEMENTS if d["num"] != d_num)

    hero_points = "".join('<li><span class="tick">✓</span><span>%s</span></li>' % p
                          for p in act["hero_points"])

    return (
        head(titre, desc, url,
             [ld_business(act, dept), ld_faq(act, dept), ld_ariane(fil)], mots)
        + topbar() + header() + ariane(fil) + f"""

<main id="contenu">

<!-- ============================ HERO ============================ -->
<section class="hero">
  <div class="container hero__grid">
    <div>
      <span class="hero__badge"><span class="dot dot--live"></span> Urgence {d_nom} · 24h/24</span>
      <h1>{h1}</h1>
      <p class="hero__sub">Interventions rapides 7j/7 — techniciens qualifiés à votre service
        {art} {d_nom}. {act['accroche']}</p>
      <ul class="hero__points">{hero_points}</ul>
      <div class="hero__actions">
        <a class="btn btn--blanc btn--xl" href="tel:{TEL_LIEN}" data-cta="hero">
          {SVG['tel']} Appeler le {TEL}
        </a>
        <a class="btn btn--outline-blanc btn--xl" href="#devis">Devis gratuit</a>
      </div>
      <p class="hero__villes"><strong>Nous intervenons&nbsp;:</strong>
        {", ".join(dept["villes"][:8])} et toutes les communes {du}.</p>
    </div>
    {formulaire("hero-" + act["key"] + "-" + d_num,
                "Rappel immédiat &amp; devis gratuit",
                "Un technicien %s vous rappelle sous 30 minutes ouvrées." % du,
                "Obtenir un Devis Gratuit", dept=dept, act=act)}
  </div>
</section>
{bandeau_stats()}

<!-- ======================== PRESTATIONS ========================= -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Nos prestations {art} {d_nom}</span>
      <h2>{act['metier']} {art} {d_nom}&nbsp;: tout ce que nous traitons</h2>
      <p class="lead">Du dépannage d'urgence au chantier planifié, nos {act['pro_pluriel']}
        interviennent sur l'ensemble {du}, particuliers comme professionnels.</p>
    </div>
    <div class="grid grid--2">{prestas}</div>
  </div>
</section>

<!-- ========================== URGENCES ========================== -->
<section class="section section--pale">
  <div class="container grid grid--2" style="align-items:center">
    <div>
      <span class="eyebrow">Situations d'urgence</span>
      <h2>Une urgence {activite} {art} {d_nom}&nbsp;?</h2>
      <p class="lead">Ces situations ne peuvent pas attendre. Appelez-nous immédiatement&nbsp;:
        un technicien vous répond, qualifie le problème et se met en route.</p>
      <ul class="checks">{urgences}</ul>
      <p style="margin-top:26px">
        <a class="btn btn--urgence btn--xl" href="tel:{TEL_LIEN}" data-cta="urgence">
          {SVG['tel']} Urgence&nbsp;: {TEL}
        </a>
      </p>
    </div>
    <div>
    {photo(act["photo_equipe"][0], act["photo_equipe"][1], large=True) + '<div style="height:22px"></div>' if act["photo_equipe"] else ""}
    <div class="encadre">
      <h3>Zone d'intervention {du}</h3>
      <p>Nos équipes sont basées en Bretagne et circulent quotidiennement sur
         {dept['axes']}. Cela nous permet d'annoncer un délai réaliste dès votre appel —
         et de le tenir.</p>
      <h3 style="margin-top:22px">Ce que vous savez avant notre arrivée</h3>
      <ul class="checks" style="margin-top:12px">
        <li><span class="tick">✓</span><span>Le créneau d'intervention et le nom du technicien</span></li>
        <li><span class="tick">✓</span><span>Le coût du déplacement et du diagnostic</span></li>
        <li><span class="tick">✓</span><span>Une fourchette de prix pour la réparation</span></li>
      </ul>
    </div>
    </div>
  </div>
</section>

{bloc_reassurance(dept)}

<!-- =========================== TARIFS ========================== -->
<section class="section section--pale">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Transparence des tarifs</span>
      <h2>Nos tarifs indicatifs {art} {d_nom}</h2>
      <p class="lead">Aucun prix caché. Ces montants sont des points de départ&nbsp;: le tarif
        exact est fixé après diagnostic et validé par vous avant toute intervention.</p>
    </div>
    <div class="table-scroll">
    <table class="tarifs">
      <caption>Tarifs TTC indicatifs {TODAY[:4]}, hors pièces spécifiques et hors majorations
        éventuelles. Le devis gratuit fait foi.</caption>
      <thead><tr><th scope="col">Intervention</th><th scope="col">Tarif indicatif</th></tr></thead>
      <tbody>{lignes}</tbody>
    </table>
    </div>
  </div>
</section>

{bloc_etapes("De votre appel à la remise en service",
             "Quatre étapes, sans zone d'ombre&nbsp;: vous gardez la main à chaque instant.")}

<!-- ============================ AVIS ============================ -->
<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Avis clients</span>
      <h2>Ils nous ont appelés {art} {d_nom}</h2>
      <p class="lead">La proximité se mesure sur le terrain. Voici ce que disent nos clients
        {du} après une intervention.</p>
    </div>
    <div class="grid grid--3">{avis}</div>
    <div class="center">
      {bandeau_avis("Note moyenne des interventions ETS-BZH en Bretagne")}
    </div>
  </div>
</section>

{galerie(act["photos"],
         "En images",
         "Nos interventions %s %s en images" % (activite, d_nom),
         "Quelques chantiers réalisés par nos équipes. Photos de nos propres "
         "interventions — pas de banque d'images.")}

<!-- =========================== VILLES =========================== -->
<section class="section section--fond">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Proximité</span>
      <h2>{act['nom_court']} {art} {d_nom}&nbsp;: les communes desservies</h2>
      <p class="lead">Nous couvrons l'ensemble du département {d_num}, des grandes villes
        aux communes rurales. Votre commune n'est pas listée&nbsp;? Appelez-nous, nous
        intervenons très probablement chez vous.</p>
    </div>
    <ul class="checks villes-grid">{villes}</ul>
  </div>
</section>

<!-- ============================ FAQ ============================= -->
<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>{act['nom_court']} {art} {d_nom}&nbsp;: vos questions</h2>
    </div>
    <div class="faq">{faq}</div>
  </div>
</section>

<!-- ========================= CONTENU SEO ======================== -->
<section class="section section--fond">
  <div class="container">
    <div class="prose">
      <h2>{fmt(act['prose_titre'], act, dept)}</h2>
      {prose}
    </div>
  </div>
</section>

{cta_final("Une urgence %s %s&nbsp;? Nos techniciens interviennent dans l'heure."
           % (art, d_nom),
           "Appelez ETS-BZH maintenant&nbsp;: un professionnel qualifié vous répond, "
           "annonce un délai clair et se déplace avec le matériel adapté. "
           "Devis gratuit, tarif validé avant intervention, garantie décennale.",
           "cta-" + act["key"] + "-" + d_num, dept=dept, act=act)}

<!-- ========================= MAILLAGE =========================== -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Nos autres interventions</span>
      <h2>ETS-BZH, c'est aussi…</h2>
    </div>
    <div class="grid grid--2">
      <div class="card">
        <h3>Nos autres métiers {art} {d_nom}</h3>
        <div class="liens-grid" style="grid-template-columns:1fr;margin-top:12px">{autres_act}</div>
      </div>
      <div class="card">
        <h3>{act['nom_court']} dans les autres départements bretons</h3>
        <div class="liens-grid" style="grid-template-columns:1fr;margin-top:12px">{autres_dept}</div>
      </div>
    </div>
  </div>
</section>

</main>
""" + footer())


# ============================================================== ACCUEIL
def page_index():
    titre = "ETS-BZH — Plomberie, Dégorgement & Électricité en Bretagne (22, 29, 35, 56)"
    desc = ("Dépannage d'urgence 24/7 en plomberie, dégorgement de canalisations et "
            "électricité sur les Côtes-d'Armor, le Finistère, l'Ille-et-Vilaine et le "
            "Morbihan. Devis gratuit — %s." % TEL)
    fil = [("Accueil", "index.html")]

    # Cartes services
    svc = ""
    for act in ACTIVITES:
        liens = "".join(
            '<li><a href="%s">%s (%s)</a></li>' % (url_landing(act, d), d["nom"], d["num"])
            for d in DEPARTEMENTS)
        items = "".join('<li>%s</li>' % t for t, _ in act["prestations"][:5])
        svc += f"""
      <article class="card svc">
        <div class="icon-box">{ICONES[act['key']]}</div>
        <h3>{act['nom']}</h3>
        <p>{act['accroche']}</p>
        <ul class="svc__list">{items}</ul>
        <div class="svc__foot">
          <p style="font-size:.8rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--gris-clair);margin-bottom:8px">Choisir votre département</p>
          <div class="liens-grid" style="grid-template-columns:1fr 1fr;gap:6px 16px">
            {"".join('<a href="%s">%s (%s)</a>' % (url_landing(act, d), d["nom"], d["num"]) for d in DEPARTEMENTS)}
          </div>
        </div>
      </article>"""

    # Départements
    depts = ""
    for d in DEPARTEMENTS:
        liens = "".join('<a href="%s">%s</a>' % (url_landing(a, d), a["nom_court"])
                        for a in ACTIVITES)
        depts += f"""
      <article class="dept">
        <div class="dept__num">{d['num']}</div>
        <div class="dept__nom">{d['nom']}</div>
        <p class="dept__villes">{", ".join(d['villes'][:5])}…</p>
        <div class="dept__links">{liens}</div>
      </article>"""

    # Avis (un par activité)
    avis = ""
    paires = [(ACTIVITES[0], DEPARTEMENTS[0]), (ACTIVITES[1], DEPARTEMENTS[2]),
              (ACTIVITES[2], DEPARTEMENTS[3])]
    for act, dep in paires:
        txt, nom, note = act["avis"][0]
        avis += ('<article class="avis"><div class="avis__stars" aria-label="%d étoiles sur 5">'
                 '%s</div><p class="avis__txt">« %s »</p><div class="avis__auteur">'
                 '<span class="avis__ini" aria-hidden="true">%s</span><span>'
                 '<span class="avis__nom">%s</span><br><span class="avis__ville">%s (%s) — %s'
                 '</span></span></div></article>'
                 % (note, "★" * note, txt, nom[0], nom, dep["villes"][0], dep["num"],
                    act["nom_court"]))

    # Maillage complet 12 pages
    table = ""
    for d in DEPARTEMENTS:
        cellules = "".join('<td><a href="%s">%s %s</a></td>'
                           % (url_landing(a, d), a["nom_court"], d["num"]) for a in ACTIVITES)
        table += '<tr><th scope="row">%s (%s)</th>%s</tr>' % (d["nom"], d["num"], cellules)

    return (
        head(titre, desc, "index.html", [ld_business(), ld_ariane(fil)],
             "plombier Bretagne, dégorgement Bretagne, électricien Bretagne, dépannage "
             "urgence 22 29 35 56, ETS-BZH")
        + topbar() + header("accueil") + f"""

<main id="contenu">

<section class="hero">
  <div class="container hero__grid">
    <div>
      <span class="hero__badge"><span class="dot dot--live"></span> Astreinte urgence 24h/24 — 7j/7</span>
      <h1>Plomberie, Dégorgement &amp; Électricité en Bretagne&nbsp;: dépannage d'urgence 7j/7</h1>
      <p class="hero__sub">ETS-BZH intervient sur les Côtes-d'Armor&nbsp;(22), le
        Finistère&nbsp;(29), l'Ille-et-Vilaine&nbsp;(35) et le Morbihan&nbsp;(56).
        Des artisans qualifiés, un tarif annoncé avant intervention, une garantie décennale.</p>
      <ul class="hero__points">
        <li><span class="tick">✓</span><span>Un technicien au téléphone, pas un répondeur&nbsp;: délai annoncé dès l'appel</span></li>
        <li><span class="tick">✓</span><span>Devis gratuit sans engagement, validé avant tout démarrage</span></li>
        <li><span class="tick">✓</span><span>Véhicules équipés&nbsp;: réparation dès le premier passage dans la majorité des cas</span></li>
      </ul>
      <div class="hero__actions">
        <a class="btn btn--blanc btn--xl" href="tel:{TEL_LIEN}" data-cta="hero">
          {SVG['tel']} Appeler le {TEL}
        </a>
        <a class="btn btn--outline-blanc btn--xl" href="#zones">Choisir mon département</a>
      </div>
      <p class="hero__villes"><strong>Bases d'intervention&nbsp;:</strong>
        Saint-Brieuc, Brest, Quimper, Rennes, Saint-Malo, Vannes, Lorient et toute la Bretagne.</p>
    </div>
    {formulaire("hero-accueil", "Devis gratuit en 2 minutes",
                "Décrivez votre besoin, nous vous rappelons.",
                "Obtenir un Devis Gratuit")}
  </div>
</section>
{bandeau_stats()}

<section class="section" id="services">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Nos trois métiers</span>
      <h2>Une seule entreprise pour vos urgences du bâtiment</h2>
      <p class="lead">Dégorgement, plomberie, électricité&nbsp;: des équipes spécialisées,
        le même niveau d'exigence et un interlocuteur unique en Bretagne.</p>
    </div>
    <div class="grid grid--3">{svc}</div>
  </div>
</section>

<section class="section section--pale" id="zones">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Zones d'intervention</span>
      <h2>Sélectionnez votre département</h2>
      <p class="lead">Chaque département dispose de sa page dédiée&nbsp;: prestations, tarifs
        indicatifs, délais et équipes locales.</p>
    </div>
    <div class="dept-grid">{depts}</div>
  </div>
</section>

{bloc_reassurance()}
{bloc_etapes("De votre appel à la remise en service",
             "Une méthode identique sur les quatre départements bretons.")}

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Avis clients</span>
      <h2>Ce que disent nos clients en Bretagne</h2>
    </div>
    <div class="grid grid--3">{avis}</div>
    <div class="center">
      {bandeau_avis("Note moyenne des interventions ETS-BZH")}
    </div>
  </div>
</section>

{galerie(PHOTOS_ACCUEIL,
         "Nos réalisations",
         "ETS-BZH en images",
         "Chantiers, matériel et équipes&nbsp;: découvrez notre travail sur le terrain "
         "dans les quatre départements bretons.", 3)}

{cta_final("Une urgence en Bretagne&nbsp;? Nos techniciens interviennent dans l'heure.",
           "Fuite d'eau, canalisation bouchée, panne électrique&nbsp;: un professionnel "
           "qualifié vous répond immédiatement et se déplace avec le matériel adapté. "
           "Devis gratuit, tarif validé avant intervention.",
           "cta-accueil")}

<section class="section">
  <div class="container">
    <div class="prose" style="max-width:100%">
      <span class="eyebrow">À propos</span>
      <h2>ETS-BZH, l'entreprise de dépannage de proximité en Bretagne</h2>
      <div class="grid grid--2" style="align-items:start">
        <div>
          <p>ETS-BZH est une entreprise bretonne spécialisée dans trois métiers d'urgence du
            bâtiment&nbsp;: le <strong>dégorgement de canalisations</strong>, la
            <strong>plomberie</strong> et l'<strong>électricité</strong>. Nos équipes
            interviennent chez les particuliers, les syndics de copropriété, les bailleurs, les
            commerces et les collectivités sur l'ensemble de la région.</p>
          <p>Notre organisation repose sur un principe simple&nbsp;: rester proche du terrain.
            Des techniciens basés en Bretagne, des véhicules équipés du matériel professionnel
            (camion hydrocureur, caméra d'inspection, détection de fuite non destructive,
            appareillage électrique), et une astreinte réelle les nuits et week-ends.</p>
          <p>La transparence fait partie du service&nbsp;: nous annonçons un ordre de prix au
            téléphone, nous établissons un devis gratuit sur place, et nous ne démarrons rien
            sans votre accord. La facture correspond au devis accepté.</p>
        </div>
        <div>
          {photo(PHOTO_EQUIPE[0], PHOTO_EQUIPE[1], "Nos équipes en Bretagne", large=True)}
          <h3 style="margin-top:28px">Nos engagements</h3>
          <ul class="checks">
            <li><span class="tick">✓</span><span><strong>Intervention 24/7</strong> — astreinte nuits, week-ends et jours fériés</span></li>
            <li><span class="tick">✓</span><span><strong>Devis gratuit</strong> — sans engagement, validé avant travaux</span></li>
            <li><span class="tick">✓</span><span><strong>Artisans qualifiés</strong> — formés, équipés et assurés</span></li>
            <li><span class="tick">✓</span><span><strong>Garantie décennale</strong> — sur les travaux qui l'exigent</span></li>
            <li><span class="tick">✓</span><span><strong>Chantier propre</strong> — protection et nettoyage systématiques</span></li>
            <li><span class="tick">✓</span><span><strong>Particuliers &amp; pros</strong> — contrats d'entretien possibles</span></li>
          </ul>
        </div>
      </div>

      <h2 style="margin-top:2em">Nos 12 pages d'intervention en Bretagne</h2>
      <div class="table-scroll">
      <table class="tarifs">
        <thead><tr><th scope="col">Département</th>
          <th scope="col">Dégorgement</th><th scope="col">Plomberie</th>
          <th scope="col">Électricité</th></tr></thead>
        <tbody>{table}</tbody>
      </table>
      </div>
    </div>
  </div>
</section>

</main>
""" + footer())


# ============================================================== CONTACT
def page_contact():
    titre = "Contact & Devis Gratuit — ETS-BZH | Plomberie, Dégorgement, Électricité"
    desc = ("Contactez ETS-BZH pour un devis gratuit ou une intervention d'urgence en "
            "Bretagne (22, 29, 35, 56). Téléphone %s — %s." % (TEL, EMAIL))
    fil = [("Accueil", "index.html"), ("Contact", "contact.html")]

    zones = "".join(
        '<li><span class="tick">▪</span><span><strong>%s (%s)</strong> — %s…</span></li>'
        % (d["nom"], d["num"], ", ".join(d["villes"][:6])) for d in DEPARTEMENTS)

    return (
        head(titre, desc, "contact.html", [ld_business(), ld_ariane(fil)],
             "contact ETS-BZH, devis gratuit plomberie Bretagne, urgence dépannage 22 29 35 56")
        + topbar() + header("contact") + ariane(fil) + f"""

<main id="contenu">

<section class="hero" style="padding:52px 0 60px">
  <div class="container hero__grid">
    <div>
      <span class="hero__badge"><span class="dot dot--live"></span> Réponse sous 30 minutes ouvrées</span>
      <h1>Contact &amp; devis express</h1>
      <p class="hero__sub">Une urgence&nbsp;? Appelez directement&nbsp;: c'est toujours le plus
        rapide. Pour un devis ou une demande planifiée, le formulaire suffit — nous vous
        rappelons avec un créneau et un ordre de prix.</p>
      <p>
        <a class="cta__tel" href="tel:{TEL_LIEN}" data-cta="contact">{SVG['tel']} {TEL}</a>
      </p>
      <ul class="hero__points" style="margin-top:28px">
        <li><span class="tick">✉</span><span>{EMAIL}</span></li>
        <li><span class="tick">⏱</span><span>Astreinte urgence 24h/24 et 7j/7, jours fériés inclus</span></li>
        <li><span class="tick">▣</span><span>Interventions&nbsp;: Côtes-d'Armor (22), Finistère (29), Ille-et-Vilaine (35), Morbihan (56)</span></li>
      </ul>
    </div>
    {formulaire("contact-principal", "Formulaire de devis express",
                "Département, type de panne, degré d'urgence&nbsp;: tout en 1 minute.",
                "Obtenir un Devis Gratuit", message=True)}
  </div>
</section>
{bandeau_stats()}

<section class="section">
  <div class="container grid grid--2">
    <div>
      <span class="eyebrow">Nous joindre</span>
      <h2>Trois façons de nous contacter</h2>
      <div class="grid" style="gap:18px;margin-top:24px">
        <article class="presta">
          <div class="presta__ico">{SVG['tel']}</div>
          <div><h3>Par téléphone — le plus rapide</h3>
            <p><a href="tel:{TEL_LIEN}"><strong>{TEL}</strong></a> — un technicien vous répond
               directement, 24h/24. Privilégiez l'appel pour toute urgence&nbsp;: fuite active,
               refoulement, panne électrique.</p></div>
        </article>
        <article class="presta">
          <div class="presta__ico">{SVG['mail']}</div>
          <div><h3>Par e-mail</h3>
            <p><a href="mailto:{EMAIL}"><strong>{EMAIL}</strong></a> — idéal pour transmettre
               des photos, un plan ou un cahier des charges. Réponse sous 24 h ouvrées.</p></div>
        </article>
        <article class="presta">
          <div class="presta__ico">{SVG['form']}</div>
          <div><h3>Par formulaire</h3>
            <p>Remplissez le formulaire de devis ci-dessus&nbsp;: nous vous rappelons sous
               30 minutes ouvrées avec un créneau et une estimation.</p></div>
        </article>
      </div>
    </div>
    <div>
      <div class="encadre">
        <h3>Zones d'intervention</h3>
        <ul class="checks" style="margin-top:14px">{zones}</ul>
        <p style="margin-top:18px;font-size:.92rem">Votre commune n'apparaît pas&nbsp;?
          Appelez-nous&nbsp;: nous couvrons l'intégralité des quatre départements bretons,
          y compris les communes rurales.</p>
      </div>
      <div style="height:22px"></div>
      {photo(PHOTO_CONTACT[0], PHOTO_CONTACT[1], large=True)}
      <div class="encadre" style="margin-top:22px;background:var(--bleu-pale-2)">
        <h3>Professionnels, syndics et bailleurs</h3>
        <p>Nous proposons des contrats d'entretien et des interventions récurrentes&nbsp;:
          curage de colonnes, dégraissage de bacs à graisse, maintenance électrique,
          contrôle des installations. Demandez une proposition dédiée à
          <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      </div>
    </div>
  </div>
</section>

{bloc_etapes("Ce qui se passe après votre demande",
             "Pas d'attente inutile, pas de prix découvert à la fin.")}

{cta_final("Besoin d'une intervention aujourd'hui&nbsp;?",
           "Nos techniciens sont en astreinte 24h/24 sur les quatre départements bretons. "
           "Un appel suffit pour obtenir un délai ferme et un ordre de prix.",
           "cta-contact")}

</main>
""" + footer())


# ============================================================ PAGES LÉGALES
def page_mentions():
    titre = "Mentions légales — ETS-BZH"
    desc = ("Mentions légales du site ETS-BZH : éditeur, hébergeur, propriété "
            "intellectuelle et traitement des données personnelles (RGPD).")
    fil = [("Accueil", "index.html"), ("Mentions légales", "mentions-legales.html")]
    return (
        head(titre, desc, "mentions-legales.html", [ld_ariane(fil)])
        + topbar() + header() + ariane(fil) + f"""

<main id="contenu">

<section class="hero hero--compact">
  <div class="container">
    <span class="eyebrow">Informations légales</span>
    <h1>Mentions légales</h1>
    <p class="hero__sub">Éditeur, hébergeur, assurances, propriété intellectuelle et
      traitement de vos données personnelles.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="prose">
      <div class="encadre" style="margin-bottom:28px">
        <p style="margin:0"><strong>À compléter avant mise en ligne&nbsp;:</strong> les champs
          signalés par <em>[à compléter]</em> doivent être renseignés avec les informations
          officielles de la société (forme juridique, capital, SIRET, RCS, TVA, assurances,
          hébergeur). Ces mentions sont obligatoires au titre de l'article 6-III de la
          loi n°&nbsp;2004-575 du 21 juin 2004 pour la confiance dans l'économie numérique.</p>
      </div>

      <h2>1. Éditeur du site</h2>
      <ul>
        <li><strong>Dénomination sociale&nbsp;:</strong> ETS-BZH</li>
        <li><strong>Forme juridique&nbsp;:</strong> <em>[à compléter]</em></li>
        <li><strong>Capital social&nbsp;:</strong> <em>[à compléter]</em></li>
        <li><strong>Siège social&nbsp;:</strong> <em>[à compléter]</em></li>
        <li><strong>SIRET&nbsp;:</strong> <em>[à compléter]</em> — <strong>RCS&nbsp;:</strong> <em>[à compléter]</em></li>
        <li><strong>N° TVA intracommunautaire&nbsp;:</strong> <em>[à compléter]</em></li>
        <li><strong>Téléphone&nbsp;:</strong> <a href="tel:{TEL_LIEN}">{TEL}</a></li>
        <li><strong>E-mail&nbsp;:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><strong>Directeur de la publication&nbsp;:</strong> <em>[à compléter]</em></li>
      </ul>

      <h2>2. Assurances professionnelles</h2>
      <p>ETS-BZH est couverte par une assurance de responsabilité civile professionnelle et
        par une garantie décennale pour les travaux qui l'exigent.</p>
      <ul>
        <li><strong>Assureur&nbsp;:</strong> <em>[à compléter]</em></li>
        <li><strong>N° de contrat&nbsp;:</strong> <em>[à compléter]</em></li>
        <li><strong>Couverture géographique&nbsp;:</strong> France métropolitaine</li>
      </ul>

      <h2>3. Hébergement</h2>
      <ul>
        <li><strong>Hébergeur&nbsp;:</strong> <em>[à compléter]</em></li>
        <li><strong>Adresse&nbsp;:</strong> <em>[à compléter]</em></li>
        <li><strong>Téléphone&nbsp;:</strong> <em>[à compléter]</em></li>
      </ul>

      <h2>4. Propriété intellectuelle</h2>
      <p>L'ensemble des éléments du site (structure, textes, logo, identité visuelle, code
        source) est la propriété d'ETS-BZH ou fait l'objet d'une autorisation d'usage. Toute
        reproduction, représentation ou adaptation, totale ou partielle, sans autorisation
        écrite préalable est interdite et constituerait une contrefaçon au sens des articles
        L.335-2 et suivants du Code de la propriété intellectuelle.</p>

      <h2>5. Données personnelles (RGPD)</h2>
      <p>Les formulaires du site collectent les données strictement nécessaires au traitement
        de votre demande&nbsp;:</p>
      <ul>
        <li><strong>Données collectées&nbsp;:</strong> nom, téléphone, ville, département,
          type d'intervention, degré d'urgence et, le cas échéant, votre message.</li>
        <li><strong>Finalité&nbsp;:</strong> vous recontacter, établir un devis et organiser
          l'intervention demandée.</li>
        <li><strong>Base légale&nbsp;:</strong> votre consentement et l'exécution de mesures
          précontractuelles prises à votre demande.</li>
        <li><strong>Durée de conservation&nbsp;:</strong> 3 ans à compter du dernier contact
          pour les prospects&nbsp;; durée légale de conservation comptable pour les clients.</li>
        <li><strong>Destinataires&nbsp;:</strong> les services internes d'ETS-BZH et, le cas
          échéant, le technicien chargé de l'intervention. Aucune donnée n'est vendue ni cédée
          à des tiers à des fins commerciales.</li>
      </ul>
      <p>Conformément au Règlement (UE) 2016/679 et à la loi Informatique et Libertés, vous
        disposez d'un droit d'accès, de rectification, d'effacement, de limitation, d'opposition
        et de portabilité de vos données. Pour l'exercer, écrivez à
        <a href="mailto:{EMAIL}">{EMAIL}</a>. Vous pouvez également introduire une réclamation
        auprès de la CNIL (<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>

      <h2>6. Cookies</h2>
      <p>Ce site ne dépose aucun cookie publicitaire ni traceur tiers. Aucun outil de mesure
        d'audience n'est actif à ce jour. Si un outil de statistiques était ajouté
        ultérieurement, un bandeau de consentement conforme aux recommandations de la CNIL
        serait mis en place.</p>

      <h2>7. Liens hypertextes</h2>
      <p>Le site peut contenir des liens vers des sites tiers. ETS-BZH n'exerce aucun contrôle
        sur leur contenu et décline toute responsabilité à leur égard.</p>

      <h2>8. Médiation de la consommation</h2>
      <p>Conformément à l'article L.612-1 du Code de la consommation, tout consommateur a le
        droit de recourir gratuitement à un médiateur de la consommation en vue de la résolution
        amiable d'un litige. Médiateur compétent&nbsp;: <em>[à compléter]</em>.</p>

      <h2>9. Tarifs affichés</h2>
      <p>Les tarifs indiqués sur ce site sont des <strong>montants indicatifs TTC</strong>,
        donnés à titre d'information et susceptibles de varier selon la nature exacte de
        l'intervention, l'accessibilité, les pièces nécessaires et les éventuelles majorations
        (nuit, dimanche, jours fériés). Seul le devis gratuit établi après diagnostic et accepté
        par le client a valeur contractuelle.</p>
    </div>
  </div>
</section>

{cta_final("Une question sur nos prestations&nbsp;?",
           "Notre équipe vous répond directement par téléphone ou par e-mail.",
           "cta-mentions")}
</main>
""" + footer())


def page_cgu():
    titre = "Conditions Générales d'Utilisation — ETS-BZH"
    desc = ("Conditions générales d'utilisation du site ETS-BZH : objet, accès, devis, "
            "responsabilité et droit applicable.")
    fil = [("Accueil", "index.html"), ("CGU", "cgu.html")]
    return (
        head(titre, desc, "cgu.html", [ld_ariane(fil)])
        + topbar() + header() + ariane(fil) + f"""

<main id="contenu">

<section class="hero hero--compact">
  <div class="container">
    <span class="eyebrow">Conditions d'utilisation</span>
    <h1>Conditions Générales d'Utilisation</h1>
    <p class="hero__sub">Objet, accès au site, demandes de devis, tarifs, responsabilité
      et droit applicable.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="prose">
      <p><strong>Dernière mise à jour&nbsp;: {TODAY}</strong></p>

      <h2>Article 1 — Objet</h2>
      <p>Les présentes conditions générales d'utilisation (CGU) régissent l'accès et
        l'utilisation du site ets-bzh.fr, édité par ETS-BZH. Toute consultation du site implique
        l'acceptation pleine et entière des présentes CGU.</p>

      <h2>Article 2 — Accès au site</h2>
      <p>Le site est accessible gratuitement à tout utilisateur disposant d'un accès à Internet.
        Les frais de connexion et de matériel restent à la charge de l'utilisateur. ETS-BZH
        s'efforce d'assurer une disponibilité continue mais ne saurait être tenue responsable
        d'une interruption liée à une maintenance, une mise à jour ou un cas de force majeure.</p>

      <h2>Article 3 — Services proposés</h2>
      <p>Le site présente les prestations d'ETS-BZH en matière de dégorgement de canalisations,
        de plomberie et d'électricité sur les départements des Côtes-d'Armor&nbsp;(22), du
        Finistère&nbsp;(29), de l'Ille-et-Vilaine&nbsp;(35) et du Morbihan&nbsp;(56). Les
        informations publiées sont fournies à titre indicatif et peuvent être modifiées à tout
        moment.</p>

      <h2>Article 4 — Demandes de devis</h2>
      <ul>
        <li>Les formulaires permettent de solliciter un rappel ou un devis&nbsp;; ils ne
          constituent ni une commande, ni un engagement contractuel.</li>
        <li>Le devis est gratuit, sans engagement, et établi après diagnostic de la situation.</li>
        <li>Seul le devis signé ou expressément accepté par le client engage les parties.</li>
        <li>L'utilisateur s'engage à fournir des informations exactes permettant d'être
          recontacté.</li>
      </ul>

      <h2>Article 5 — Tarifs</h2>
      <p>Les tarifs affichés sur le site sont indicatifs, exprimés en euros TTC, et ne tiennent
        pas compte des pièces spécifiques ni des majorations applicables aux interventions de
        nuit, le dimanche et les jours fériés. Le prix définitif figure sur le devis validé
        avant intervention.</p>

      <h2>Article 6 — Droit de rétractation</h2>
      <p>Conformément aux articles L.221-18 et suivants du Code de la consommation, le
        consommateur dispose d'un délai de quatorze (14) jours pour exercer son droit de
        rétractation sur un contrat conclu hors établissement. Ce droit ne s'applique pas
        lorsque le client a expressément demandé une intervention d'urgence à domicile pour des
        travaux de réparation strictement nécessaires (article L.221-28 du même code). Dans ce
        cas, une demande d'exécution immédiate est recueillie auprès du client.</p>

      <h2>Article 7 — Propriété intellectuelle</h2>
      <p>Tous les contenus du site sont protégés par le droit de la propriété intellectuelle.
        Toute reproduction ou exploitation non autorisée est interdite. Voir les
        <a href="mentions-legales.html">mentions légales</a>.</p>

      <h2>Article 8 — Responsabilité</h2>
      <p>ETS-BZH met tout en œuvre pour fournir des informations exactes et actualisées, sans
        garantir leur exhaustivité. Les conseils de première urgence figurant sur le site
        (couper l'eau, couper le courant) sont donnés à titre informatif et ne se substituent
        pas à l'intervention d'un professionnel. ETS-BZH ne saurait être tenue responsable des
        dommages résultant d'une manipulation effectuée par l'utilisateur.</p>

      <h2>Article 9 — Données personnelles</h2>
      <p>Le traitement des données collectées via les formulaires est détaillé dans les
        <a href="mentions-legales.html">mentions légales</a>, section «&nbsp;Données personnelles
        (RGPD)&nbsp;».</p>

      <h2>Article 10 — Modification des CGU</h2>
      <p>ETS-BZH se réserve le droit de modifier les présentes CGU à tout moment. La version
        applicable est celle en vigueur à la date de consultation du site.</p>

      <h2>Article 11 — Droit applicable</h2>
      <p>Les présentes CGU sont soumises au droit français. En cas de litige, et après échec
        d'une résolution amiable ou d'une médiation de la consommation, les tribunaux français
        sont seuls compétents.</p>
    </div>
  </div>
</section>

{cta_final("Une intervention à planifier&nbsp;?",
           "Devis gratuit et sans engagement sur les quatre départements bretons.",
           "cta-cgu")}
</main>
""" + footer())


def page_404():
    liens = "".join('<a href="%s">%s %s (%s)</a>' % (url_landing(a, d), a["nom_court"],
                                                     d["nom"], d["num"])
                    for a in ACTIVITES for d in DEPARTEMENTS)
    return (
        head("Page introuvable (404) — ETS-BZH",
             "La page demandée n'existe pas. Retrouvez nos interventions en plomberie, "
             "dégorgement et électricité en Bretagne.", "404.html")
        .replace('<meta name="robots" content="index, follow, max-snippet:-1, '
                 'max-image-preview:large">', '<meta name="robots" content="noindex, follow">')
        + topbar() + header() + f"""

<main id="contenu">

<section class="hero hero--compact">
  <div class="container">
    <span class="eyebrow">Erreur 404</span>
    <h1>Cette page n'existe pas (ou plus)</h1>
    <p class="hero__sub">Le lien est peut-être erroné. Choisissez votre intervention et
      votre département ci-dessous, ou appelez-nous directement&nbsp;: c'est encore
      plus rapide.</p>
    <div class="hero__actions">
      <a class="btn btn--blanc btn--xl" href="tel:{TEL_LIEN}">{SVG['tel']} Appeler le {TEL}</a>
      <a class="btn btn--outline-blanc btn--xl" href="index.html">Retour à l'accueil</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Nos interventions en Bretagne</h2>
    <div class="liens-grid">{liens}</div>
  </div>
</section>
</main>
""" + footer())


# ============================================================== SITEMAP
def sitemap(pages):
    urls = ""
    for nom, prio, freq in pages:
        urls += ("\n  <url><loc>%s/%s</loc><lastmod>%s</lastmod>"
                 "<changefreq>%s</changefreq><priority>%s</priority></url>"
                 % (BASE, nom, TODAY, freq, prio))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s\n</urlset>' % urls)


# ================================================================= BUILD
def main():
    print("\nETS-BZH — génération du site\n" + "-" * 62)
    pages = [("index.html", "1.0", "weekly")]

    ecrire("index.html", page_index())
    for act in ACTIVITES:
        for dept in DEPARTEMENTS:
            nom = url_landing(act, dept)
            ecrire(nom, page_landing(act, dept))
            pages.append((nom, "0.9", "monthly"))

    ecrire("contact.html", page_contact())
    ecrire("mentions-legales.html", page_mentions())
    ecrire("cgu.html", page_cgu())
    ecrire("404.html", page_404())
    pages += [("contact.html", "0.8", "monthly"),
              ("mentions-legales.html", "0.3", "yearly"),
              ("cgu.html", "0.3", "yearly")]

    ecrire("sitemap.xml", sitemap(pages))
    ecrire("robots.txt",
           "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)

    print("-" * 62)
    print("%d pages HTML générées (12 landing pages + 5 pages annexes).\n" % (len(pages) + 1))


if __name__ == "__main__":
    main()
