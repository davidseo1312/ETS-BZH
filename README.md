# Site ETS-BZH — Plomberie · Dégorgement · Électricité (Bretagne)

Site vitrine statique orienté conversion pour **ETS-BZH**, avec 12 landing pages
ultra-ciblées (3 activités × 4 départements bretons) générées à partir d'un
template unique.

- **Téléphone :** 02 20 06 00 75 · **E-mail :** contact@ets-bzh.fr
- **Zones :** Côtes-d'Armor (22), Finistère (29), Ille-et-Vilaine (35), Morbihan (56)

## Arborescence

| Fichier | Rôle |
| --- | --- |
| `index.html` | Accueil / hub — sélecteur d'activité et de département |
| `degorgement-canalisation-{22,29,35,56}.html` | 4 landing pages Dégorgement |
| `plomberie-depannage-{22,29,35,56}.html` | 4 landing pages Plomberie |
| `electricite-urgence-{22,29,35,56}.html` | 4 landing pages Électricité |
| `contact.html` | Formulaire de devis express (département + type de panne) |
| `mentions-legales.html` · `cgu.html` | Pages légales |
| `404.html` · `sitemap.xml` · `robots.txt` | Annexes SEO |

*(les noms de fichiers réels portent le slug du département, ex.
`plomberie-depannage-cotes-d-armor-22.html`)*

## Structure d'une landing page

1. Barre d'infos + **header sticky** (logo à gauche, bouton d'appel à droite)
2. **Hero** : H1 localisé, sous-titre de réassurance, formulaire de rappel immédiat
3. Bandeau de chiffres clés
4. **Nos prestations** (8 blocs carrés)
5. Situations d'urgence + zone d'intervention
6. **Pourquoi choisir ETS-BZH** (24/7, devis gratuit, artisans qualifiés, décennale)
7. Tarifs indicatifs (transparence)
8. Processus en 4 étapes
9. **Avis clients & témoignages** localisés
10. Communes desservies (maillage local)
11. FAQ (balisage `FAQPage`)
12. Contenu rédactionnel SEO géolocalisé
13. **CTA final** : bannière bleue, bouton d'appel géant + formulaire court
14. Maillage interne + footer + barre d'appel fixe mobile

## Logo

Le logo officiel fourni par le client est utilisé **tel quel** — aucune
reconstruction.

| Fichier | Provenance | Usage |
| --- | --- | --- |
| `assets/img/logo-original.jpg` | Fichier source intact (1407 × 768) | Archive de référence, non chargé par les pages |
| `assets/img/logo.jpg` | Source rognée de ses marges blanches et redimensionnée en 680 px | Pied de page (sur plaque blanche) et `og:image` |
| `assets/img/logo-emblem.png` | Disque découpé dans la source, fond rendu transparent | En-tête (haut à gauche) et icône Apple |
| `assets/img/favicon.png` | Même emblème en 96 px | Favicon |

Les déclinaisons sont produites par découpe, détourage circulaire et
redimensionnement du fichier source : les pixels proviennent tous de l'original.
Total servi aux visiteurs : 59 Ko.

Le rognage ignore un liseré d'artefacts d'export présent sur le bord droit du
fichier source (dernière colonne de pixels), qui décentrait le logo. Le contenu
est désormais centré à 0,5 px près, et la plaque du pied de page est centrée
exactement dans sa colonne à toutes les largeurs.

Dans l'en-tête, l'emblème est associé au nom « ETS-BZH » en texte HTML plutôt
qu'à l'image complète : à 78 px de hauteur de barre, le bandeau du logo
descendrait sous 10 px et deviendrait illisible. Le logo complet est affiché en
taille lisible dans le pied de page de chaque page, centré sur une plaque
blanche (340 px en desktop, 300 px en tablette, 250 px en mobile).

### Arrière-plan des en-têtes

Le bandeau haut de chaque page (`.hero`) affiche un réseau de plomberie vectoriel
(tuyaux, brides, vanne à volant, manomètre, siphon). Le motif est **raccordable à
l'infini** : les tuyaux traversent les bords du carreau aux mêmes coordonnées, il se
répète donc sans coupure quelle que soit la largeur d'écran.

Deux couches le rendent lisible, dans `assets/css/style.css` :

- `.hero::before` — le motif, `opacity: .11`
- `.hero::after` — un voile dégradé foncé côté texte

Contraste vérifié sur les 17 pages : **5,8:1 au pire cas** (seuil WCAG AA : 4,5:1).
Pour renforcer ou atténuer le motif, ajustez la seule valeur `opacity` de
`.hero::before`.

## Charte graphique

| Élément | Valeur |
| --- | --- |
| Bleu Marseille (principal) | `#005580` |
| Bleu clair (dégradés) | `#006699` |
| Blanc | `#FFFFFF` |
| Bleu nuit (textes) | `#0A1A26` / `#13293A` |
| Rouge urgence (CTA secondaire) | `#D43F1A` |
| Angles | `border-radius: 0` appliqué globalement |

## Régénérer le site

Le HTML de la racine est **généré** : modifiez le contenu dans `tools/`, jamais
les fichiers `.html` directement.

```bash
python3 tools/build.py
```

- `tools/data.py` — contenus éditoriaux (activités, prestations, tarifs, FAQ,
  avis, départements et communes)
- `tools/build.py` — templates, rendu HTML, JSON-LD, sitemap

Aucune dépendance : Python 3 seul suffit. Prévisualisation locale :

```bash
python3 -m http.server 8000   # puis http://localhost:8000
```

## Performance

Aucune requête tierce (pas de Google Fonts, pas de framework, pas de tracker) :
une feuille CSS (~27 Ko), un script JS (~8 Ko), le logo et le motif (43 Ko au
total), polices système.
Pages HTML de ~36 Ko.

## Réception des formulaires

Par défaut, l'envoi ouvre la messagerie du visiteur avec une demande pré-remplie
vers `contact@ets-bzh.fr`. Pour recevoir les demandes directement en base ou par
webhook, renseignez `FORM_ENDPOINT` en haut de `assets/js/main.js` :

```js
var FORM_ENDPOINT = "https://…"; // reçoit un POST JSON
```

Un champ piège (`_gotcha`) bloque les robots de formulaire.

## À compléter avant mise en ligne

- [ ] **Mentions légales** — forme juridique, capital, siège, SIRET, RCS, TVA,
      directeur de publication, assureur et n° de contrat, hébergeur, médiateur
      de la consommation (champs marqués *[à compléter]*)
- [ ] **Avis clients** — les témoignages et la note « 4,8/5 » sont des contenus
      d'exemple : remplacez-les par de vrais avis vérifiés avant publication
      (l'affichage d'avis fictifs est une pratique commerciale trompeuse)
- [ ] **Tarifs** — vérifier les montants indicatifs de `tools/data.py`
- [ ] **Endpoint de formulaire** (voir ci-dessus)
- [ ] **Domaine** — `SITE["url"]` dans `tools/data.py` alimente les URLs
      canoniques et le sitemap
