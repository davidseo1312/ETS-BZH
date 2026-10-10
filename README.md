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

**Un numéro distinct.** Ces 52 pages portent le **06 20 06 01 96**, et lui seul —
le numéro du site n'y figure nulle part. Tout appel sur ce numéro vient donc
d'une annonce, sans dépendre du suivi d'appel de la régie. Le formulaire
transmet en plus un champ masqué `source` (« ADS Électricité Saint-Brieuc
(22) »), que
`formulaire.php` reprend en préfixe du sujet du courriel&nbsp;: les prospects
payants se distinguent au premier coup d'œil dans la boîte de réception.

**Structure de la page** (`page_ads` dans `tools/build.py`)&nbsp;:

1. Barre collante haute&nbsp;: identité, département, bouton d'appel.
2. Hero&nbsp;: **photo d'intervention en fond**, promesse, quatre preuves,
   bouton d'appel géant + formulaire à deux champs (téléphone, commune).
3. Bandeau de chiffres.
4. Les six urgences traitées, suivies d'un rappel d'appel.
5. **« Demandez Julien »**&nbsp;: le technicien, la transmission familiale, une
   photo et un bouton d'appel (voir l'avertissement plus bas).
6. **Galerie**&nbsp;: les quatre photos de la page métier Électricité,
   réduites à leur légende courte.
7. **Bloc commune par commune**&nbsp;: contexte départemental puis douze
   communes, chacune avec une note propre.
8. Les trois étapes (grille `steps--3`, voir ci-dessous).
9. **Avis clients** — six témoignages rattachés à six communes du
   département, avec le bandeau de note (voir l'avertissement).
10. **Engagements** — aucun prix, voir ci-dessous.
11. **FAQ de levée d'objection** — dix questions, voir ci-dessous.
12. CTA final, second formulaire.
13. **Bandeau assurances**&nbsp;: RC professionnelle, garantie décennale et les
    trois logos (Artisan de France, CMA, MIC Insurance).
14. Pied léger.
15. Barre d'appel fixe en bas sur mobile, là où se trouve le pouce.

### Palette propre aux pages Ads

Ces quatre pages ne portent **ni le bleu ni l'orange du site**&nbsp;: elles
sont en **bleu nuit et jaune**, et rien d'autre. `assets/css/ads.css`
redéfinit les variables de `style.css`&nbsp;; comme le fichier n'est chargé
que par ces pages, le site public n'en voit rien — vérifié au build.

Le partage des rôles est strict, et c'est lui qui fait la lisibilité&nbsp;:

| Couleur | Rôle |
| --- | --- |
| **Bleu nuit** `#0d2237` / `#10395c` | structure et sérieux&nbsp;: en-têtes, bandeaux, titres, texte, bouton de formulaire |
| **Jaune** `#ffc400` | l'action, et elle seule&nbsp;: boutons d'appel, œils d'accroche, chiffres clés, sceau |

Tout ce qui est jaune se clique ou désigne ce qu'il faut cliquer. Du jaune
partout ne ferait plus rien ressortir.

**Le jaune ne reçoit jamais de texte blanc**&nbsp;: `#ffc400` sous du blanc
tombe à 1,9:1, illisible. Il porte toujours le bleu nuit (9,8:1), d'où la
variable `--sur-jaune` qu'aucune règle n'outrepasse. Contrôle sur les pixels
rendus, 48 zones sur deux pages et deux largeurs&nbsp;: pire cas
**5,56:1** — la page est plus lisible qu'avec l'ancienne palette (4,64:1).

### ⚠ « Demandez Julien » et « de père en fils »

Ce bloc (`TECHNICIEN` dans `tools/ads.py`) **affirme des faits sur
l'entreprise**&nbsp;: qu'un technicien nommé Julien y travaille et répond au
téléphone, et que le métier s'est transmis de père en fils.

Sur une page publicitaire, une affirmation inexacte sur la nature ou
l'ancienneté de l'entreprise relève de la **pratique commerciale trompeuse**
(article L121-2 du Code de la consommation), et c'est également un motif de
refus en régie. **À ne publier que si c'est exact.** Si la transmission
familiale ne correspond pas à la réalité, retirez `sceau` et le troisième
paragraphe de `TECHNICIEN`&nbsp;: le reste du bloc — un électricien décroche,
il vous dit s'il faut venir — fonctionne sans cette affirmation.

Aucune navigation, aucun lien vers le site hormis les trois liens légaux du
pied&nbsp;: sur une page payante, chaque lien sortant est une fuite.

**Aucun prix affiché.** Ces pages n'avancent aucun montant. Un chiffre posé
sur une page payante est lu comme un engagement, et il se retourne contre
l'entreprise dès que l'intervention se révèle plus lourde que prévu. Le bloc
`ENGAGEMENTS` le remplace&nbsp;: il tient la promesse de transparence — c'est
elle qui lève l'objection, pas le montant — en annonçant que le prix est
donné avant le déplacement, que le devis est gratuit et que rien n'est engagé
sans accord. Vérifié au build&nbsp;: aucune occurrence de montant dans les
quatre pages.

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

### La FAQ

C'est l'étape où se gagne ou se perd l'appel&nbsp;: un visiteur venu d'une
annonce n'a aucune raison de faire confiance. Les dix questions suivent
**l'ordre dans lequel l'objection se pose**&nbsp;: d'abord le délai, puis le
prix, puis le risque, puis le passage à l'acte.

| # | Objection levée |
| --- | --- |
| 1 | *Vous allez mettre trois jours* → créneau annoncé, priorités expliquées |
| 2-3 | *Je vais me faire avoir sur le prix* → prix avant la route, déplacement facturé ou non |
| 4 | *Personne ne vient le dimanche* → 24h/24, majoration annoncée |
| 5 | *Et si ça se passe mal&nbsp;?* → RC pro, décennale, attestations sur demande |
| 6 | *Vous ne venez pas chez moi* → département entier, communes rurales comprises |
| 7 | *Qu'est-ce que je fais maintenant&nbsp;?* → consignes de sécurité réelles |
| 8 | *Vous allez repartir sans rien faire* → mise en sécurité d'abord, devis et date |
| 9 | *Je veux comparer* → devis gratuit, sans engagement |
| 10 | *C'est pour les particuliers seulement* → bailleurs, syndics, commerces |

Trois règles de rédaction&nbsp;: **aucun montant**&nbsp;; on répond vraiment,
y compris quand la réponse n'arrange pas — «&nbsp;oui, le diagnostic est
facturé s'il n'est suivi de rien&nbsp;» rassure davantage qu'un
«&nbsp;c'est gratuit&nbsp;» que personne ne croit&nbsp;; et la question sur
la commune porte le numéro du département de la page.

**La première est ouverte par défaut**&nbsp;: un accordéon entièrement fermé
se lit comme une page vide, surtout sur mobile. Une relance sous le bloc
renvoie vers l'appel. Le «&nbsp;+&nbsp;» passe au jaune d'action, comme tout
ce qui invite à cliquer.

Pas de `FAQPage` en données structurées&nbsp;: ces pages sont en `noindex`, le
balisage n'y servirait à rien.

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
- [ ] **Domaine** — `SITE["url"]` vaut encore `https://www.ets-bzh.fr` alors que
      l'e-mail est passé à `@etablissement-breizh.fr`. Si le site doit être publié
      sur `etablissement-breizh.fr`, changez aussi cette valeur dans
      `tools/data.py` : elle alimente les URLs canoniques, le sitemap et le
      JSON-LD
