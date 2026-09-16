# Site ETS-BZH — Plomberie · Dégorgement · Électricité (Bretagne)

Site vitrine statique orienté conversion pour **ETS-BZH**, avec 12 landing pages
ultra-ciblées (3 activités × 4 départements bretons) générées à partir d'un
template unique.

- **Téléphone :** 02 20 06 00 75 · **E-mail :** contact@etablissement-breizh.fr
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
| `assets/img/logo.jpg` | Source rognée de ses marges blanches et redimensionnée en 680 px | Image de partage (`og:image`) et `LocalBusiness` |
| `assets/img/logo-emblem.png` | Disque découpé dans la source, fond rendu transparent | En-tête (haut à gauche) et icône Apple |
| `assets/img/favicon.png` | Même emblème en 96 px | Favicon |

Les déclinaisons sont produites par découpe, détourage circulaire et
redimensionnement du fichier source : les pixels proviennent tous de l'original.
Total servi aux visiteurs : 59 Ko.

Le rognage ignore un liseré d'artefacts d'export présent sur le bord droit du
fichier source (dernière colonne de pixels), qui décentrait le logo. Le contenu
est désormais centré à 0,5 px près, et la plaque du pied de page est centrée
exactement dans sa colonne à toutes les largeurs.

Le logo apparaît dans l'en-tête de chaque page, en haut à gauche : l'emblème
est associé au nom « ETS-BZH » en texte HTML plutôt qu'à l'image complète, car à
78 px de hauteur de barre le bandeau du logo descendrait sous 10 px et
deviendrait illisible. Le pied de page ne reprend pas le logo.

### Arrière-plan des en-têtes

Le bandeau haut de chaque page utilise, de bas en haut :

1. `assets/img/fond-equipe.webp` (repli `.jpg`) — photo d'un technicien devant un
   véhicule ETS-BZH, servie en `image-set()` ; une version `-mobile` allégée
   prend le relais sous 720 px
2. un dégradé bleu très couvrant (0,80 à 0,93 d'opacité) qui rend la photo
   discrète tout en gardant les textes lisibles
3. `motif-plomberie.svg` à 6 % d'opacité, pour la texture
4. un voile latéral côté texte

Contraste mesuré sur le rendu réel, 13 zones de texte réparties sur desktop et
mobile : **5,21:1 au pire cas** (seuil WCAG AA : 4,5:1). Pour rendre la photo
plus ou moins visible, ajustez les opacités du dégradé de `.hero` — les baisser
révèle la photo, les augmenter l'efface.

Poids : 89 Ko en WebP desktop (151 Ko en repli JPEG), 33 Ko en WebP mobile.


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

## Emplacements photo

**6 photos sont déjà en place** (3 dégorgement, 2 plomberie, 1 équipe/véhicule).
Les emplacements restants attendent vos fichiers.

Le site prévoit **23 emplacements photo** répartis sur toutes les pages :

| Page | Emplacements |
| --- | --- |
| Accueil | Galerie « ETS-BZH en images » (6 photos) + photo d'équipe dans « À propos » |
| Chaque landing page | Galerie « Nos interventions en images » (4 photos) + photo d'équipe dans la section urgences |
| Contact | 1 photo (atelier / matériel) |

Les galeries sont **partagées par activité** : les 4 pages Dégorgement affichent
les mêmes 4 photos, idem pour Plomberie et Électricité. Cela fait 23 fichiers à
fournir, pas 68. La galerie de l'accueil réutilise les fichiers des pages métier —
elle n'a donc pas ses propres images à fournir.

État actuel :

| Page | Fournies | À fournir |
| --- | --- | --- |
| Dégorgement | WC, lavabo, douche | curage haute pression, photo d'équipe |
| Plomberie | diagnostic sous lavabo, chauffe-eau | réseau d'alimentation, salle de bain, photo d'équipe |
| Électricité | — | 4 photos de galerie + photo d'équipe |
| Accueil | les 5 ci-dessus + équipe/véhicule | — |
| Contact | — | atelier |

### Comment ajouter une photo

Déposez le fichier dans `assets/img/photos/` **sous le nom exact attendu** — la
photo remplace aussitôt le cadre d'attente, sans toucher au code ni relancer le
générateur. La liste complète des noms de fichiers est dans
`assets/img/photos/LISEZ-MOI.txt`, et chaque cadre d'attente affiche lui-même le
nom qu'il attend.

Format conseillé : JPEG 1200 × 900 px (galeries) ou 1200 × 800 px (photos
larges), moins de 250 Ko. Le recadrage est automatique et centré
(`object-fit: cover`).

Pour masquer les emplacements non encore remplis, décommentez dans
`assets/css/style.css` :

```css
.photo--vide { display: none; }
```

Les légendes et textes alternatifs se modifient dans `tools/data.py`
(clés `photos`, `photo_equipe`, `PHOTOS_ACCUEIL`, `PHOTO_EQUIPE`,
`PHOTO_CONTACT`), puis `python3 tools/build.py`.

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
une feuille CSS (~28 Ko), un script JS (~9 Ko), le logo et le motif (~45 Ko), et
la photo de fond (89 Ko en WebP, 33 Ko sur mobile). Polices système.
Pages HTML de ~36 Ko.

## Réception des formulaires

Par défaut, l'envoi ouvre la messagerie du visiteur avec une demande pré-remplie
vers `contact@etablissement-breizh.fr`. Pour recevoir les demandes directement en base ou par
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
- [ ] **Photos** — remplir les 23 emplacements avec vos propres chantiers
      (voir « Emplacements photo »). N'utilisez que des visuels dont vous
      détenez les droits : présenter des images de banque comme vos
      réalisations est trompeur et juridiquement risqué
- [ ] **Endpoint de formulaire** (voir ci-dessus)
- [ ] **Domaine** — `SITE["url"]` vaut encore `https://www.ets-bzh.fr` alors que
      l'e-mail est passé à `@etablissement-breizh.fr`. Si le site doit être publié
      sur `etablissement-breizh.fr`, changez aussi cette valeur dans
      `tools/data.py` : elle alimente les URLs canoniques, le sitemap et le
      JSON-LD
