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

| Fichier | Usage |
| --- | --- |
| `assets/img/logo-mark.svg` | Emblème seul (disque) — en-tête, pied de page |
| `assets/img/logo.svg` | Logo complet : emblème + bandeau ETS-BZH + baseline — partage social |
| `assets/img/favicon.svg` | Favicon (copie de l'emblème) |

> Ces fichiers sont une **reconstruction vectorielle** du logo fourni : le fichier
> source n'était pas disponible sur le dépôt. Pour utiliser l'original, déposez-le
> dans `assets/img/` et remplacez les références dans `tools/build.py`
> (fonctions `header()` et `footer()`), puis relancez `python3 tools/build.py`.
> Un SVG est préférable (net à toutes les tailles) ; un PNG détouré convient aussi.

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
une feuille CSS (~28 Ko), un script JS (~8 Ko), un logo SVG, polices système.
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
- [ ] **Logo** — remplacer la reconstruction vectorielle par le fichier source
      officiel si vous le possédez (voir section « Logo »)
