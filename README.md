# Site ETS-BZH — Plomberie · Dégorgement · Électricité (Bretagne)

Site vitrine statique orienté conversion pour **ETS-BZH**, avec 12 landing pages
ultra-ciblées (3 activités × 4 départements bretons) et 80 articles géolocalisés
(20 par département), générés à partir de templates uniques.

- **Téléphone :** 02 20 06 00 75 · **E-mail :** contact@etablissement-breizh.fr
- **Zones :** Côtes-d'Armor (22), Finistère (29), Ille-et-Vilaine (35), Morbihan (56)

## Arborescence

Les URL sont **sans extension** : chaque page est écrite dans son propre dossier,
sous le nom `index.html`. Un serveur sert alors `/contact/` sans aucune règle de
réécriture — cela fonctionne sur GitHub Pages, Netlify, OVH, Apache ou nginx,
sans configuration.

| URL publique | Fichier | Rôle |
| --- | --- | --- |
| `/` | `index.html` | Accueil / hub |
| `/degorgement-canalisation-{dept}/` | `…/index.html` | 4 landing pages Dégorgement |
| `/plomberie-depannage-{dept}/` | `…/index.html` | 4 landing pages Plomberie |
| `/electricite-urgence-{dept}/` | `…/index.html` | 4 landing pages Électricité |
| `/conseils/` | `conseils/index.html` | Rubrique conseils, page 1 sur 7 |
| `/conseils/page-{n}/` | `…/index.html` | Pages 2 à 7 de la rubrique |
| `/conseils/{dept}/` | `…/index.html` | Sous-catégorie départementale (20 articles, 2 pages) |
| `/conseils/{article}/` | `…/index.html` | 80 articles (20 par département) |
| `/contact/` | `contact/index.html` | Formulaire de devis express |
| `/mentions-legales/` | `mentions-legales/index.html` | Éditeur, hébergeur, identité, assurances |
| `/politique-de-confidentialite/` | `…/index.html` | RGPD : finalités, bases légales, droits |
| `/cgu/` | `cgu/index.html` | Conditions générales d'utilisation |
| `/404.html` | racine | Page d'erreur (servie automatiquement) |
| `/sitemap.xml` · `/robots.txt` | racine | Annexes SEO |

*(`{dept}` vaut `cotes-d-armor-22`, `finistere-29`, `ille-et-vilaine-35` ou
`morbihan-56`)*

Les chemins des ressources sont **absolus** (`/assets/…`) puisque les pages
vivent dans des sous-dossiers. Le site doit donc être servi à la racine d'un
domaine, pas dans un sous-répertoire.

## Structure d'une landing page

1. Barre d'infos (numéro en clair) + **header sticky** (logo à gauche, bouton
   d'appel à droite)
2. **Hero** : H1 localisé, accroche, **formulaire de rappel à deux champs**
3. Bandeau de chiffres clés
4. **Nos prestations** (8 blocs carrés)
5. Photos de chantiers, chacune décrite
6. **Tarifs indicatifs** (transparence)
7. **Avis clients & témoignages** localisés
8. Situations d'urgence
9. Communes desservies + carte cliquable (maillage local)
10. **Pourquoi choisir ETS-BZH** (24/7, devis gratuit, artisans qualifiés, décennale)
11. Processus en 4 étapes
12. FAQ (balisage `FAQPage`)
13. Contenu rédactionnel SEO géolocalisé
14. **CTA final** : bannière bleue, bouton d'appel géant + formulaire court
15. Maillage interne + footer + barre d'appel fixe mobile

**Les tarifs et les avis ont été remontés** de la 7e et de la 9e place à la 6e
et la 7e, juste après les photos. Mesuré sur mobile avant ce changement : les
tarifs arrivaient à 12 628 px, soit le 15e écran, et les avis à 14 810 px, le
18e. Ce sont pourtant les deux arguments qui décident un appel. Ils sont
maintenant à 7 344 px et 8 490 px, et le texte SEO long — qui n'a besoin d'être
lu par personne — est passé derrière.

## Articles

Quatre-vingts articles, **vingt par département**, publiés sous `/conseils/`.
Ils ne répètent pas les pages métier&nbsp;: ils visent une autre intention de
recherche. Quelqu'un qui tape « plombier Saint-Brieuc » cherche une
entreprise&nbsp;; quelqu'un qui tape « fosse septique qui déborde » cherche quoi
faire dans les cinq minutes. Ce sont deux visiteurs différents, et le second
appelle plus vite que le premier si on lui répond clairement.

Ils se répartissent en **trois familles**, qui ne se cannibalisent pas parce
qu'elles répondent à trois questions différentes&nbsp;:

| Famille | Nombre | Question à laquelle l'article répond |
| --- | --- | --- |
| **Guides de situation** | 40 (10 par département) | *Que faire&nbsp;?* Une panne précise, la marche à suivre, les erreurs à éviter |
| **Articles de zone** | 24 (6 par département, 2 par métier) | *Qui intervient chez moi, et pour quoi&nbsp;?* Un contexte d'intervention, détaillé commune par commune |
| **Articles d'installation** | 16 (4 par département) | *Qu'est-ce qu'on pose, combien de temps, comment on choisit&nbsp;?* Un remplacement ou une pose, de la décision à la mise en service |

Les trois familles visent des intentions de recherche distinctes, et c'est ce
qui les empêche de se concurrencer&nbsp;: « WC bouché que faire » (guide),
« plombier Quiberon » (zone), « remplacer ballon d'eau chaude » (installation)
ne ramènent pas les mêmes pages ni les mêmes visiteurs.

### Guides de situation (40)

**Chaque article traite une situation différente.** Il n'y a pas un même sujet
décliné quatre fois avec un nom de ville changé&nbsp;: les quarante articles
couvrent quarante pannes distinctes, réparties 15 dégorgement, 15 plomberie et
10 électricité.

| Dép. | Dégorgement | Plomberie | Électricité |
| --- | --- | --- | --- |
| **22** | fosse septique qui déborde · WC bouché · cave inondée · odeur d'égout | fuite enterrée · plus d'eau chaude · radiateur qui fuit | panne après tempête · disjoncteur qui saute · fusibles à broche |
| **29** | eaux usées qui remontent · évier bouché · racines · regard qui déborde | canalisation gelée · fuite sous évier · chasse d'eau · plus d'eau au robinet | surtension après orage · installation inondée |
| **35** | colonne bouchée · WC en appartement · odeur d'égout · évacuation lente | dégât des eaux du voisin · lave-linge qui inonde · fuite encastrée · fuite vers le dessous | puissance insuffisante · prise hors service |
| **56** | WC en location · bac à graisse · pompe de relevage | chauffe-eau qui fuit · facture anormale · vanne bloquée · coup de bélier | odeur de brûlé · ballon qui ne chauffe plus · borne de recharge |

### Articles de zone (24)

Six par département, **deux par métier** — dégorgement, plomberie,
électricité. Là où un guide de situation répond à « mon WC est bouché », un
article de zone répond à « qui intervient dans ma commune, pour ce type de
problème, et dans quel délai ». C'est la requête de quelqu'un qui a déjà
compris son problème et qui cherche un intervenant&nbsp;: il est beaucoup plus
proche de l'appel.

| Dép. | Dégorgement | Plomberie | Électricité |
| --- | --- | --- | --- |
| **22** | débouchage de nuit et le week-end · inspection caméra et curage | recherche de fuite non destructive · dépannage de chauffe-eau | remise en sécurité après sinistre · mise aux normes du tableau |
| **29** | vidange de fosse et bac de relevage · eaux pluviales bouchées | fermeture et réouverture de maison · dégât des eaux et assèchement | électricité du bâti ancien · panne de chauffage en hiver |
| **35** | dégorgement en copropriété et en location · regards et réseaux extérieurs | plomberie locative (bailleurs, agences) · petites surfaces et colocations | électricité des parties communes · mise en sécurité avant location ou vente |
| **56** | campings, hôtels et restaurants · réseaux du littoral | résidences secondaires et propriétaires absents | calcaire et corrosion saline* · électricité de bord de mer · éclairage extérieur et portails |

<sub>* « calcaire et corrosion saline » est un article de plomberie.</sub>

### Articles d'installation (16)

Quatre par département, répartis **2 plomberie, 1 électricité, 1
dégorgement** — la plomberie pèse le double parce que c'est là que se
concentre la demande d'installation.

| Dép. | Plomberie | Électricité | Dégorgement |
| --- | --- | --- | --- |
| **22** | remplacer un ballon d'eau chaude · poser radiateurs et sèche-serviettes | électricité de cuisine (circuits dédiés) | créer ou refaire des évacuations |
| **29** | rénover une salle de bain · remplacer un WC (suspendu, broyeur) | compteur, branchement et puissance | raccordement au tout-à-l'égout |
| **35** | baignoire remplacée par une douche · robinetterie et colonnes | remplacer un tableau électrique | installer un poste de relevage |
| **56** | chauffe-eau thermodynamique ou électrique · canalisations plomb et acier | installer une VMC | poser un clapet anti-retour |

Ils reprennent la même structure que les autres — marche à suivre, bloc
sécurité, sections de fond, bloc commune par commune, FAQ — mais l'angle est
la **décision et la pose**&nbsp;: quel appareil, quelles conditions, combien
de temps de chantier, ce que comprend réellement un remplacement, et ce que
l'équipement demandera ensuite.

**Trois points de rédaction méritent d'être signalés**, parce qu'ils engagent
l'entreprise et pas seulement le référencement&nbsp;:

- L'article sur le **compteur** dit explicitement que le compteur et le
  disjoncteur de branchement appartiennent au gestionnaire de réseau, qu'aucun
  électricien privé n'intervient dessus, et qu'un changement de puissance se
  demande au fournisseur. Promettre le contraire aurait été à la fois faux et
  intenable.
- L'article sur le **raccordement au tout-à-l'égout** renvoie au service
  d'assainissement de la commune pour tout ce qui relève du règlement local
  (délais, dérogations, participation financière), qui varie d'une
  collectivité à l'autre.
- L'article **baignoire → douche** mentionne l'existence d'aides à
  l'adaptation du logement sans en nommer aucune ni en chiffrer le montant&nbsp;:
  les dispositifs et leurs conditions changent trop souvent pour être gravés
  dans une page statique.

**Le bloc commune par commune.** C'est ce qui distingue cette famille. Chaque
article nomme **six communes du département** et dit, pour chacune, quelque
chose de vrai et de spécifique au sujet traité&nbsp;: pourquoi les réseaux
s'ensablent à Guidel et pas à Pontivy, pourquoi une intervention à Belle-Île se
prépare en mars et pas en août, pourquoi le parc locatif rennais appelle pour
des chauffe-eau de placard. Les notes ne sont jamais interchangeables&nbsp;: un
même nom de commune reçoit une note différente d'un article à l'autre, parce
que le sujet change.

Les articles d'installation le portent aussi, avec des notes orientées
pose&nbsp;: place disponible, type de réseau, contrainte d'accès, bâti local.

Ce bloc est généré par `bloc_villes()` (`tools/build.py`) à partir de la clé
`villes` de l'article — une liste de couples `(commune, note)`. Il alimente
aussi le `areaServed` du `LocalBusiness` de la page, qui porte alors les six
communes citées plutôt que la liste générique du département. Un pied de bloc
nomme huit communes supplémentaires et rappelle que le délai est annoncé au
téléphone avant tout déplacement.

Visuellement, c'est une liste à deux colonnes (`190px 1fr` en desktop,
empilée sous 720&nbsp;px), nom en Barlow Condensed, note en gris, séparée par
des filets — sans puce ni pastille, comme le reste du corps d'article.

**Structure de chaque article** (`page_article` dans `tools/build.py`)&nbsp;:

1. Bandeau avec le titre, le résumé et deux boutons d'appel.
2. **Ligne de contexte**&nbsp;: date de mise à jour, temps de lecture, métier et
   département.
3. **Sommaire ancré** vers chaque section.
4. **« À faire tout de suite »**&nbsp;: la marche à suivre numérotée, suivie d'un
   bouton d'appel pleine largeur.
5. **Avertissement de sécurité**, sur un filet ambre.
6. Trois à cinq sections de fond, chacune avec son ancre.
7. Un **lien contextuel** vers la page métier du département.
8. Une **photo d'intervention** légendée.
9. Un **bloc de proximité**&nbsp;: communes desservies et liens vers les trois
   pages métier du département.
10. FAQ balisée `FAQPage`, bandeau de rappel, trois articles liés.

Neuf liens d'appel par article.

### Référencement des articles

Chaque article porte quatre blocs de données structurées&nbsp;:

- **`Article`** — titre, description, dates de publication et de modification,
  nombre de mots, rubrique, mots-clés, image, et un nœud `about` de type
  `Service` qui relie le métier à la zone desservie.
- **`LocalBusiness`** (`Plumber` ou `Electrician` selon le métier) — nom,
  téléphone, `areaServed` avec le département **et** ses six principales
  communes, horaires 24h/24 et 7j/7. Un article est souvent la page d'entrée
  depuis une recherche d'urgence&nbsp;: il doit porter lui-même l'entreprise et
  sa zone, pas seulement renvoyer vers la page métier.
- **`FAQPage`** — les quatre questions de fin d'article.
- **`BreadcrumbList`** — Accueil › Conseils › Département › Article.

S'y ajoutent `og:type=article` et les métadonnées `article:published_time`,
`article:modified_time` et `article:section`.

**Signaux locaux.** Le bloc de proximité nomme le département, ses dix communes
principales et renvoie vers les trois pages métier correspondantes avec des
ancres descriptives. Le lien contextuel en fin de corps de texte utilise une
ancre du type « dégorgement dans les Côtes-d'Armor », avec trois tournures
alternées pour qu'elle ne soit pas identique sur soixante-quatre pages. La légende de
la photo porte elle aussi le métier et le département.

**Sommaire ancré.** Chaque `<h2>` reçoit un identifiant stable, et le sommaire
pointe dessus. C'est utile au lecteur sur un article de 800 mots, et c'est ce
que Google utilise pour proposer des liens de saut directement dans ses
résultats.

**Non-redondance mesurée.** Le contenu est comparé texte contre texte avec
`difflib.SequenceMatcher`, sur le texte éditorial des 80 articles et sur le
rendu réel des 12 pages métier.

| Comparaison | Similarité |
| --- | --- |
| La paire d'articles la plus proche sur 3 160 paires | **12,9&nbsp;%** |
| Article à bloc communal ↔ page métier la plus proche | **9,4 à 14,2&nbsp;%** (moyenne 11,8&nbsp;%) |
| *Pour mémoire&nbsp;:* 2 pages d'un même métier entre elles | 84–90&nbsp;% |

Aucune paire d'articles ne dépasse 13&nbsp;%. Les paires les plus exposées ont
été vérifiées une à une plutôt que laissées au hasard du maximum
global&nbsp;: « remplacer un ballon » contre « dépannage de chauffe-eau »
(2,0&nbsp;%), « remplacer un tableau » contre « mise aux normes du tableau »
(4,7&nbsp;%), « installer un poste de relevage » contre « pompe de relevage en
panne » (2,9&nbsp;%), « poser un clapet » contre « réseaux du littoral »
(2,1&nbsp;%). Toutes restent sous 5&nbsp;%.

**Volume.** Environ 74 000 mots, moyenne 929 mots par article.

### Mise en forme des articles

Les numéros d'étape et les puces de liste étaient des **pastilles carrées
pleines**, rouges pour la marche à suivre et bleues pour les listes. Sur un
article entier, cela donnait un air de notice d'avertissement plutôt que de
conseil professionnel — et dans les listes, la puce de `.prose` doublait le
marqueur, ce qui faisait deux carrés par ligne.

La hiérarchie repose désormais sur la typographie et des filets&nbsp;:

- les numéros d'étape sont de **grands chiffres en Barlow Condensed**, sans
  fond, séparés par des filets fins&nbsp;;
- les listes utilisent une **coche verte fine**, sans aplat, avec un filet entre
  les éléments&nbsp;;
- l'encadré de marche à suivre est une carte blanche avec un filet rouge à
  gauche et une ombre douce, au lieu d'un cadre rouge plein&nbsp;;
- l'avertissement passe sur un fond ivoire et un filet ambre.

Le seul aplat de couleur restant dans le corps de l'article est le **bouton
d'appel**, et c'est voulu&nbsp;: c'est le seul élément qui doit attirer l'œil.

**Ancrage local.** Chaque article traite le contexte réel du département plutôt
que de remplacer un nom de ville dans un texte générique&nbsp;: assainissement non
collectif et nappes hautes dans l'arrière-pays costarmoricain, résidences
secondaires non chauffées et collecteurs anciens en Finistère, colonnes
collectives et rotation locative sur Rennes métropole, locations saisonnières et
air marin dans le Morbihan.

**Le contenu vit dans `tools/articles.py`**, séparé de `tools/data.py`&nbsp;: un
article se modifie sans toucher aux données du site, et s'ajoute en écrivant un
dictionnaire de plus dans la liste `ARTICLES`. Tout le reste suit
automatiquement&nbsp;: page générée, entrée au sitemap, classement par département
sur l'index, et vignettes de maillage.

**Pagination et sous-catégories.** Quatre-vingts vignettes sur une seule page
ne se lisent pas. La rubrique est donc découpée à **12 articles par page**
(quatre lignes de trois), avec une barre de numéros en bas, et une **barre de
sous-catégories** en haut&nbsp;: tous les départements, puis un lien par
département avec son compteur.

```
/conseils/                        page 1 sur 7, tous départements
/conseils/page-2/  … page-7/      la suite
/conseils/cotes-d-armor-22/       les 20 articles du 22, page 1 sur 2
/conseils/cotes-d-armor-22/page-2/
/conseils/finistere-29/           les 20 du 29   (idem 35 et 56)
```

Trois choix méritent d'être expliqués&nbsp;:

- **Ce sont des liens, pas un filtre en JavaScript.** Chaque sous-catégorie a sa
  propre URL, donc un titre, une description et un `<h1>` qui lui sont propres —
  « Conseils d'urgence dans le Finistère » se positionne, pas un paramètre
  d'URL. Elle est partageable, indexable, et elle fonctionne sans script.
- **Les intertitres de département subsistent dans la liste paginée.** Les
  articles sont triés par département puis par métier, et un `<h2>` réapparaît à
  chaque changement de département&nbsp;: même coupée en tranches de douze, la
  page reste lisible.
- **Chaque page a son propre `canonical` et son propre titre**, et les pages 2 à
  7 portent « Page N sur 7 » en tête de description. Sans cela, Google verrait
  sept pages au résumé identique.

Le découpage est générique&nbsp;: `url_conseils()`, `articles_tries()` et
`nb_pages()` servent aussi bien à la liste complète qu'aux sous-catégories. Les
pages départementales comptent aujourd'hui deux pages chacune (20 articles pour
12 par page)&nbsp;; la barre de numéros y est apparue d'elle-même, sans rien
changer au code.

**Maillage.** Chaque page métier affiche les **quatre premiers articles** de son
département, sous un intertitre qui renvoie à la sous-catégorie complète — vingt
vignettes noieraient le bas de page. Le fil d'Ariane d'un article passe par son
département&nbsp;: Accueil › Conseils d'urgence › Côtes-d'Armor (22) › WC bouché.

## Pages Google Ads (hors site)

**52 pages d'atterrissage électricité** conçues pour le trafic payant et rien
d'autre&nbsp;: une par département, et une par commune citée.

| Niveau | Nombre | URL |
| --- | --- | --- |
| Département | 4 | `/electricite-urgence-{departement}-{num}-2/` |
| Commune | 48 | `/electricite-urgence-{commune}-{num}/` |

**Elles vivent à la racine, sans préfixe qui les désigne.** Une URL en
`/ads/` annonce à qui la lit — visiteur, concurrent, régie — qu'elle est une
page publicitaire. Elles reprennent donc le nommage des pages publiques.

**Le suffixe `-2` ne concerne que les quatre pages départementales**, dont
l'URL serait sinon identique à celle de la page métier publique du même
département (`/electricite-urgence-cotes-d-armor-22/`). Les communes n'ont
pas de page publique&nbsp;: leur URL est libre, et aucun suffixe ne vient
l'alourdir. Contrôlé au build&nbsp;: les 52 URL sont uniques et aucune ne
heurte une page publique.

**Une seule fabrique pour les deux.** `page_ads(dept, ville=None)` produit la
page départementale ou la page commune&nbsp;; la seconde reprend exactement la
première en substituant le lieu partout où il apparaît. Ce qui change
réellement d'une commune à l'autre&nbsp;: la note locale en chapeau de la
section zone, les onze communes voisines proposées, et les communes qui
signent les avis.

**Le maillage.** Sur une page départementale, les douze communes sont des
liens vers leur propre page. Sur une page commune, les onze autres le sont, et
un lien ramène à la page départementale. Un visiteur arrivé sur la mauvaise
commune trouve la sienne au lieu de repartir. Les noms portent un
soulignement jaune&nbsp;: un lien qui ne se voit pas n'est pas cliqué.

**Les prépositions sont calculées**, pas concaténées&nbsp;: `a_ville()` et
`de_ville()` contractent l'article qui fait partie du nom de la commune. Sans
elles, une page annoncerait «&nbsp;électricien d'urgence à Le
Relecq-Kerhuon&nbsp;»&nbsp;; elle annonce «&nbsp;au Relecq-Kerhuon&nbsp;».

**Elles sont étanches par construction**, et c'est vérifié à chaque build&nbsp;:

- **aucun lien** depuis une page du site ne pointe vers elles&nbsp;;
- elles sont **absentes du sitemap** — dans `main()`, elles sont écrites sans
  être ajoutées à la liste `pages` qui alimente `sitemap.xml`&nbsp;;
- elles portent `<meta name="robots" content="noindex, nofollow">` et **aucune
  balise canonique**.

`robots.txt` n'interdit volontairement rien, et il ne le pourrait plus par
préfixe puisque ces pages vivent à la racine. De toute façon un `Disallow`
empêcherait Googlebot de lire le `noindex`, et l'URL pourrait alors
apparaître en résultat sans description — l'inverse de l'effet recherché. Le
`noindex` seul fait le travail, et AdsBot garde l'accès dont la régie a
besoin pour contrôler la page.

**L'étanchéité est vérifiée fichier par fichier**, pas au doigt mouillé&nbsp;:
les 52 pages portent toutes `noindex, nofollow`, aucune page publique ne
pointe vers l'une d'elles, aucune n'est au sitemap, le numéro du site
n'apparaît sur aucune page Ads et le numéro Ads sur aucune page publique.

**Un numéro distinct.** Ces 172 pages portent le **06 20 06 01 96**, et lui seul —
le numéro du site n'y figure nulle part. Tout appel sur ce numéro vient donc
d'une annonce, sans dépendre du suivi d'appel de la régie. Le formulaire
transmet en plus un champ masqué `source` (« ADS Électricité Saint-Brieuc
(22) »), que
`formulaire.php` reprend en préfixe du sujet du courriel&nbsp;: les prospects
payants se distinguent au premier coup d'œil dans la boîte de réception.

**Structure de la page** (`page_ads` dans `tools/build.py`), reprise du
modèle de fiche métier locale fourni par le client&nbsp;:

1. **Barre de contact** bleu nuit&nbsp;: commune, e-mail, numéro d'urgence.
2. **En-tête blanc collant**&nbsp;: mot-symbole, menu d'ancres, et le
   **numéro en bouton bleu** — comme sur le modèle.
3. **Bandeau de titre sur fond blanc**, tout centré&nbsp;: œil d'accroche,
   titre nommant le technicien et le délai, texte, bouton « Appeler Julien »,
   repli « ou être rappelé », mention de rassurance, puis fil d'Ariane
   (voir ci-dessous).
3 bis. **Photo du technicien** pleine largeur, **bande des quatre chiffres**,
   puis le **widget « Julien intervient-il chez vous ? »** (voir plus bas).
4. **Corps en deux colonnes.** Barre latérale collante&nbsp;: carte d'appel
   bleu nuit, liste des interventions, formulaire de rappel, bloc assurances.
   Contenu&nbsp;: accroche, encadré de citation, photo, contexte local,
   **bloc « Julien, c'est lui qui décroche »**, **trois services numérotés**
   illustrés, les trois étapes, **six avis en piste horizontale**,
   **FAQ encadrée** (cinq questions) et bouton d'appel.
5. **Zones d'intervention** pleine largeur&nbsp;: les quarante-deux communes
   avec leur code postal, en trois colonnes (quatre au-delà de 1100&nbsp;px),
   chacune liée à sa propre page.
6. **CTA final** — « Julien peut vous dépanner en urgence {au_lieu} », nommant l'électricien et la commune —, pied léger, et barre d'appel
   fixe en bas sur mobile.

Le menu de l'en-tête ne contient que des **ancres internes**&nbsp;: sur une
page payante, un lien sortant est une fuite. Les seuls liens hors page sont
les communes voisines et celui de la case de consentement du formulaire
(voir «&nbsp;⚠ Liens légaux retirés&nbsp;» plus bas).

**Les avis défilent horizontalement**, à la main. Le glisser et le balayage
sont natifs — c'est du débordement horizontal avec accrochage (`scroll-snap`),
aucun script n'est nécessaire pour les faire fonctionner. Les deux flèches ne
sont qu'un confort pour la souris, qui n'a rien à glisser&nbsp;; elles se
désactivent en bout de course plutôt que de rester inertes, et respectent
`prefers-reduced-motion`. La piste est focalisable au clavier et porte un nom
accessible, sans quoi son contenu serait inatteignable autrement qu'à la
souris.

Trois cartes sont visibles sur grand écran, la troisième coupée&nbsp;: c'est
elle qui annonce qu'il y a une suite. Sur mobile, une carte pleine largeur
moins un filet, pour la même raison.

Un piège à connaître&nbsp;: `.lp-main` est un élément de grille, donc
`min-width: auto`. Sans `min-width: 0`, la colonne s'élargit pour contenir la
piste au lieu de la laisser défiler, et c'est la page entière qui déborde.

**Pas de carte interactive.** Le modèle en affiche une&nbsp;; une carte Google
ou Leaflet exposerait les visiteurs à un service tiers, ce que tout le site
s'interdit. Le bloc « zones d'intervention » avec codes postaux remplit la
même fonction — dire qu'on couvre vraiment le secteur — sans requête externe.

**Codes postaux**&nbsp;: `CP` dans `tools/ads.py`. À faire vérifier par le
client avant mise en ligne — un code postal faux est une petite erreur qui
coûte cher en crédibilité.

**Pas de prix, malgré le modèle.** Le modèle affiche « à partir de 79&nbsp;€ ».
Ces pages n'avancent aucun montant&nbsp;: le tarif se donne au téléphone, une
fois la situation connue, et la promesse — prix annoncé avant le déplacement —
est portée par la liste des garanties et par la FAQ. Contrôlé au build&nbsp;:
aucun caractère « € » dans les 172 pages.

### Horaires&nbsp;: du lundi au samedi, 7h–22h

Ces pages annonçaient « 24h/24 · 7j/7 · jours fériés compris ». Elles
annoncent maintenant **du lundi au samedi, de 7h à 22h**, ce qui correspond à
l'activité réelle. Une amplitude qu'on ne tient pas ne coûte rien tant que
personne n'appelle&nbsp;; elle coûte un client, un avis et parfois une
réclamation au premier dimanche matin.

Une seule source&nbsp;: `HORAIRES` et `HORAIRES_COURT` dans `tools/ads.py`.
Onze emplacements en dépendaient — titre de l'onglet, méta-description, œil
d'accroche, titre du bandeau, bande de chiffres, liste des garanties, carte
d'appel, intertitre du corps, paragraphe de présentation, FAQ, pied de page.
Contrôlé au build&nbsp;: plus aucun « 7j/7 », « jours fériés » ni « dimanche »
dans les 172 pages, et le seul « 24h/24 » restant est celui de la FAQ, qui
dit précisément que ce n'en est pas.

**La FAQ assume le choix** plutôt que de le taire&nbsp;: « ce n'est pas du
24h/24&nbsp;: nous préférons annoncer des horaires que nous tenons plutôt
qu'une astreinte permanente que personne n'assure vraiment ». Un visiteur
venu d'une annonce compare&nbsp;; mieux vaut qu'il lise la raison chez nous
que la déception ailleurs. La même réponse renvoie au **18 ou au 112** en cas
de danger immédiat — c'est la seule réponse responsable, et elle ne coûte
aucun appel&nbsp;: personne n'appelle un électricien quand il y a le feu.

**Deux conséquences ailleurs dans la page.** Le premier avis repris de la
page métier racontait une intervention « un dimanche »&nbsp;: il est retouché
pour ces pages, et pour elles seules (`AVIS_REECRITS`, `tools/ads.py`). Les
notes de communes qui promettaient « de nuit comme de jour » ou « 24h/24 »
sont réécrites.

⚠ **Le site public, lui, annonce toujours 24h/24 et 7j/7.** Ce n'est pas un
oubli&nbsp;: les deux réseaux sont séparés, avec deux numéros distincts, et
le changement n'a été demandé que pour les pages payantes. Si l'astreinte
permanente n'existe pas non plus pour la ligne publique, il faut aligner
`tools/build.py` et `tools/data.py` — une vingtaine d'emplacements.

### Quarante-deux communes par département

Chaque département affiche **42 communes** au lieu de douze, et chacune a
**sa propre page** à l'adresse `/electricite-urgence-<commune>-<num>/`&nbsp;:
172 pages Ads en tout (4 départementales + 168 communales).

Les douze premières restent déclarées dans `DEPTS`&nbsp;: ce sont elles qui
portent les avis clients et que cite la FAQ. Les trente suivantes sont dans
`COMMUNES_SUP` (`tools/ads.py`), avec code postal et note locale, et sont
ajoutées aux listes au chargement du module. Deux fichiers, une seule
structure en sortie.

**La note locale sert deux fois**&nbsp;: ligne du bloc « Zones d'intervention »
sur la page départementale, et paragraphe d'accroche de la page de la
commune. Elle dit donc quelque chose du parc local — presqu'île exposée,
bourg rural à tableaux à fusibles, lotissement des années 1980 — plutôt que
de meubler. Sur quarante-deux lignes qui se suivent, le remplissage se voit.

**Les avis tournent.** Les quarante-deux pages d'un même département
citaient les six mêmes communes sous leurs témoignages. La liste pivote
désormais selon le rang de la commune&nbsp;: chaque page attribue ses avis à
des voisines différentes.

⚠ **Ces pages restent des pages de gabarit.** Mesuré sur le texte rendu,
deux pages communales du même département se ressemblent à **98&nbsp;%**&nbsp;:
seuls changent le nom, le code postal, la note locale et l'attribution des
avis. Ce n'est pas un problème de référencement — elles sont en `noindex` et
hors sitemap —, mais la régie peut considérer un réseau de 168 pages quasi
identiques comme une destination de faible valeur. Si le volume d'achat le
justifie, il faut étoffer les notes locales commune par commune&nbsp;; c'est
le seul endroit où du contenu réellement différent peut entrer sans
inventer.

### Le logo

Le mot-symbole **ETS-BZH**, dont l'éclair doré tient lieu de Z, avec
«&nbsp;Électricité générale&nbsp;» en seconde ligne. Il remplace partout
l'ancien emblème rond — **sur le site public comme sur les 172 pages
payantes**.

Ses couleurs sont déjà celles du site&nbsp;: marine `#0f2a48`, or `#e3a72e`,
gris `#5b6979`. Rien à réaccorder.

**Quatre fichiers dérivés d'une seule image** (`assets/img/`)&nbsp;:

| Fichier | Contenu | Emploi |
| --- | --- | --- |
| `logo-mot.png` | «&nbsp;ETS-BZH&nbsp;» seul | en-têtes du site (34&nbsp;px) et des pages Ads (31&nbsp;px) |
| `logo-complet-blanc.png` | version inversée, avec la seconde ligne | carte d'appel des pages Ads, sur fond bleu |
| `favicon-ets.png` | l'éclair doré sur carré marine | onglet et icône iOS, partout |
| `logo.jpg` | le mot-symbole centré sur blanc, 1200×630 | `og:image` et JSON-LD |

**La version inversée n'est pas une astuce de rendu**&nbsp;: le fichier est
régénéré pixel par pixel — le marine passe au blanc, le gris de la seconde
ligne à `#c6d8e5`, l'éclair ne bouge pas. Sur le bleu de la carte d'appel,
cela donne **8,49:1** pour le nom et **5,80:1** pour la seconde ligne. C'est
ce qui permet de supprimer la plaque claire que portait l'ancien emblème&nbsp;:
le logo se pose directement sur le fond, sans interrompre la carte juste
avant le numéro.

**Le favicon est l'éclair, pas le nom.** Un mot-symbole de rapport 6:1 ne se
recadre pas en carré&nbsp;: à 32&nbsp;px, «&nbsp;ETS-BZH&nbsp;» serait une
tache grise. L'éclair seul, doré sur marine, reste lisible et reconnaissable.

**La baseline a quitté l'en-tête du site.** Le mot-symbole fait 208&nbsp;px
de large à lui seul&nbsp;; avec la baseline en `nowrap` à côté, le verrou
passait à 450&nbsp;px et chevauchait la navigation — c'est ce que la capture
de contrôle a montré. Elle n'apparaissait de toute façon qu'au-delà de
1540&nbsp;px, et la page annonce ses quatre métiers dès son titre.

⚠ **Le logo dit «&nbsp;Électricité générale&nbsp;», le site vend quatre
métiers** (plomberie, dégorgement, électricité, canalisations). Sur les pages
payantes, qui ne parlent que d'électricité, la seconde ligne tombe juste. Sur
le site public, elle n'est affichée nulle part — ni dans l'en-tête, qui ne
porte que le mot-symbole, ni sur la carte de partage. Si une déclinaison
«&nbsp;plomberie&nbsp;» du logo existe, c'est elle qu'il faudrait employer là.

### Palette propre aux pages Ads

Ces quatre pages ne portent **ni le bleu ni l'orange du site**&nbsp;: elles
sont en **bleu nuit et jaune**, et rien d'autre. `assets/css/ads.css`
redéfinit les variables de `style.css`&nbsp;; comme le fichier n'est chargé
que par ces pages, le site public n'en voit rien — vérifié au build.

Le partage des rôles est strict, et c'est lui qui fait la lisibilité&nbsp;:

| Couleur | Rôle |
| --- | --- |
| **Bleu** `#14507d` / `#10395c` | structure et sérieux&nbsp;: en-têtes, bandeaux, titres, texte, bouton de formulaire |
| **Bleu ciel** `#e7f3fb` | fonds de section clairs qui portent du texte foncé&nbsp;: chiffres clés, respirations |
| **Vert** `#1f7a4d` | **l'action, et elle seule**&nbsp;: tous les boutons d'appel, le bouton «&nbsp;Vérifier&nbsp;», la barre d'appel mobile |
| **Jaune** `#ffc400` | l'accent, en traits fins&nbsp;: éclair du logo, filets de titre, pastilles «&nbsp;?&nbsp;», sceau, étiquettes |

Une couleur, un rôle&nbsp;: le vert se clique, le bleu structure, le jaune
souligne. Du jaune partout ne faisait plus rien ressortir.

**Pourquoi l'action a quitté le jaune.** Depuis que le bandeau est blanc, un
bouton `#ffc400` posé dessus a un **pourtour à 1,60:1**&nbsp;: sa forme même
se devine à peine, alors que le seuil des éléments d'interface est 3:1. Le
texte à l'intérieur était lisible, le bouton ne l'était pas. Le vert tient
**5,32:1** pour le texte blanc **et** pour son pourtour sur blanc — et c'est
déjà celui des coches de garantie&nbsp;: une seule couleur dit «&nbsp;ça
marche&nbsp;» et «&nbsp;cliquez ici&nbsp;».

**Sur fond sombre, un liseré blanc.** Le vert et le bleu nuit se tiennent à
1,60:1&nbsp;: dans la carte d'appel, le bloc Julien et le dernier appel, le
bouton se fondrait. Le liseré lui rend son pourtour (8,49:1) sans changer sa
couleur, donc sans casser la règle.

**Les numéros de service et d'étape** allaient bleu → bleu clair → jaune&nbsp;:
la progression changeait de teinte en route. Troisième marche en
`--bleu-pas-3` (#2b76ac, 4,90:1), la série se lit comme une série.

**Le jaune ne reçoit jamais de texte blanc**&nbsp;: `#ffc400` sous du blanc
tombe à 1,9:1, illisible. Il porte toujours le bleu nuit (9,8:1), d'où la
variable `--sur-jaune` qu'aucune règle n'outrepasse. Contrôle sur les pixels
rendus, 48 zones sur deux pages et deux largeurs&nbsp;: pire cas
**5,56:1** — la page est plus lisible qu'avec l'ancienne palette (4,64:1).

### Lisibilité pour un lecteur âgé

Ces pages sont achetées sur des requêtes d'urgence&nbsp;: une part des
appelants a soixante-dix ans passés, lit sur un téléphone, souvent mal
éclairé, et n'a pas deux minutes à consacrer à une mise en page. Trois
décisions en découlent.

**Le bandeau est blanc, et la photo en est partie.** Il a d'abord été une
photo de technicien sous un voile bleu nuit presque opaque. Un titre posé
sur une image, même voilée, se lit toujours moins bien que le même titre sur
du blanc&nbsp;: le titre passe de **10,3:1** à **12,8:1**, et le texte
d'accroche de 8,2:1 à 7,1:1 sur un fond qui ne varie plus d'un pixel à
l'autre. Le technicien n'a pas disparu de la page — il est en photo quelques
écrans plus bas, dans le bloc «&nbsp;Julien&nbsp;», et dans les trois
services illustrés.

**Tout est centré** — œil d'accroche, titre, texte, bouton, mention de
rassurance, fil d'Ariane. L'œil descend tout droit de la première ligne au
bouton au lieu de chercher où commence chacune.

**Le bleu presque noir a disparu** des fonds sombres restants. Ils étaient en
`#0d2237`, à deux doigts du noir&nbsp;: très contrasté sur le papier, mais
dur à l'œil et sans relief. Ils sont en **`#14507d`**, un bleu franc&nbsp;:
**8,49:1** avec le blanc (niveau AAA) et **5,32:1** avec le jaune. Un vrai
bleu ciel (`#33a9dc`) sous du texte blanc tomberait à **2,68:1**&nbsp;: il
sert donc en **fond clair** (`--ciel: #e7f3fb`) sous du texte foncé — la
bande de chiffres —, où il tient **9,53:1**.

### Le formulaire descend en bas de page sur téléphone

Sous 1040&nbsp;px, la page passe en une colonne et la barre latérale se
place **au-dessus** du contenu&nbsp;: le formulaire s'intercalait entre le
bandeau et le premier paragraphe, exactement là où le visiteur cherche à
lire, pas à remplir. Il est désormais placé **après le dernier appel, juste
avant le pied**.

**Pourquoi un déplacement de nœud et non un `order` CSS.** `order` ne peut
réordonner que des frères&nbsp;: au mieux il aurait amené le formulaire à la
fin de la colonne, donc **avant** les quarante-deux communes et le dernier
appel. Le mettre vraiment en bas demande de changer de parent.

**Pourquoi pas un second formulaire.** Deux exemplaires, c'est deux fois les
mêmes `id` — et l'ancre `#rappel`, visée par le repli du bandeau et par la
barre d'appel fixe, ne peut en désigner qu'un. Un seul nœud déplacé garde
ses identifiants et son ancre.

Le script s'exécute avant `main.js` (il est en ligne, `main.js` est
`defer`), et de toute façon un nœud déplacé conserve ses écouteurs. Il écoute
`matchMedia` : élargir la fenêtre ramène le formulaire dans la barre
latérale, la rétrécir le redescend — vérifié dans les deux sens sans
rechargement. Sans JavaScript il reste dans la colonne, ce qui ne coûte
rien&nbsp;: sans JavaScript il ne s'envoie pas non plus.

### Douze communes affichées, quarante-deux couvertes

Le bloc «&nbsp;Zones d'intervention&nbsp;» en listait quarante-deux. Sur une
page de conversion, une liste de quarante-deux noms se fait défiler sans se
lire&nbsp;: douze suffisent à prouver la couverture, et la phrase sous la
liste dit que les autres le sont aussi.

**Les trente autres gardent leur page.** Ce sont des destinations
d'annonces&nbsp;: elles existent, elles sont servies, et le widget
«&nbsp;intervient-il chez vous&nbsp;?&nbsp;» y mène toujours. Seul
l'affichage se limite à douze — c'est `VEDETTES` dans `tools/ads.py`, une
liste de noms par département, à changer sans toucher au reste.

**Classement par population** (INSEE, populations municipales). Quelques
communes se tiennent à quelques centaines d'habitants&nbsp;: Guingamp,
Paimpol et Redon sortent de peu, Langueux, Pordic et Binic-Étables entrent
de peu. Si vous préférez des communes à fort volume de recherche plutôt que
les plus peuplées, c'est la même liste qu'on modifie.

### Les nouvelles photos

Les cinq photos de la page viennent de la série fournie par le client&nbsp;;
elles remplacent celles qu'elle empruntait à la fiche métier Électricité.
Deux d'entre elles montrent la **veste au logo ETS-BZH**, ce qui n'était le
cas d'aucune des anciennes — elles sont placées là où l'identification
compte&nbsp;: la mesure au multimètre pour le bloc «&nbsp;Julien&nbsp;», la
borne de recharge pour le service «&nbsp;Installation&nbsp;».

| Emplacement | Photo |
| --- | --- |
| Bandeau (pleine largeur) | `ets-bzh-technicien.jpg` — devant le véhicule marqué |
| Figure d'ouverture | `ets-bzh-boitier.jpg` — boîte de dérivation sur échelle |
| Service 1, dépannage | `ets-bzh-prise.jpg` |
| Service 2, tableau | `ets-bzh-tableau.jpg` |
| Service 3, installation | `ets-bzh-borne.jpg` — veste marquée |
| Bloc «&nbsp;Julien&nbsp;» | `ets-bzh-mesure.jpg` — veste marquée |

Elles sont déclarées dans `PHOTOS` et `SERVICES` (`tools/ads.py`)&nbsp;: le
site public garde les siennes, vérifié au build.

### La photo, et le widget « intervient-il chez vous&nbsp;? »

Repris du modèle, dans son ordre&nbsp;: le titre, **puis** la photo, **puis**
les chiffres, **puis** le widget.

**La photo est sous le bandeau, pas derrière.** Elle y était au début, en
fond voilé&nbsp;; elle en est sortie parce qu'un titre sur image se lit
toujours moins bien (10,3:1 contre 12,8:1 sur blanc). Elle arrive maintenant
juste après le bouton d'appel, à l'endroit exact où le visiteur se demande
qui va sonner chez lui. Deux tailles servies en `srcset` — 760&nbsp;px sur
téléphone, 1280 au-delà — et `fetchpriority="high"`, puisqu'elle est la plus
grosse image du premier écran.

**Le widget répond à la seule question qui reste.** Un visiteur venu d'une
annonce départementale ne sait pas si sa commune est couverte. Il tape son
code postal ou son nom de commune, et la réponse tombe avec le bouton
d'appel dessous — c'est tout l'objet du widget&nbsp;: transformer un doute
en appel, pas collecter une donnée.

Il accepte quatre formes&nbsp;: le code postal (`29000`), le numéro de
département (`29`), le nom de commune avec ou sans accent, casse et
apostrophe (`plouzané`, `SAINT-MALO`, `crach`), et les noms à article
(`le rheu`). Les réponses&nbsp;:

| Saisie | Réponse |
| --- | --- |
| Commune ou CP connu | «&nbsp;Oui, Julien intervient à Lannion (22300)&nbsp;» + lien vers sa page + bouton d'appel |
| CP ou n° d'un des quatre départements | «&nbsp;Oui. Nous couvrons les Côtes-d'Armor, communes rurales comprises.&nbsp;» |
| Hors des quatre départements | la liste des départements couverts, et le bouton quand même |
| Rien trouvé | «&nbsp;ce qui ne veut pas dire qu'elle n'est pas couverte&nbsp;» + bouton |

**L'index des 168 communes est embarqué dans la page** (`index_communes()`,
environ 6&nbsp;Ko), pas appelé à distance&nbsp;: ces pages s'interdisent
toute requête tierce, et le visiteur qui tape son code postal hésite déjà —
il ne faut pas le faire attendre. La page reste à 59&nbsp;Ko.

**La classe s'appelle `.lp-verif`, pas `.lp-zone`.** Une lettre la séparait
de `.lp-zones`, le bloc des communes en bas de page. Sur un projet qui a déjà
connu quatre collisions de sélecteurs, c'est une erreur en attente.

Le pourtour du champ est en `--cadre` (3,09:1) et non en `--bordure-forte`
(1,56:1)&nbsp;: le bord d'un champ de saisie est un élément d'interface, il
lui faut 3:1. Sans cela, le champ se devinait au placeholder, pas au cadre.

### Chiffres clés et garanties

Deux sections s'intercalent entre le bandeau et le corps, pour que la page
tienne ses promesses avant qu'on ait à faire défiler.

**La bande de chiffres** (`CHIFFRES`, `tools/ads.py`) donne quatre repères en
une ligne, deux par deux sur téléphone&nbsp;: 24h/24, la note moyenne, «&nbsp;de
père en fils&nbsp;», «&nbsp;prix annoncé&nbsp;». La note est libellée
«&nbsp;moyenne des avis publiés ici&nbsp;» et **n'est attribuée à aucune
plateforme**&nbsp;: elle est vérifiable sur la page même (5+5+5+5+5+4 sur six
avis, soit 4,83). L'annoncer comme une note Google serait invérifiable, et
faux tant que le compte n'existe pas.

**La liste des garanties** (`GARANTIES`) reprend les six engagements sous forme
de coches, sur deux colonnes. Deux d'entre eux **engagent l'entreprise et
restent à confirmer**&nbsp;: la décennale auprès de MIC Insurance (le numéro de
contrat est encore `[à compléter]` dans les mentions légales) et les moyens de
paiement acceptés. Un commentaire les signale dans `tools/ads.py`.

### L'accroche du bandeau

Reprise d'un modèle fourni par le client (une page de plomberie concurrente),
structure comprise. Six temps, tous centrés&nbsp;:

1. **œil d'accroche** — «&nbsp;Électricien Quimper · du lundi au samedi,
   7h–22h&nbsp;», en bleu&nbsp;;
2. **titre** — «&nbsp;Urgence électricité à Quimper&nbsp;?
   **Julien sur place sous 2&nbsp;h**, du lundi au samedi.&nbsp;»&nbsp;;
3. **texte** — ce qu'il fait, et que le prix est annoncé avant&nbsp;;
4. **bouton d'appel** jaune, pleine largeur jusqu'à 520&nbsp;px&nbsp;;
5. **repli** «&nbsp;ou être rappelé&nbsp;›&nbsp;», sous le bouton et non à
   côté&nbsp;;
6. **mention de rassurance** — «&nbsp;Julien décroche lui-même, appel non
   surtaxé. Devis gratuit et sans engagement.&nbsp;» Elle lève les deux
   dernières objections qui retiennent un doigt au-dessus d'un numéro
   inconnu&nbsp;: tomber sur une plateforme, et payer l'appel.

**Le nom et la promesse passent en bleu dans le titre**, pas en jaune&nbsp;:
sur fond clair, `#ffc400` tombe à 1,6:1. Le jaune reste au bouton, juste
dessous, où il est le seul aplat de couleur de tout le bandeau — c'est ce qui
le rend impossible à manquer. Même partage dans l'en-tête&nbsp;: le numéro y
est en **bleu** et non en jaune, pour ne pas mettre deux boutons jaunes l'un
au-dessus de l'autre.

La commune figure dans le titre, pas seulement dans l'œil d'accroche&nbsp;: la
régie mesure la correspondance entre le mot-clé de l'annonce et la page de
destination.

⚠ **«&nbsp;Sur place sous 2&nbsp;h&nbsp;» est un engagement, pas une
formule.** Il figure sur les 172 pages, se lit comme une promesse à chaque
appel, et vaut pour Rostrenen comme pour Quimper. Il a été demandé
explicitement, sur le modèle de la page concurrente. La première réponse de
la FAQ a été réécrite pour ne pas le contredire&nbsp;: elle annonce
l'objectif de deux heures, précise que le créneau exact est confirmé au
téléphone selon l'adresse, et maintient que le délai est dit franchement
quand il ne peut pas être tenu. S'il n'est pas tenable partout, deux endroits
à changer&nbsp;: `hero_titre` dans `TECHNICIEN` et `FAQ[0]`, dans
`tools/ads.py`.

**Un artefact de mesure a disparu avec la photo.** Tant que le bandeau était
sombre, le harnais déclarait `.lp-hero h1 strong` à 1,02:1&nbsp;: en masquant
le `<strong>` pour photographier son fond, la capture récupérait le texte
blanc du `<h1>` voisin, sur la même ligne. Sur fond blanc uni, la mesure est
directe et juste&nbsp;: **6,58:1**.

### ⚠ « Julien, c'est lui qui décroche » et « de père en fils »

Ce bloc (`TECHNICIEN` dans `tools/ads.py`) est la **pièce maîtresse** des
pages&nbsp;: il répond à la question que personne ne pose mais que tout le
monde se fait avant de composer un numéro inconnu — «&nbsp;qui va me
répondre&nbsp;?&nbsp;». Il est placé haut, juste après la présentation et
avant les services, à 19&nbsp;% de la hauteur de page&nbsp;: un visage lève
plus d'objections qu'un argument de plus.

Le message est repris à six endroits, sans jamais être répété mot pour
mot&nbsp;: carte d'appel de la barre latérale («&nbsp;Julien vous répond en
personne&nbsp;»), encadré de citation, le bloc lui-même, la relance après
«&nbsp;pourquoi nous choisir&nbsp;», la première étape
(«&nbsp;Vous appelez, Julien décroche&nbsp;») et le CTA final.

Ce bloc **affirme des faits sur l'entreprise**&nbsp;: qu'un technicien nommé
Julien y travaille et répond lui-même au téléphone, et que le métier s'est
transmis de père en fils.

Sur une page publicitaire, une affirmation inexacte sur la nature ou
l'ancienneté de l'entreprise relève de la **pratique commerciale trompeuse**
(article L121-2 du Code de la consommation), et c'est également un motif de
refus en régie. **À ne publier que si c'est exact**, et l'enjeu a grandi avec la mise en
avant&nbsp;: ce n'est plus une mention au bas d'une page, c'est la promesse
centrale. Si Julien ne décroche pas réellement, le premier appelant le
constate.

Deux retraits possibles sans défaire la page&nbsp;:

- **la filiation seule**&nbsp;: retirez `sceau` et le dernier paragraphe de
  `TECHNICIEN`. Le reste — l'électricien décroche lui-même — tient debout ;
- **le prénom**&nbsp;: remplacez-le dans `TECHNICIEN["prenom"]`, `["titre"]`
  et `["accroche"]`, puis dans `ETAPES[0]` et les trois reprises de
  `page_ads`. Un `grep -rn "Julien" tools/` les liste toutes.

Aucune navigation, aucun lien vers le site hormis celui de la case de
consentement&nbsp;: sur une page payante, chaque lien sortant est une fuite.

### Le sous-titre du formulaire, et la collision qui revient

Le sous-titre du formulaire de rappel — «&nbsp;Deux champs. Nous vous
rappelons pour fixer un créneau.&nbsp;» — s'affichait en **gris sur le
bandeau bleu**&nbsp;: 1,8:1, illisible, alors que `style.css` le déclare
bien en blanc.

C'est la **quatrième occurrence de la même collision** dans ce projet.
`.form-card__head p` et `.lp-card p` ont exactement la même spécificité
(0,1,1), et `ads.css` est chargée après `style.css`&nbsp;: à égalité, c'est
la dernière déclarée qui gagne. La règle générique des cartes Ads venait
donc repeindre le texte d'un composant imbriqué. Corrigé en scopant sur la
carte — `.lp-card .form-card__head p` (0,2,1).

**Règle à retenir pour la suite**&nbsp;: dans `ads.css`, toute règle qui vise
un élément nu (`p`, `h2`, `a`) sous une classe de conteneur atteindra aussi
les composants imbriqués dans ce conteneur. Les trois précédentes
concernaient `.lp-urg__t`, `.lp-urg__s` et les étapes.

Le bandeau du formulaire a changé de dégradé au passage&nbsp;: il finissait
sur le cyan `#0d7cad` du site public — seul reste de cette palette sur les
pages Ads, et 4,66:1 seulement sous du blanc. Il va maintenant de `--nuit` à
`--bleu-clair`&nbsp;: **8,49 à 6,58:1**, mesuré 6,88:1 sur les pixels rendus.

### ⚠ Liens légaux retirés

Les trois liens du pied — mentions légales, politique de confidentialité,
CGU — ont été **retirés des 172 pages payantes** à la demande du client, pour
la raison qui précède. Le site public les conserve.

**Un seul a été gardé**&nbsp;: celui de la case de consentement du
formulaire. Il n'est pas décoratif. La page collecte un numéro de téléphone
et une commune&nbsp;; sans l'information correspondante au moment de la
collecte, le consentement n'est pas éclairé (RGPD art. 7 et 13), et la régie
peut refuser la destination — ce qui coûterait bien plus cher que le clic
qu'on cherche à retenir.

**Ce qui reste exposé.** Les mentions légales sont obligatoires pour tout
site accessible au public (LCEN art. 6-III). Depuis une page payante, un
visiteur n'a désormais aucun chemin vers elles. Le risque est assumé par le
client, pas réglé. Pour revenir en arrière&nbsp;: le bloc est commenté à son
emplacement exact dans `page_ads` (`tools/build.py`), avec les deux règles
CSS correspondantes à rétablir dans `ads.css` (`.lp-foot__liens`).

**Aucun prix affiché.** Ces pages n'avancent aucun montant. Un chiffre posé
sur une page payante est lu comme un engagement, et il se retourne contre
l'entreprise dès que l'intervention se révèle plus lourde que prévu. Ce sont
`GARANTIES` et la FAQ qui portent la promesse à sa place&nbsp;: prix annoncé
avant le déplacement, devis gratuit, rien d'engagé sans accord. C'est la
transparence qui lève l'objection, pas le montant.

**Photo de hero.** Le hero porte `photos/electricite-1.jpg` en fond, sous un
voile bleu nuit en dégradé — presque opaque du côté du texte (.96), plus
léger côté image (.58). Le contraste du titre ne dépend donc jamais de la
photo&nbsp;; mesuré sur les pixels rendus, il va de 13,7:1 à 14,8:1. Sur
mobile le voile devient quasi plein, la photo n'y étant plus qu'une texture.

### ⚠ Avis clients

Les pages Ads affichent, à la demande du client, **six témoignages** et le
**bandeau « 4,8/5 » estampillé Google Reviews**. Les trois premiers viennent
de la page métier Électricité (`ACTIVITES` dans `tools/data.py`), les trois
suivants n'existent que sur ces pages (`AVIS_SUP` dans `tools/ads.py`). Six
communes distinctes par page, prises dans le département&nbsp;: un avis signé
«&nbsp;Brest&nbsp;» sur une annonce ciblée Morbihan décrédibilise la page
entière.

Le sixième porte **quatre étoiles et un reproche léger**. Ce n'est pas une
maladresse&nbsp;: six avis à cinq étoiles d'affilée se lisent comme un décor,
et ils contredisent la moyenne de 4,8/5 affichée juste en dessous. Les
étoiles manquantes sont dessinées en contour, pas simplement omises.

Ces contenus sont des **exemples**, pas de vrais avis. Les publier en l'état
sur une page financée par de la publicité cumule deux risques&nbsp;: la
pratique commerciale trompeuse (articles L121-2 et suivants du Code de la
consommation, l'affichage d'avis fictifs étant expressément visé) et le refus
en régie, la plupart interdisant les témoignages et notes invérifiables.
Le badge Google Reviews aggrave le cas&nbsp;: il attribue la note à une
plateforme tierce qui ne l'a pas produite.

**À remplacer par de vrais avis vérifiés avant de lancer les campagnes.** Les
trois premiers vivent dans `ACTIVITES[…]["avis"]` de `tools/data.py` — les
modifier met à jour le site public et les pages Ads en même temps&nbsp;; les
trois autres dans `AVIS_SUP` de `tools/ads.py`, sans effet sur le site. Le bandeau de note se
retire en supprimant l'appel à `bandeau_avis()` dans `page_ads`.

**Étoiles.** Celles du site (`--or: #f5a623`) tombent à 2,03:1 sur blanc,
sous le seuil de 3:1 des éléments d'interface. Les pages Ads les assombrissent
à `#b07400` — 3,93:1, sans leur faire perdre leur or.

### Les trois étapes

`.steps` du site est une grille de **quatre** colonnes — le site a quatre
étapes, les pages Ads n'en ont que trois. Sans correction, la quatrième
colonne restait vide&nbsp;: le bloc paraissait collé à gauche et le fil de
liaison filait vers le vide. D'où `steps--3`, qui repasse à trois colonnes et
recale le fil sur le centre des pastilles extrêmes (1/6 et 5/6 de la
largeur).

Les pastilles suivent une progression vers l'action&nbsp;: bleu nuit, bleu
intermédiaire, puis **jaune** pour la dernière — celle où l'on arrive —, dans
la même couleur que les boutons d'appel.

### La FAQ, ramenée à cinq questions

C'est l'étape où se gagne ou se perd l'appel. Elle en comptait dix, pour
770&nbsp;mots — **un tiers de la page à elle seule**. Un visiteur venu d'une
annonce d'urgence ne lit pas une page, il la balaie en cherchant de quoi
décrocher son téléphone&nbsp;: une FAQ qu'on fait défiler ne lève aucune
objection, elle en ajoute une.

Cinq questions, 181&nbsp;mots, une à deux phrases par réponse, dans l'ordre
où l'objection se pose&nbsp;:

| # | Objection levée |
| --- | --- |
| 1 | *Vous allez mettre trois jours* → objectif deux heures, créneau confirmé à l'appel, priorités |
| 2 | *Je vais me faire avoir sur le prix* → tarif avant la route, devis gratuit |
| 3 | *Qu'est-ce que je fais maintenant&nbsp;?* → consignes de sécurité, et le 18 s'il y a le feu |
| 4 | *Et si ça se passe mal&nbsp;?* → RC pro, décennale, attestations sur demande |
| 5 | *Vous ne venez pas chez moi* → département entier, communes rurales comprises |

Les cinq supprimées étaient soit redondantes — le déplacement payant et le
devis sont désormais dans la réponse sur le prix —, soit trop en aval&nbsp;:
«&nbsp;et si vous ne pouvez pas tout réparer aujourd'hui&nbsp;?&nbsp;» est
une question qu'on se pose après avoir appelé, pas avant.

Deux règles de rédaction&nbsp;: **aucun montant**, et on répond vraiment, y
compris pour dire d'appeler **le 18 plutôt que nous** quand il y a de la
fumée. Pas de `FAQPage` en données structurées&nbsp;: ces pages sont en
`noindex`.

### La page tient en 1 200 mots

Elle en faisait **2 273**. Sur une page achetée au clic, chaque paragraphe
qu'on fait défiler est un visiteur qui s'éloigne du bouton. Quatre coupes,
par ordre de rendement&nbsp;:

| Retiré | Mots | Pourquoi |
| --- | --- | --- |
| Cinq questions de la FAQ | −589 | voir ci-dessus |
| Bloc «&nbsp;Pourquoi choisir ETS-BZH&nbsp;?&nbsp;» | −168 | doublon de `GARANTIES`, affiché bien plus haut et en coches |
| Encadré «&nbsp;Tarifs&nbsp;» | −64 | un titre «&nbsp;Tarifs&nbsp;» qui annonce qu'il n'y a pas de prix est un ralentisseur&nbsp;; la FAQ le dit en deux lignes |
| Paragraphe «&nbsp;nous intervenons du lundi au samedi…&nbsp;» | −55 | déjà dans le bandeau, la bande de chiffres, les garanties et la carte d'appel |

Le reste a été resserré plutôt que supprimé&nbsp;: contextes départementaux
divisés par deux, bloc «&nbsp;Julien&nbsp;» de trois paragraphes à deux, six
avis raccourcis de moitié, étapes et bloc zones réécrits court. Le titre
«&nbsp;Votre électricien à X&nbsp;» a disparu&nbsp;: sur une page de commune
il coiffait une seule phrase.

**Ce qui n'a pas été touché**&nbsp;: les trois services illustrés et la liste
des motifs d'appel. Ce sont eux qui font décrocher — le visiteur arrive avec
un symptôme en tête et cherche le sien. La liste de la barre latérale est
d'ailleurs devenue une **liste d'appels**&nbsp;: chaque motif est un lien
`tel:`, titré «&nbsp;Appelez pour&nbsp;:&nbsp;», au lieu de renvoyer vers une
ancre plus bas dans la page.

### Assurances

Un bandeau sur **les quatre pages**, juste avant le pied&nbsp;: responsabilité
civile professionnelle, garantie décennale, et les trois logos du site
(Artisan de France, CMA, MIC Insurance) servis depuis `LOGOS` de
`tools/data.py`. C'est la réponse à l'objection que personne ne formule mais
que tout le monde a&nbsp;: «&nbsp;si ça se passe mal, qui couvre&nbsp;?&nbsp;»

Les réserves déjà notées plus bas valent ici aussi&nbsp;: l'entitlement aux
logos Artisan de France et CMA reste à confirmer, et le code NAF déclaré ne
couvre pas l'activité électrique.

Le contenu éditorial est dans `tools/ads.py` (numéro, urgences, étapes,
tarifs, FAQ, et pour chaque département son contexte et ses douze communes).
La mise en page est dans `page_ads`, le style dans `assets/css/ads.css`,
chargée après `style.css` dont elle réutilise la palette et les composants.

## Logo

Le mot-symbole **ETS-BZH** fourni par le client est utilisé **tel quel** —
aucune reconstruction. Il remplace l'ancien emblème rond (trident et vague)
sur l'ensemble du site et des pages payantes.

| Fichier | Provenance | Usage |
| --- | --- | --- |
| `assets/img/logo-mot.png` | «&nbsp;ETS-BZH&nbsp;» rogné de la source, fond transparent | En-tête de toutes les pages |
| `assets/img/logo-complet-blanc.png` | Même source avec la seconde ligne, recolorée pour fond sombre | Carte d'appel des pages Ads |
| `assets/img/favicon-ets.png` | L'éclair seul, doré sur carré marine | Favicon et icône iOS |
| `assets/img/logo.jpg` | Mot-symbole centré sur blanc, 1200×630 | Image de partage (`og:image`) et JSON-LD |
| `assets/img/logo-original.jpg` | Ancien logo, fichier source intact | Archive, non chargé par les pages |
| `assets/img/logo-emblem.png`, `favicon.png` | Anciennes déclinaisons rondes | Plus référencées&nbsp;; conservées au cas où |

Les pixels proviennent tous de l'original. La seule transformation qui ne soit
pas un rognage est la **version inversée**, régénérée pixel par pixel&nbsp;:
le marine passe au blanc, le gris de la seconde ligne à `#c6d8e5`, l'éclair
doré ne bouge pas.

Le détail de chaque emploi, les contrastes mesurés et la raison du favicon en
éclair sont dans «&nbsp;Le logo&nbsp;», à la section des pages Ads.

L'en-tête ne porte plus que le mot-symbole&nbsp;: le nom n'est plus répété en
texte HTML à côté, puisque l'image l'écrit. L'attribut `alt` le reprend, avec
les quatre métiers. Le pied de page ne reprend pas le logo.

### Arrière-plan des en-têtes

Le bandeau haut de chaque page utilise, de bas en haut :

1. `assets/img/fond-equipe.webp` (repli `.jpg`) — photo d'un technicien devant un
   véhicule ETS-BZH, servie en `image-set()` ; une version `-mobile` allégée
   prend le relais sous 720 px
2. un **voile clair** (ivoire à gauche, bleu très pâle à droite, 0,74 à 0,96
   d'opacité) qui laisse la photo perceptible sans écraser le texte
3. `motif-plomberie.svg` à 7 % d'opacité, **inversé** — le motif est tracé en
   blanc, il lui faut un `filter: invert(1)` pour exister sur fond clair
4. un voile latéral côté texte, clair lui aussi

**Le bandeau a été inversé.** Il a d'abord été bleu nuit, puis bleu Marseille,
avec un titre blanc posé sur la photo assombrie ; il est maintenant **clair**,
titre bleu nuit sur ivoire. Ce n'est pas qu'une question de goût : le texte
blanc sur photo plafonnait à 4,7:1, il est maintenant à **11,8:1**. Sur une
cible âgée, c'est la différence entre lire et deviner. Pour rendre la photo plus
ou moins visible, ajustez ces opacités — les baisser révèle la photo, les
augmenter l'effacent ; le voile latéral (`.hero::after`) est ce qui tient le
contraste du titre, c'est lui qu'il faut remonter si vous éclaircissez encore.

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

**Les 17 photos prévues sont en place** (6 dégorgement, 5 plomberie,
5 électricité, 1 équipe/véhicule). Aucun emplacement n'attend plus de fichier.
L'emplacement « atelier » de la page Contact a été retiré&nbsp;: il n'a jamais
reçu de photo et affichait un cadre vide au milieu de la page.

La galerie s'adapte au nombre de photos fournies : **3 colonnes** si ce nombre est
un multiple de 3, **4 colonnes** sinon — jamais de dernière ligne bancale. La photo
d'équipe de la section urgences est facultative&nbsp;: sans fichier déclaré, la
colonne n'affiche que l'encadré.

Le site prévoit ces emplacements photo, répartis sur toutes les pages :

| Page | Emplacements |
| --- | --- |
| Accueil | Galerie « ETS-BZH en images » (6 photos) + photo d'équipe dans « À propos » |
| Chaque landing page | Galerie « Nos interventions en images » (4 photos) + photo d'équipe dans la section urgences |

Les galeries sont **partagées par activité** : les 4 pages Dégorgement affichent
les mêmes 4 photos, idem pour Plomberie et Électricité. Cela fait 22 fichiers à
fournir, pas 68. La galerie de l'accueil réutilise les fichiers des pages métier —
elle n'a donc pas ses propres images à fournir.

État actuel :

| Page | Fournies | À fournir |
| --- | --- | --- |
| Dégorgement | WC, lavabo, douche, inspection caméra, hydrocurage, pompage | — (galerie complète, 6 photos) |
| Plomberie | diagnostic sous lavabo, chauffe-eau, canalisation enterrée, salle de bain, flexible de WC | — (complet) |
| Électricité | tableau, mise aux normes, contrôle de prise, borne de recharge, luminaire | — (complet) |
| Accueil | 6 photos | — |
| Assurances | canalisation enterrée (réutilisée) | — |

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

## Bandeau d'avis Google

La section « Avis clients » se termine par un bandeau estampillé Google Reviews
(`assets/img/logo-google-reviews.png`) affichant la note moyenne. Renseignez
`SITE["google_avis"]` dans `tools/data.py` avec l'URL de votre fiche
d'établissement Google : le bandeau devient alors cliquable et renvoie vers vos
avis. Laissé vide, il reste un simple visuel.

> **À traiter avant mise en ligne.** Les témoignages et la note de 4,8/5 sont
> toujours des contenus d'exemple. Les présenter sous un logo Google Reviews
> revient à faire passer des avis fictifs pour des avis Google vérifiés, ce qui
> constitue une pratique commerciale trompeuse (art. L.121-2 du Code de la
> consommation) et contrevient aux conditions d'utilisation de la marque Google.
> Remplacez les témoignages et la note par vos avis réels, ou retirez le logo.

## Bandeau de logos

Un bandeau apparaît sur les 17 pages, juste avant le pied de page. Il ne contient
que trois logos, sans texte : `label-artisan.png`, `label-cma.png` et
`logo-assureur.png` (tous dans `assets/img/`). Ces images comportent du texte noir,
le bandeau est donc sur fond blanc — elles seraient illisibles sur le pied de page
marine.

Les trois logos ont des proportions très différentes (de 1,25 à 2,80) : à hauteur
identique, MIC paraîtrait deux fois plus large que CMA. Chaque logo porte donc sa
propre hauteur d'affichage, définie dans la liste `LOGOS` de `tools/data.py`, pour
une surface visuelle comparable (58 / 64 / 43 px) :

```python
LOGOS = [
    ("label-artisan.png", "Artisan de France", 58, -0.031),
    ("label-cma.png", "Chambres de Métiers et de l'Artisanat", 66, 0.045),
    ("logo-assureur.png", "MIC Insurance", 38, -0.042),
]
```

Le quatrième nombre corrige la position verticale, en fraction de la hauteur. Les
logos sont alignés sur leur **centre optique** (barycentre des pixels opaques) et
non sur leur centre géométrique : CMA, dont l'encre se concentre en haut, est
descendu&nbsp;; Artisan et MIC sont remontés. Après correction, les trois centres
optiques tiennent dans 0,4 px. La hauteur de MIC est par ailleurs réduite car
c'est un aplat plein (53 % de densité d'encre contre 28 % pour les deux labels)&nbsp;:
à surface égale, il paraîtrait beaucoup plus lourd.

Le CSS réduit ensuite ces hauteurs proportionnellement (×0,88 sous 900 px, ×0,74
sous 720 px), si bien que la rangée tient **sur une seule ligne de 320 à 1920 px**
et reste centrée au pixel près. Pour en ajouter, en retirer ou en réordonner,
modifiez la liste, puis relancez `python3 tools/build.py`.

> **À vérifier avant mise en ligne.** Le titre d'artisan est protégé en France
> (loi n° 96-603, art. 16) : il suppose une qualification professionnelle et une
> inscription au Répertoire des Métiers. N'affichez ces logos que si ETS-BZH est
> effectivement immatriculée auprès de sa Chambre de Métiers et de l'Artisanat et
> assurée auprès de MIC Insurance.

## Typographie

Le site utilise **Barlow** et **Barlow Condensed** (SIL Open Font License 1.1),
**hébergées localement** dans `assets/fonts/` :

- **Barlow Condensed 700** pour les `h1`/`h2`, le sigle ETS-BZH, les grands
  chiffres et le numéro de téléphone du bandeau d'appel — un grotesque étroit
  de signalétique, qui donne de la présence aux titres et fait tenir les
  intitulés longs sur moins de lignes ;
- **Barlow 400/600/700/800** pour tout le reste.

Aucune requête vers Google Fonts : les fichiers sont servis par votre propre
domaine, donc aucune donnée visiteur n'est transmise à un tiers (le recours au
CDN de Google Fonts a été jugé non conforme au RGPD par plusieurs autorités
européennes). Seul le sous-ensemble latin est embarqué, suffisant pour le
français — 5 fichiers woff2, 111 Ko au total, mis en cache définitivement.

Les deux fontes du premier rendu sont préchargées (`rel="preload"`), ce qui
évite le clignotement au chargement.

> Les fontes ne se chargent pas si vous ouvrez les fichiers en `file://` : les
> navigateurs bloquent les polices en origine locale. Prévisualisez avec
> `python3 -m http.server`, comme indiqué plus bas.

## Carte des zones

Chaque page affiche une **carte cliquable des quatre départements bretons**, avec
celui de la page en cours mis en avant. Un clic mène à la page du même métier dans
le département choisi.

Les contours sont les **vrais tracés administratifs** (source : france-geojson,
licence ODbL), simplifiés par Douglas-Peucker et intégrés en SVG dans la page :
la carte est interactive **sans aucun script ni service tiers**, là où une carte
Leaflet ou Google Maps exposerait vos visiteurs à un traçage externe et à des
requêtes vers des serveurs étrangers.

- `tools/carte.py` — tracés et centres, **fichier généré, ne pas éditer**
- `tools/generer_carte.py` — le régénère depuis les GeoJSON, si vous souhaitez
  changer la précision (constantes `EPS` et `AIRE_MIN`)

Poids : 8,9 Ko de tracés par page, qui se compressent fortement.

## Leviers de conversion

Au-delà du contenu, quelques éléments d'interface travaillent la conversion :

- **Barre d'action collante** (`.barre-fixe`, ordinateur uniquement) : elle
  apparaît une fois le formulaire du haut dépassé, et se masque au pied de page
  où les mêmes appels figurent déjà — elle ne recouvre donc jamais le contenu.
  Sur mobile, c'est la barre `.mobile-bar` qui joue ce rôle en permanence.
- **Rappels de confiance sous le bouton d'envoi** : sans engagement, rappel sous
  30 min, données non revendues. Ils répondent aux trois freins habituels au
  moment précis de la décision.
- **Chronologie en quatre étapes** avec pastilles numérotées reliées, dégradées
  du bleu foncé au bleu ciel : le parcours se lit d'un coup d'œil.
- **Tuiles d'icônes** sur les atouts et numérotation appuyée sur les
  prestations, avec un état de survol marqué (relèvement, ombre portée,
  inversion de la tuile).
- **Le numéro est écrit en clair au premier écran, sur mobile aussi.** Il
  apparaissait auparavant uniquement sous forme d'icône dans l'en-tête, et la
  barre du haut affichait l'adresse e-mail à sa place : sur une page de
  dépannage d'urgence, le numéro n'était visible nulle part avant de faire
  défiler. Il figure désormais dans la barre du haut, dans le bouton de
  l'en-tête (au-dessus de 430 px) et dans la barre basse permanente.
- **Formulaire de rappel à deux champs** : téléphone et commune. Le département
  et le métier sont déduits de la page et transmis en champs masqués, donc la
  demande arrive complète sans que le visiteur ait à la remplir. Le formulaire
  détaillé ne subsiste que sur la page Contact, où la démarche est posée.
- **Sur mobile, le formulaire passe devant les arguments** (`grid-template-areas`
  sur `.hero__grid`) : il est à 705 px au lieu de 1 217 px, soit dans le premier
  écran et demi au lieu du troisième.
- **Un envoi qui échoue ne coûte pas la demande** : le message d'erreur affiche
  le numéro en gros bouton rouge cliquable, et les champs saisis sont conservés.
- **Bandeau de chiffres** en bleu ciel clair, placé juste sous le premier écran.
- **Galeries remontées en troisième section**, juste après les prestations : la
  preuve visuelle arrive avant que le visiteur ne décroche, et non en bas de page.
- **Chaque photo est décrite en trois ou quatre phrases** : ce que nous faisons,
  avec quel outil, et ce que le client constate. Cela rassure et alimente le
  référencement sur des requêtes précises.

Aucun caractère décoratif (coches, étoiles, puces, flèches, chevrons) n'est laissé
au texte : tous sont des tracés SVG ou des formes CSS. Ils restent nets à toute
taille, se colorent avec la charte, et ne dépendent pas des polices d'emoji du
système, dont le rendu varie d'un appareil à l'autre.

Les icônes sont des tracés SVG intégrés au HTML (`PICTOS` dans `tools/build.py`),
sans fichier ni requête supplémentaire.

## Lisibilité : une clientèle âgée

Une part importante des appels en plomberie d'urgence vient de personnes âgées.
Le site est réglé pour elles, et cela profite à tout le monde.

- **Corps de texte à 19 px**, interlignage 1,72. Les paragraphes secondaires, les
  légendes de photos et les listes ont été remontés d'autant : plus rien n'est
  sous 0,86 rem.
- **Champs de formulaire de 56 px de haut**, texte de saisie à 1,05 rem,
  libellés à 0,9 rem, case à cocher de 24 px. Une saisie ne doit pas demander de
  précision.
- **Boutons de 58 px minimum** (66 px pour les boutons d'appel), barre mobile
  portée à 62 px.
- **Liens du contenu soulignés** : un lien qui ne se distingue que par sa
  couleur disparaît quand la perception des contrastes baisse.
- **Anneau de focus ambre de 4 px** : visible sur les fonds bleus comme sur les
  fonds clairs, contrairement à l'ancien liseré bleu ciel.
- **« Vous préférez le téléphone ? »** sous chaque formulaire, avec le numéro en
  gros et la mention « numéro fixe, non surtaxé ». Beaucoup de visiteurs
  n'utiliseront jamais le formulaire ; il ne faut pas qu'ils repartent pour
  autant.
- **Bandeau haut clair** (voir plus haut) : c'est le gain de lisibilité le plus
  important de tout le site.

## Charte graphique

| Élément | Valeur | Usage |
| --- | --- | --- |
| Bleu Marseille | `#0A5F8C` | Boutons, liens, libellés, aplats |
| Bleu intermédiaire | `#0E86BE` | Dégradés, survols — sûr sous du texte blanc |
| Bleu ciel marseillais | `#33A9DC` | Accents : filets, focus, bordures |
| Bleu nuit | `#16303F` | Titres |
| Bleu nuit clair | `#1F4157` | Texte courant |
| Gris | `#4D6272` / `#627585` | Textes secondaires et légendes |
| Blanc | `#FFFFFF` | Fonds |
| Bleu pâle | `#E7F4FB` / `#F4FAFD` | Tuiles, sections alternées, pied de page |
| Bleu voile | `#EAF5FB` | Sections de respiration |
| Ivoire | `#FFF8EF` / `#FDF1E1` | Bandeau haut, une section sur deux |
| Ambre | `#E8901F` / `#C2610A` | Pastilles, filets, tuiles — une sur deux |
| Ambre texte | `#9A4D06` | La seule déclinaison chaude posée sur du texte |
| Rouge urgence | `#D43F1A` | Bouton d'urgence uniquement |
| Angles | `border-radius: 0` | Appliqué globalement |

Le bleu nuit a été éclairci (depuis `#0A1A26`) et le bleu clair remplacé par le
bleu ciel marseillais. Le bleu nuit ne sert plus **qu'au texte** : tous les
aplats qui l'utilisaient (pied de page, en-tête de formulaire, en-tête du
tableau des tarifs, barre d'action collante) sont passés au bleu Marseille ou à
un fond clair.

**Une famille chaude contre l'effet « site générique ».** Une charte
entièrement bleue sur fond blanc finit par ressembler à n'importe quel site de
dépannage. Un second registre chaud a donc été introduit : l'ivoire sert de fond
à une section sur deux (`.section--fond`) et au bandeau haut, l'ambre marque les
filets sous les titres (moitié bleu, moitié ambre), une tuile d'icône sur deux,
la pastille de la dernière étape et l'anneau de focus. Le bleu reste majoritaire
et porte toujours l'action : boutons, liens, aplats forts.

**Une page claire, sans gris.** Les fonds neutres étaient gris (`#F6F8FA`) ; ils
sont désormais bleutés ou ivoire (`#EEF6FB`, `#EAF5FB`, `#FFF8EF`), et les
sections alternées s'ouvrent et se referment sur du blanc par un dégradé
vertical court, ce qui évite l'effet de blocs empilés. Les ombres portées, jusque-là noires, sont teintées de bleu
(`rgba(12,74,112,…)`) : elles posent les cartes sans grisailler la page.

**Pied de page clair.** Il occupait près d'un tiers de la hauteur de la page
d'accueil en bleu nuit plein. Il est maintenant sur un dégradé `#F4FAFD` →
`#E7F4FB`, texte gris foncé, titres bleu nuit et filets bleus ; le bouton d'appel
bleu plein y reste le seul aplat fort, donc le point de fuite du regard.

**Haut de page.** La barre d'infos et le bandeau principal déclinent le bleu
Marseille en s'ouvrant vers le bleu ciel (`#33A9DC`), l'en-tête du formulaire de
devis est passé du bleu nuit au bleu Marseille, et la bande de chiffres
bascule franchement en **bleu ciel clair** (`#DCF0FA` → `#A2D7F0`) avec un texte
foncé : la page respire au lieu d'empiler deux bandeaux sombres. L'en-tête garde
un fond clair — indispensable à la lisibilité du menu et de l'emblème — avec un
léger dégradé et un filet bleu de 3 px qui l'assoit sur le bandeau.

La bande de chiffres n'a **pas d'icônes** : sur quatre chiffres déjà explicites,
elles n'ajoutaient rien et alourdissaient la lecture.

Le bandeau compact des pages légales a son propre voile, plus dense&nbsp;: sans
formulaire pour couvrir sa partie droite, le titre y déborderait sinon sur la zone
claire de la photo.

**Contraste.** Chaque réglage est mesuré sur le **rendu réel**, et non sur les
valeurs CSS —
un dégradé posé sur une photo ne se calcule pas, il se regarde. La méthode :
les lignes de texte sont localisées par un `Range` posé sur les nœuds texte
(ce qui exclut les icônes et les blocs voisins), les glyphes passent en
`color: transparent` — et non en `visibility: hidden`, qui effacerait aussi le
fond propre d'un bouton — puis chaque pixel du fond est comparé à la couleur du
texte. Sur **65 zones** réparties sur 6 pages, en 1440 px et en 390 px, le pire
cas est à **4,66:1** (seuil WCAG AA : 4,5:1).

Deux chiffres d'étapes étaient sous ce seuil : le bleu ciel de la quatrième
pastille ne donnait que **2,68:1** sous du blanc — sous le seuil de 3:1 des
grands caractères, donc non conforme depuis l'origine. Les pastilles chaudes
portent maintenant un chiffre bleu nuit sur ambre vif (5,52:1), ce qui est à la
fois plus lisible et plus vivant que du blanc sur ambre (4,19:1).

Deux textes du bandeau CTA étaient sous le seuil **avant** ce changement (4,37:1
et 4,26:1) : ils étaient en bleu très pâle sur un dégradé qui s'ouvrait jusqu'au
`#0E86BE`. Ils sont passés en blanc pur et le dégradé est plafonné à `#0D7CAD`,
la teinte la plus claire qui reste conforme sous du texte blanc de petite taille.

## Régénérer le site

Le HTML de la racine est **généré** : modifiez le contenu dans `tools/`, jamais
les fichiers `.html` directement.

```bash
python3 tools/build.py
```

- `tools/data.py` — contenus éditoriaux (activités, prestations, tarifs, FAQ,
  avis, départements et communes)
- `tools/articles.py` — les 80 articles, un dictionnaire par article (la clé
  `villes` fait d'un article un article de zone)
- `tools/build.py` — templates, rendu HTML, JSON-LD, sitemap

Aucune dépendance : Python 3 seul suffit. Prévisualisation locale **via un
serveur** (obligatoire : les URL sans extension et les fontes ne fonctionnent
pas en `file://`) :

```bash
python3 -m http.server 8000   # puis http://localhost:8000
```

## Performance

Aucune requête tierce (pas de Google Fonts, pas de framework, pas de tracker) :
une feuille CSS (~28 Ko), un script JS (~9 Ko), le logo et le motif (~45 Ko), et
la photo de fond (89 Ko en WebP, 33 Ko sur mobile). Polices système.
Pages HTML de ~36 Ko.

## Réception des formulaires

Les formulaires envoient leurs demandes à **`formulaire.php`**, à la racine du
site. Ce script n'a aucune dépendance et fonctionne sur tout hébergement PHP,
dont l'offre mutualisée d'Hostinger retenue ici. Il valide le numéro et la
commune, écarte les robots (champ piège `_gotcha`), limite à six demandes par
appareil et par tranche de dix minutes, puis envoie un courriel lisible :

```
Téléphone            : 06 12 34 56 78
Ville                : Saint-Brieuc
Département          : Côtes-d'Armor (22)
Type d’intervention  : Plomberie & Dépannage
Page d’origine       : Plomberie 22 (/plomberie-depannage-cotes-d-armor-22/)
```

**À vérifier une fois en ligne** : que `DESTINATAIRE` reçoit bien les demandes
(faites un essai réel), et que `EXPEDITEUR` est une adresse du domaine — sinon
les messages partent en indésirables. Si l'hébergeur bloque `mail()`, remplacez
l'envoi par un service SMTP, ou pointez `SITE["form_endpoint"]` (dans
`tools/data.py`) vers un service externe qui accepte un POST JSON : Formspree,
Brevo, ou tout autre.

**Si l'adresse est vidée**, les demandes basculent sur un `mailto:` que le
visiteur doit envoyer lui-même depuis sa messagerie — autant dire qu'elles sont
perdues. C'était l'état du site jusqu'ici, et c'est pour cela que le repli
n'existe plus que comme filet de sécurité.

**Si le script est absent** (hébergement sans PHP), l'envoi échoue proprement :
le visiteur voit le numéro en gros bouton cliquable, et ce qu'il a saisi reste
dans les champs.

## À compléter avant mise en ligne

- [ ] **Identité de l'éditeur — provisoire, à rétablir** — le nom du dirigeant
      et les quatre identifiants d'immatriculation ont été retirés à la demande
      du client, avec l'adresse du siège social. Tout tient dans `tools/data.py` :
      `denomination`, `dirigeant`, `siege`, `siren`, `siret`, `rcs` et `tva`.
      Renseigner un vrai `siren` suffit à faire revenir le bloc complet (SIREN,
      SIRET, RCS, RNE, TVA) — voir `bloc_immatriculation()` dans
      `tools/build.py` ; le siège et le dirigeant se remettent en remplaçant
      leur valeur.

      **Ce n'est pas un état publiable.** Il ne reste aujourd'hui, pour
      identifier l'éditeur, que le nom commercial, un téléphone et un e-mail.
      Trois obligations distinctes sont en défaut :

      | Texte | Ce qu'il impose |
      | --- | --- |
      | LCEN, art. 6 III | nom et prénom de l'éditeur, son domicile, et le directeur de la publication |
      | Code de commerce, art. R.123-237 | le numéro SIREN et la mention du RCS de tout professionnel immatriculé |
      | RGPD, art. 13 | l'identité et les coordonnées du responsable du traitement |

      Les trois sont à rétablir avant mise en ligne. En l'état, le site peut
      servir à montrer le rendu, pas à être publié
- [ ] **Mentions légales** — l'hébergeur et l'immatriculation sont renseignés.
      Restent trois champs *[à compléter]* : le **numéro de contrat
      d'assurance**, les **activités déclarées au contrat**, et le **médiateur de
      la consommation** (obligatoire pour toute activité avec des particuliers,
      article L.612-1 du Code de la consommation)
- [ ] **Code NAF** — l'entreprise est immatriculée en `81.29A` (désinfection,
      désinsectisation, dératisation). Le site présente des prestations de
      plomberie, d'électricité et d'assainissement, qui relèvent d'autres codes
      (43.22A, 43.21A, 37.00Z). Vérifiez que les activités déclarées et le
      contrat d'assurance couvrent bien ce qui est vendu sur le site
- [ ] **Avis clients** — les témoignages et la note « 4,8/5 » sont des contenus
      d'exemple : remplacez-les par de vrais avis vérifiés avant publication
      (l'affichage d'avis fictifs est une pratique commerciale trompeuse)
- [ ] **Tarifs** — vérifier les montants indicatifs de `tools/data.py`
- [ ] **Photos** — remplir les 22 emplacements avec vos propres chantiers
      (voir « Emplacements photo »). N'utilisez que des visuels dont vous
      détenez les droits : présenter des images de banque comme vos
      réalisations est trompeur et juridiquement risqué
- [ ] **Pages Ads et identité de l'annonceur** — les régies publicitaires
      exigent que l'annonceur soit identifiable sur la page de destination.
      Tant que les mentions légales ne portent ni nom, ni SIREN, ni adresse
      (voir ci-dessus), une annonce renvoyant vers ces pages risque le refus
      à la validation. À régler avant de lancer les campagnes, pas après
- [ ] **Essai réel du formulaire** — une fois en ligne, envoyez une demande et
      vérifiez qu'elle arrive bien dans la boîte `contact@etablissement-breizh.fr`
      (voir « Réception des formulaires »). Tant que cet essai n'est pas fait,
      considérez que les demandes se perdent
- [ ] **Redirection `www` → domaine nu** — `SITE["url"]` vaut
      `https://etablissement-breizh.fr`, sans `www.`&nbsp;: c'est la forme
      canonique du site. Il reste à configurer chez l'hébergeur une
      redirection permanente (301) de `www.etablissement-breizh.fr` vers
      `etablissement-breizh.fr`, faute de quoi les deux formes répondent et
      se font concurrence
