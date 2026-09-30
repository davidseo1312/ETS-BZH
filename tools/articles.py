# -*- coding: utf-8 -*-
"""Articles d'urgence géolocalisés.

Chaque article traite **une situation précise**, pas un métier : le visiteur qui
tape « fosse septique qui déborde » n'est pas au même endroit que celui qui
cherche « plombier Saint-Brieuc ». Il est en panique, il veut savoir quoi faire
dans les cinq minutes, et il appelle si on le lui dit clairement.

Règle de non-redondance : aucun article ne reprend le contenu des pages
métier (causes de bouchons, mise aux normes NF C 15-100, liste des
prestations). Chacun apporte un raisonnement de diagnostic que les pages
métier n'ont pas.

Structure d'un article :
    slug      — URL sous /conseils/
    court     — libellé du fil d'Ariane (le titre complet y serait tronqué)
    dept      — numéro de département (lien vers la page métier correspondante)
    act       — clé de métier
    titre     — balise <title>
    h1, meta, mots_cles, chapo
    urgent    — les gestes à faire tout de suite, dans l'ordre
    danger    — l'avertissement de sécurité qui ne souffre pas d'exception
    sections  — [(h2, [paragraphes], [puces] ou None)]
    faq       — [(question, réponse)]
    date      — publication (ISO)
"""

ARTICLES = [

# ============================================================ 22 — CÔTES-D'ARMOR
{
 "slug": "fosse-septique-qui-deborde-cotes-d-armor",
 "court": "Fosse septique qui déborde (22)",
 "dept": "22", "act": "degorgement", "date": "2026-09-30",
 "titre": 'Fosse septique qui déborde (22) : que faire — ETS-BZH',
 "h1": "Fosse septique qui déborde dans les Côtes-d'Armor&nbsp;: que faire dans l'heure",
 "meta": "Fosse septique qui déborde dans les Côtes-d'Armor : les gestes immédiats, les 3 causes possibles, et quand appeler. Pompage 7j/7 au 02 20 06 00 75.",
 "mots_cles": ("fosse septique qui déborde, vidange fosse septique Côtes-d'Armor, "
               "assainissement non collectif 22, urgence fosse Saint-Brieuc"),
 "chapo": ("Un regard qui affleure, une odeur qui monte dans le jardin, des WC qui "
           "ne s'évacuent plus&nbsp;: une fosse qui déborde ne se règle pas en attendant "
           "lundi. Voici ce qu'il faut faire dans l'heure, ce qu'il ne faut surtout pas "
           "faire, et comment savoir si le problème vient de la fosse elle-même ou de "
           "ce qu'il y a après."),
 "urgent": [
   "Coupez tout usage d'eau dans la maison&nbsp;: WC, douche, lave-linge, lave-vaisselle. "
   "Chaque litre envoyé aggrave le débordement.",
   "Éloignez les enfants et les animaux, et ne marchez pas dans les eaux répandues.",
   "Ne versez aucun déboucheur chimique&nbsp;: il détruit les bactéries qui font "
   "fonctionner la fosse et rend la remise en service bien plus longue.",
   "Photographiez la zone avant tout nettoyage&nbsp;: votre assurance et le SPANC "
   "pourront vous les demander.",
   "Appelez-nous. Nous vous dirons au téléphone si un pompage d'urgence suffit "
   "ou s'il faut aussi contrôler le départ.",
 ],
 "danger": ("Ne descendez jamais dans une fosse, et n'y passez pas la tête pour "
            "regarder. La fermentation des boues produit de l'hydrogène sulfuré, un gaz "
            "qui endort l'odorat avant d'assommer&nbsp;: plusieurs accidents mortels ont "
            "lieu chaque année en France, y compris chez des professionnels. Le tampon "
            "s'ouvre, on s'écarte, on laisse ventiler."),
 "sections": [
  ("Trois causes possibles, trois interventions différentes",
   ["Un débordement ne veut pas dire « fosse pleine ». Dans les faits, nous "
    "rencontrons trois situations, et elles ne se traitent pas de la même façon.",
    "<strong>La fosse est effectivement pleine.</strong> Les boues ont atteint le "
    "niveau de la sortie. Le signe qui ne trompe pas&nbsp;: tous les appareils de la "
    "maison s'évacuent mal en même temps, et cela s'est dégradé progressivement sur "
    "plusieurs semaines. Un pompage règle la situation.",
    "<strong>La sortie ou le préfiltre est bouché.</strong> La fosse n'est pas pleine, "
    "mais rien ne sort. Le préfiltre — ce panier de pouzzolane placé en sortie sur les "
    "installations récentes — se colmate en quelques années et personne ne pense à le "
    "nettoyer. Là, le pompage seul ne règle rien&nbsp;: tout reviendra en quinze jours.",
    "<strong>L'épandage ne reçoit plus.</strong> Le sol est saturé, colmaté, ou la nappe "
    "est remontée. C'est typiquement ce que nous voyons après un hiver pluvieux dans "
    "l'arrière-pays costarmoricain. Le pompage donne de l'air pour quelques jours, mais "
    "le diagnostic doit aller plus loin.",
    "C'est pour cela que nous inspectons le départ à la caméra quand le doute "
    "subsiste&nbsp;: repartir sans savoir laquelle des trois causes est en jeu, c'est "
    "garantir un second appel."],
   None),
  ("Pourquoi c'est si fréquent dans les Côtes-d'Armor",
   ["Le département compte une proportion importante d'installations d'assainissement "
    "non collectif, en particulier dans l'arrière-pays entre Guingamp, Loudéac et "
    "Lamballe-Armor, où l'habitat dispersé n'a jamais été raccordé au tout-à-l'égout. "
    "Beaucoup de ces installations ont été posées il y a trente ou quarante ans, sur "
    "des sols schisteux qui drainent mal.",
    "S'y ajoute un facteur saisonnier que nos clients sous-estiment&nbsp;: en hiver, la "
    "nappe remonte, et un épandage qui fonctionnait très bien en août ne reçoit plus "
    "rien en février. Les longères rénovées posent un autre problème&nbsp;: la fosse a "
    "été dimensionnée pour quatre personnes, et la maison en accueille désormais six, "
    "avec deux salles de bain. Le volume ne suit plus."],
   None),
  ("Ce que nous faisons sur place",
   ["L'intervention d'urgence suit toujours le même ordre&nbsp;: pomper pour arrêter le "
    "débordement, puis comprendre pourquoi il a eu lieu.",
    "Le camion pompe la fosse, les boues sont évacuées vers une filière agréée et "
    "vous recevez le bordereau de suivi — document que le SPANC peut vous demander lors "
    "du contrôle périodique. Nous rinçons ensuite les parois, nettoyons le préfiltre "
    "s'il y en a un, et vérifions que le départ vers l'épandage s'écoule réellement.",
    "Si l'écoulement reste anormal, l'inspection caméra localise l'obstacle au mètre "
    "près, et vous recevez le diagnostic par écrit. Nous vous disons alors clairement ce "
    "qui relève de l'entretien courant et ce qui relève de travaux — sans chiffrer le "
    "second pour justifier le premier."],
   None),
  ("Après l'urgence : les repères qui évitent la récidive",
   [],
   ["Faire vidanger avant que le niveau des boues n'atteigne la moitié du volume utile, "
    "soit en général tous les quatre ans pour un foyer permanent.",
    "Nettoyer le préfiltre une à deux fois par an&nbsp;: c'est cinq minutes, et c'est la "
    "panne la plus évitable des trois.",
    "Ne rien jeter dans les WC hors papier hygiénique — les lingettes dites biodégradables "
    "ne se dégradent pas à l'échelle d'une fosse.",
    "Surveiller les eaux de pluie&nbsp;: une gouttière qui se déverse près de l'épandage "
    "suffit à le noyer chaque hiver.",
    "Conserver les bordereaux de vidange&nbsp;: ils vous seront réclamés à la vente du bien."],
   ),
 ],
 "faq": [
  ("Ma fosse a été vidangée il y a un an, pourquoi déborde-t-elle déjà&nbsp;?",
   "Parce que le problème n'était probablement pas le niveau de boues. Une vidange "
   "faite alors que le préfiltre est colmaté ou que l'épandage est saturé soulage "
   "quelques semaines, pas plus. C'est la raison pour laquelle nous contrôlons le "
   "départ avant de repartir, et pas seulement le niveau."),
  ("Puis-je pomper moi-même avec une pompe vide-cave&nbsp;?",
   "Non. Une pompe de relevage n'est pas conçue pour des boues chargées et se bloque "
   "immédiatement, et surtout, vous ne pouvez rejeter ces effluents nulle part&nbsp;: "
   "les épandre dans le jardin ou les envoyer au fossé est interdit et sanctionnable. "
   "Les matières doivent partir vers une filière agréée, avec bordereau."),
  ("Dois-je prévenir le SPANC&nbsp;?",
   "Le service public d'assainissement non collectif de votre commune ou de votre "
   "communauté d'agglomération n'a pas à être appelé en urgence, mais il est votre "
   "interlocuteur si le débordement révèle une installation non conforme. Gardez le "
   "bordereau de vidange et notre rapport&nbsp;: ce sont les pièces qu'il examinera."),
  ("Intervenez-vous le dimanche dans l'arrière-pays&nbsp;?",
   "Oui, l'astreinte couvre les nuits, les week-ends et les jours fériés sur "
   "l'ensemble des Côtes-d'Armor. Le délai est annoncé au téléphone avant tout "
   "déplacement&nbsp;: sur les secteurs ruraux, comptez généralement un peu plus de "
   "temps que sur l'agglomération briochine."),
 ],
},

{
 "slug": "panne-de-courant-apres-tempete-cotes-d-armor",
 "court": "Panne de courant après tempête (22)",
 "dept": "22", "act": "electricite", "date": "2026-09-30",
 "titre": 'Panne de courant après tempête (22) : que faire — ETS-BZH',
 "h1": "Plus de courant après une tempête dans les Côtes-d'Armor&nbsp;: réseau public ou votre installation&nbsp;?",
 "meta": "Plus de courant après une tempête dans les Côtes-d'Armor : le test en 2 minutes pour savoir si c'est le réseau ou chez vous. Urgence au 02 20 06 00 75.",
 "mots_cles": ("panne de courant tempête Côtes-d'Armor, coupure électricité 22, "
               "électricien urgence Saint-Brieuc, disjoncteur qui ne se réarme pas"),
 "chapo": ("Le vent est tombé, les voisins ont de la lumière, et vous non. Ou bien "
           "tout le quartier est noir. Ces deux situations n'appellent pas le même coup "
           "de téléphone, et appeler le mauvais interlocuteur fait perdre des heures. "
           "Voici le test simple qui permet de trancher, et ce qu'il faut faire ensuite."),
 "urgent": [
   "Regardez dehors&nbsp;: si l'éclairage public et les maisons voisines sont éteints, "
   "la panne vient du réseau. Signalez-la au service de dépannage de votre "
   "distributeur — le numéro figure sur votre facture d'électricité.",
   "Si vous êtes le seul dans le noir, ouvrez votre tableau et regardez lequel des "
   "appareils est abaissé&nbsp;: le gros interrupteur en amont ou l'un des petits.",
   "Si vous sentez une odeur de brûlé, si le tableau est humide ou si de l'eau est "
   "entrée par la toiture, ne touchez à rien et appelez.",
   "Débranchez les appareils sensibles — box, télévision, informatique — avant tout "
   "retour du courant&nbsp;: les surtensions au réarmement en détruisent beaucoup.",
 ],
 "danger": ("Si un câble pend dans votre jardin ou dans la rue après une tempête, "
            "n'approchez sous aucun prétexte, même s'il paraît inerte&nbsp;: il peut être "
            "réalimenté sans préavis. Écartez tout le monde à bonne distance et signalez-le "
            "immédiatement au distributeur. Ce câble n'est ni à nous ni à vous&nbsp;: aucun "
            "électricien privé n'a le droit d'y toucher."),
 "sections": [
  ("Le test en deux minutes",
   ["Tout se joue devant le tableau. Il faut distinguer deux appareils que beaucoup "
    "confondent.",
    "<strong>Le disjoncteur de branchement</strong> est le plus gros, généralement "
    "isolé, souvent près du compteur. C'est la limite entre le réseau public et chez "
    "vous. S'il a sauté, le défaut est dans votre installation, presque toujours.",
    "<strong>Les disjoncteurs divisionnaires</strong> sont les petits alignés en rangée, "
    "un par circuit. Si l'un d'eux est abaissé, le défaut est sur ce circuit-là "
    "uniquement&nbsp;: une prise, un luminaire, un appareil.",
    "<strong>L'interrupteur différentiel</strong>, un peu plus large, protège un groupe "
    "de circuits. Quand il saute après une tempête, c'est le signe classique d'une "
    "entrée d'eau quelque part&nbsp;: un boîtier extérieur, une VMC, un luminaire de "
    "terrasse, une prise de garage.",
    "Si aucun n'a bougé et que vous n'avez toujours rien, la coupure est en amont&nbsp;: "
    "c'est le réseau, et votre électricien n'y peut rien."],
   None),
  ("Le différentiel saute dès que je le remonte : la méthode",
   ["C'est le cas le plus fréquent après un coup de vent avec pluie battante. La "
    "démarche est méthodique et vous pouvez la mener vous-même sans risque, car elle "
    "consiste uniquement à manœuvrer des protections.",
    "Abaissez tous les disjoncteurs divisionnaires du groupe concerné. Remontez le "
    "différentiel&nbsp;: il doit tenir. Puis remontez les divisionnaires un par un, en "
    "attendant quelques secondes à chaque fois. Celui qui fait retomber le différentiel "
    "désigne le circuit en défaut. Laissez-le abaissé, vous avez récupéré le courant "
    "partout ailleurs.",
    "Il vous reste à trouver ce qui, sur ce circuit, a pris l'eau. Neuf fois sur dix, "
    "c'est un point lumineux extérieur, une prise de terrasse, un abri de jardin ou un "
    "portail motorisé. Débranchez ce qui est débranchable et refaites l'essai.",
    "Si le différentiel refuse de tenir même avec tous les divisionnaires abaissés, le "
    "défaut est en amont des circuits, dans le tableau lui-même ou sur la liaison. "
    "Arrêtez là&nbsp;: c'est notre travail."],
   None),
  ("Ce que le littoral costarmoricain change vraiment",
   ["Sur la côte, entre Paimpol, Saint-Brieuc et Erquy, ce n'est pas seulement le vent "
    "qui abîme les installations&nbsp;: c'est l'air salin. Le sel se dépose sur les "
    "contacts, absorbe l'humidité, et finit par créer des chemins de fuite là où tout "
    "était sain quelques années plus tôt. Les coffrets extérieurs, les prises de "
    "terrasse et les luminaires de façade sont les premiers touchés.",
    "L'autre particularité locale tient à l'habitat&nbsp;: beaucoup de longères et de "
    "maisons de bourg ont vu leur installation étendue par tranches successives, avec "
    "des dérivations dans les combles ou les dépendances. Après une tempête, l'eau entre "
    "par la toiture et ressort par ces dérivations oubliées. C'est à ce moment que "
    "l'absence de protection différentielle 30&nbsp;mA sur une partie de l'installation "
    "devient réellement dangereuse."],
   None),
  ("Quand il faut appeler sans attendre le lendemain",
   [],
   ["Odeur de brûlé, plastique fondu ou trace noire sur le tableau ou une prise.",
    "Eau visible dans le tableau, ou tableau installé sous une zone qui a fui.",
    "Le disjoncteur de branchement refuse de se réarmer.",
    "Grésillement ou claquement à l'intérieur du tableau.",
    "Chocs électriques ressentis au contact d'un robinet, d'un évier ou d'un appareil.",
    "Installation partiellement immergée après une entrée d'eau&nbsp;: ne remettez rien "
    "en service avant contrôle."],
   ),
 ],
 "faq": [
  ("Comment savoir si la coupure vient du réseau&nbsp;?",
   "Trois indices concordants&nbsp;: l'éclairage public est éteint, les voisins n'ont "
   "rien non plus, et aucune protection n'a bougé dans votre tableau. Dans ce cas, seul "
   "le distributeur peut intervenir&nbsp;; le numéro de dépannage figure sur votre "
   "facture d'électricité, et la plupart des distributeurs publient une carte des "
   "coupures en cours."),
  ("Mon congélateur a dégelé pendant la coupure, que faire&nbsp;?",
   "Relevez la durée de la coupure et photographiez le contenu avant de jeter quoi que "
   "ce soit&nbsp;: beaucoup de contrats multirisque habitation couvrent la perte de "
   "denrées après une coupure prolongée. Cela se règle avec votre assureur, pas avec "
   "l'électricien."),
  ("Puis-je remettre le courant moi-même après une inondation&nbsp;?",
   "Non, pas tant qu'une partie de l'installation a été mouillée. Un circuit noyé peut "
   "sembler sec en surface alors que l'eau stagne dans les gaines. Le contrôle "
   "d'isolement se fait avec un appareil de mesure, avant remise en service&nbsp;; c'est "
   "l'une des interventions les plus courantes que nous menons après un coup de vent."),
  ("Intervenez-vous la nuit après une tempête&nbsp;?",
   "Oui, l'astreinte fonctionne 24h/24 et 7j/7 sur les Côtes-d'Armor. En période de "
   "tempête, les demandes affluent&nbsp;: nous annonçons un délai réaliste dès l'appel "
   "plutôt qu'un horaire que nous ne tiendrions pas, et nous traitons en priorité les "
   "situations présentant un risque."),
 ],
},

# =============================================================== 29 — FINISTÈRE
{
 "slug": "canalisation-gelee-finistere",
 "court": "Canalisation gelée (29)",
 "dept": "29", "act": "plomberie", "date": "2026-09-30",
 "titre": 'Canalisation gelée (29) : dégeler sans casser — ETS-BZH',
 "h1": 'Canalisation gelée en Finistère&nbsp;: dégeler sans faire éclater le tuyau',
 "meta": "Canalisation gelée en Finistère : la méthode pour dégeler sans faire éclater le tuyau, et quoi vérifier après. Plombier d'urgence au 02 20 06 00 75.",
 "mots_cles": ("canalisation gelée Finistère, tuyau gelé que faire, plombier urgence "
               "Brest, dégeler canalisation, résidence secondaire gel 29"),
 "chapo": ("Il a gelé cette nuit, le robinet crache un filet puis plus rien. La "
           "tentation est de chauffer fort et vite&nbsp;: c'est exactement ce qui fait "
           "éclater le tuyau. Un bouchon de glace se dégèle lentement, dans un ordre "
           "précis, et la vraie urgence commence souvent au moment où l'eau revient."),
 "urgent": [
   "Fermez le robinet d'arrêt général avant toute tentative de dégel. Si le tuyau a "
   "déjà fendu, l'eau ne sortira pas au moment où la glace cédera.",
   "Ouvrez le robinet le plus proche de la zone gelée, côté maison&nbsp;: la vapeur et "
   "l'eau de fonte doivent pouvoir s'échapper, sinon la pression monte.",
   "Chauffez doucement et en partant du robinet vers la zone gelée, jamais l'inverse.",
   "Vérifiez en même temps si le compteur tourne alors que tout est fermé&nbsp;: c'est "
   "le signe qu'une conduite a déjà rompu quelque part.",
 ],
 "danger": ("Jamais de flamme sur une canalisation&nbsp;: ni chalumeau, ni lampe à "
            "souder, ni décapeur thermique à pleine puissance. Le cuivre transmet la "
            "chaleur beaucoup plus vite que la glace ne fond, la vapeur se forme en "
            "poche et le tuyau éclate — parfois à un mètre du point chauffé. Dans une "
            "maison ancienne, la flamme au contact d'un plancher bois ou d'une gaine "
            "ajoute un risque d'incendie tout à fait réel."),
 "sections": [
  ("La méthode qui marche : lentement, et dans le bon sens",
   ["Le principe tient en une phrase&nbsp;: l'eau de fonte doit toujours avoir un chemin "
    "de sortie. Si vous dégelez le milieu d'un bouchon, l'eau libérée se retrouve "
    "coincée entre deux blocs de glace, et c'est la pression qui fait céder le tuyau.",
    "Commencez donc par le robinet, ouvert, et remontez progressivement vers la zone "
    "gelée. Un sèche-cheveux, un chiffon trempé dans l'eau chaude, un ruban chauffant, "
    "ou tout simplement un convecteur posé à distance dans la pièce&nbsp;: tout ce qui "
    "chauffe doucement convient. Comptez souvent une bonne heure, parfois plus.",
    "Repérer la zone gelée demande un peu d'observation&nbsp;: le givre extérieur, une "
    "portion de tuyau anormalement froide au toucher, ou un renflement visible. Les "
    "points critiques sont toujours les mêmes&nbsp;: traversée de vide sanitaire, "
    "passage en garage non chauffé, conduite en façade nord, compteur en regard "
    "extérieur, canalisation dans une dépendance."],
   None),
  ("Le vrai risque arrive au dégel",
   ["Un tuyau gelé est rarement le problème principal. La glace, en prenant du volume, "
    "a pu fendre le cuivre ou déboîter un raccord, et tant que le bouchon est en place, "
    "rien ne coule. La fuite se déclare au moment précis où l'eau reprend son chemin — "
    "souvent quand personne ne regarde.",
    "C'est pourquoi le robinet d'arrêt reste fermé pendant l'opération, et qu'on "
    "rouvre lentement, en surveillant. Si vous entendez un sifflement, si la pression ne "
    "revient pas normalement, ou si le compteur continue de tourner une fois tout "
    "refermé, il y a une rupture en amont.",
    "Le scénario le plus coûteux que nous rencontrons en Finistère n'est pas le tuyau "
    "gelé&nbsp;: c'est la maison inoccupée. Une résidence secondaire de la côte "
    "nord-finistérienne, une canalisation qui cède un mardi de janvier, et l'eau qui "
    "coule jusqu'au week-end suivant. À ce stade, ce n'est plus un dépannage de "
    "plomberie, c'est un dossier d'assurance."],
   None),
  ("Finistère : le froid n'est pas rude, mais les installations sont exposées",
   ["Le climat breton ne descend pas très bas, et c'est précisément le piège&nbsp;: "
    "parce que les grands froids sont rares, beaucoup d'installations n'ont jamais été "
    "protégées. Les conduites passent en apparent dans des dépendances, les compteurs "
    "sont en regard extérieur, les abris de jardin alimentés en eau n'ont aucune "
    "vidange. Il suffit de deux nuits à -4&nbsp;°C avec du vent pour que cela suffise.",
    "Le parc de résidences secondaires aggrave l'exposition. Entre la côte des Abers, "
    "la presqu'île de Crozon et le pays bigouden, des milliers de maisons passent "
    "l'hiver vides et non chauffées. Elles ne sont pas conçues pour cela&nbsp;: elles "
    "sont conçues pour être habitées l'été.",
    "La parade est connue et coûte peu&nbsp;: fermer l'arrivée d'eau générale à chaque "
    "départ prolongé, purger les conduites par le point le plus bas, isoler les "
    "portions exposées, et maintenir un chauffage hors gel dans les pièces qui "
    "contiennent de la plomberie."],
   None),
  ("Les six points à protéger avant le prochain coup de froid",
   [],
   ["Le compteur en regard extérieur&nbsp;: un isolant adapté dans le regard, jamais de "
    "matériau qui absorbe l'eau.",
    "Les conduites en vide sanitaire et en garage&nbsp;: manchons isolants sur toute la "
    "longueur, y compris les coudes.",
    "Les robinets extérieurs&nbsp;: fermer la vanne intérieure et laisser le robinet "
    "extérieur ouvert pour qu'il se vide.",
    "Le circuit d'une dépendance ou d'un abri&nbsp;: une vanne d'isolement et une purge, "
    "c'est la seule vraie protection.",
    "La résidence secondaire&nbsp;: coupure générale, purge complète, et quelqu'un qui "
    "passe après un épisode de gel.",
    "Le local technique de piscine, oublié presque à chaque fois."],
   ),
 ],
 "faq": [
  ("Combien de temps pour dégeler une canalisation&nbsp;?",
   "Comptez une à deux heures avec un chauffage doux, davantage si la portion gelée "
   "est longue ou enterrée. Si rien ne se passe après deux heures, insister ne sert à "
   "rien&nbsp;: soit le bouchon est ailleurs, soit le tuyau est déjà rompu."),
  ("Mon tuyau a éclaté, l'assurance prend-elle en charge&nbsp;?",
   "La plupart des contrats multirisque habitation couvrent les dégâts des eaux "
   "consécutifs à une rupture par le gel, mais souvent sous condition&nbsp;: logement "
   "chauffé, ou circuit purgé en cas d'absence prolongée. Relisez cette clause, elle "
   "est presque toujours présente. Notre rapport d'intervention vous servira de pièce."),
  ("Peut-on prévenir le gel avec un simple ruban chauffant&nbsp;?",
   "Oui, c'est une solution efficace sur une portion identifiée — compteur, traversée "
   "de mur, conduite en apparent — à condition qu'il soit alimenté et conçu pour cet "
   "usage. Il ne remplace pas la purge sur un logement laissé sans chauffage tout "
   "l'hiver."),
  ("Intervenez-vous sur les résidences secondaires en l'absence du propriétaire&nbsp;?",
   "Oui, à condition d'avoir un accès et un accord écrit du propriétaire. Beaucoup de "
   "nos interventions hivernales en Finistère sont déclenchées par un voisin ou un "
   "gardien qui constate un dégât. Nous intervenons, nous sécurisons, et nous "
   "transmettons le rapport photographique au propriétaire."),
 ],
},

{
 "slug": "eaux-usees-qui-remontent-douche-finistere",
 "court": "Eaux usées qui remontent (29)",
 "dept": "29", "act": "degorgement", "date": "2026-09-30",
 "titre": "Eaux usées qui remontent (29) : d'où ça vient — ETS-BZH",
 "h1": "L'eau remonte dans la douche à Brest ou Quimper&nbsp;: siphon, collecteur ou réseau public&nbsp;?",
 "meta": "L'eau remonte dans la douche à Brest ou Quimper : le test qui localise le bouchon et dit qui doit payer. Débouchage 7j/7 au 02 20 06 00 75.",
 "mots_cles": ("eaux usées qui remontent douche, refoulement canalisation Brest, "
               "débouchage Quimper, bouchon collecteur Finistère, qui paie débouchage"),
 "chapo": ("Quand une eau grise et odorante remonte par la bonde de douche, ce n'est "
           "jamais la douche le problème&nbsp;: elle est simplement le point le plus bas "
           "de la maison. Le bouchon est en aval, et selon l'endroit où il se trouve, "
           "l'intervention — et la facture — ne relèvent pas des mêmes personnes."),
 "urgent": [
   "N'utilisez plus aucun point d'eau de l'étage concerné, y compris le lave-linge "
   "et le lave-vaisselle&nbsp;: tout ce qui part redescend chez vous.",
   "Ne versez pas de déboucheur chimique dans une eau stagnante&nbsp;: il ne l'atteindra "
   "pas et rendra l'intervention dangereuse pour le technicien.",
   "Épongez sans jeter les eaux dans une autre évacuation du logement.",
   "Faites le test des trois appareils décrit plus bas&nbsp;: il vous fera gagner "
   "une heure au téléphone.",
 ],
 "danger": ("Des eaux usées remontées sont chargées en bactéries&nbsp;: gants, "
            "aération, désinfection des surfaces ensuite, et tenez les enfants à "
            "l'écart. En immeuble, si plusieurs logements sont touchés en même temps, "
            "prévenez le syndic dans la foulée&nbsp;: le problème est collectif et la "
            "réponse doit l'être."),
 "sections": [
  ("Le test des trois appareils",
   ["Avant d'appeler qui que ce soit, cinq minutes d'observation vous diront presque "
    "toujours où se trouve le bouchon.",
    "<strong>Un seul appareil est touché</strong> — la douche uniquement, les autres "
    "s'évacuent normalement. Le bouchon est local, dans le siphon ou juste après. C'est "
    "le cas le plus simple, souvent réglé au furet en moins d'une heure.",
    "<strong>Plusieurs appareils du même niveau sont touchés</strong> — douche, WC et "
    "évier de la salle de bain refoulent ensemble. Le bouchon est sur la canalisation "
    "commune de cet étage, en aval du raccordement.",
    "<strong>Tout le logement est touché, et l'eau remonte par le point le plus bas</strong> "
    "— souvent la douche du rez-de-chaussée ou un siphon de sol de garage. Le bouchon "
    "est sur le collecteur principal, voire sur le branchement vers le réseau public.",
    "Un dernier indice, utile en maison&nbsp;: allez soulever le tampon du regard "
    "extérieur. Si le regard est plein, le bouchon est après lui, donc côté "
    "branchement. S'il est vide alors que ça refoule dans la maison, le bouchon est "
    "entre la maison et le regard."],
   None),
  ("Qui paie quoi : la limite n'est pas où l'on croit",
   ["La règle générale est simple à énoncer&nbsp;: ce qui est situé à l'intérieur de "
    "votre propriété est à votre charge, ce qui est sous le domaine public relève du "
    "service d'assainissement de la collectivité. La limite se matérialise en général "
    "au niveau du regard de branchement.",
    "En immeuble, la séparation est différente&nbsp;: la canalisation qui dessert votre "
    "seul logement est privative, la colonne verticale qui dessert plusieurs logements "
    "est une partie commune, donc du ressort du syndic. Un refoulement qui touche "
    "plusieurs appartements d'une même colonne n'est jamais à la charge d'un seul "
    "occupant.",
    "En location, l'usage veut que le débouchage courant relève du locataire au titre "
    "de l'entretien, et que la réparation d'une canalisation dégradée, affaissée ou "
    "percée revienne au propriétaire. C'est précisément pour trancher ce genre de "
    "situation que l'inspection caméra est utile&nbsp;: elle documente la cause, et un "
    "rapport écrit vaut mieux qu'une discussion."],
   None),
  ("Brest, Quimper et la côte : trois particularités locales",
   ["Le bâti ancien de Brest et des centres-villes finistériens compte encore beaucoup "
    "de collecteurs en fonte ou en grès. Ces matériaux se rétrécissent avec les dépôts, "
    "et leurs joints se déchaussent&nbsp;: un bouchon qui revient tous les six mois au "
    "même endroit signale presque toujours un défaut structurel, pas un excès de "
    "lingettes.",
    "Sur les communes littorales, les réseaux enterrés sont sollicités autrement&nbsp;: "
    "les racines des haies et des pins cherchent l'humidité et pénètrent par les joints, "
    "et l'eau de pluie s'invite dans des réseaux qui n'étaient pas prévus pour elle. "
    "Après un gros épisode pluvieux, nous voyons des refoulements sans le moindre "
    "bouchon&nbsp;: c'est le réseau qui est saturé, et un clapet anti-retour est alors la "
    "seule vraie parade.",
    "Enfin, les locations saisonnières changent le rythme d'usage&nbsp;: une installation "
    "dimensionnée pour un foyer reçoit six personnes pendant trois semaines. C'est "
    "souvent là que le bouchon latent se déclare."],
   None),
  ("Ce qui se passe quand nous arrivons",
   [],
   ["Localisation du bouchon par les regards et, si nécessaire, par inspection caméra.",
    "Débouchage au furet électrique pour un bouchon ponctuel, hydrocurage haute "
    "pression si le réseau est encrassé sur la longueur.",
    "Contrôle de l'écoulement en votre présence, sur tous les appareils concernés.",
    "Diagnostic écrit si une cause structurelle apparaît&nbsp;: affaissement, racines, "
    "joint déchaussé, contre-pente.",
    "Conseil sur le clapet anti-retour si le refoulement vient du réseau et non de "
    "chez vous."],
   ),
 ],
 "faq": [
  ("L'eau remonte uniquement quand je fais tourner le lave-linge, est-ce grave&nbsp;?",
   "C'est le signe d'une canalisation partiellement obstruée&nbsp;: elle absorbe un "
   "débit normal mais pas le rejet rapide d'une machine. Le bouchon est déjà formé et "
   "il finira par se refermer complètement. Traité à ce stade, cela reste une "
   "intervention simple."),
  ("Puis-je utiliser un déboucheur chimique en attendant&nbsp;?",
   "Non, surtout pas dans une eau déjà stagnante. Le produit ne descend pas jusqu'au "
   "bouchon, il reste en surface, et il devient dangereux à manipuler lors du "
   "débouchage — projections comprises. Sur une canalisation ancienne en fonte, "
   "certains produits attaquent en plus le métal."),
  ("Combien de temps pour un débouchage en urgence à Brest ou Quimper&nbsp;?",
   "Sur les agglomérations brestoise et quimpéroise, nous visons l'heure&nbsp;; sur les "
   "communes plus éloignées, deux à trois heures. Le délai vous est annoncé au "
   "téléphone avant tout déplacement, et le devis est validé avec vous avant le "
   "démarrage."),
  ("Le bouchon revient tous les six mois, que faut-il faire&nbsp;?",
   "Arrêter de déboucher et commencer par regarder. Une récidive régulière au même "
   "endroit vient d'une cause physique&nbsp;: contre-pente, affaissement, racines, joint "
   "ouvert. L'inspection caméra la localise, et l'hydrocurage ne suffira pas à la faire "
   "disparaître."),
 ],
},

# ========================================================= 35 — ILLE-ET-VILAINE
{
 "slug": "colonne-eaux-usees-bouchee-rennes",
 "court": "Colonne d'eaux usées bouchée (35)",
 "dept": "35", "act": "degorgement", "date": "2026-09-30",
 "titre": 'Colonne bouchée à Rennes : qui appelle, qui paie — ETS-BZH',
 "h1": "Colonne d'eaux usées bouchée à Rennes&nbsp;: qui appelle, qui paie, en combien de temps",
 "meta": "Colonne d'eaux usées bouchée en immeuble à Rennes : reconnaître un problème collectif, prévenir le syndic, faire intervenir. 7j/7 au 02 20 06 00 75.",
 "mots_cles": ("colonne eaux usées bouchée Rennes, débouchage colonne immeuble, "
               "syndic canalisation bouchée, dégorgement copropriété Ille-et-Vilaine"),
 "chapo": ("Dans un immeuble, un refoulement n'est presque jamais une affaire "
           "individuelle. Quand la colonne verticale se bouche, l'eau ressort chez celui "
           "qui habite le plus bas — qui n'y est pour rien. Savoir reconnaître ce cas en "
           "cinq minutes évite une intervention inutile chez le mauvais occupant, et "
           "surtout une facture adressée à la mauvaise personne."),
 "urgent": [
   "Faites cesser tout rejet dans la colonne&nbsp;: prévenez les voisins des étages "
   "au-dessus, c'est le geste le plus efficace des dix premières minutes.",
   "Appelez le syndic ou son astreinte&nbsp;: une colonne est une partie commune, et "
   "c'est lui qui donne l'ordre d'intervenir.",
   "Si le syndic est injoignable et que l'eau continue de monter, faites intervenir "
   "et conservez tous les justificatifs&nbsp;: une mesure conservatoire face à un "
   "dommage imminent se défend.",
   "Photographiez, horodatez, notez les logements touchés&nbsp;: c'est la pièce "
   "maîtresse du dossier d'assurance.",
 ],
 "danger": ("Un refoulement d'eaux usées en pied de colonne peut atteindre les "
            "installations électriques d'un rez-de-chaussée ou d'un sous-sol. Si l'eau "
            "s'approche d'un tableau, d'une prise ou d'une chaufferie, coupez "
            "l'alimentation du local concerné avant d'y entrer, et n'y faites entrer "
            "personne pieds nus."),
 "sections": [
  ("Comment reconnaître un bouchon de colonne en cinq minutes",
   ["La différence entre un bouchon privatif et un bouchon de colonne se voit à trois "
    "signes, et il suffit d'un seul pour lever le doute.",
    "<strong>Plusieurs logements sont touchés en même temps.</strong> Un appel au voisin "
    "du dessus ou du dessous suffit. Si deux appartements superposés refoulent, le "
    "problème est vertical, donc commun.",
    "<strong>L'eau qui remonte chez vous n'est pas la vôtre.</strong> Vous n'avez rien "
    "fait couler depuis une heure, et pourtant ça monte dans la douche ou l'évier quand "
    "un voisin tire la chasse. C'est le signe le plus net.",
    "<strong>Des glouglous remontent des appareils à l'autre bout du logement.</strong> "
    "L'air est chassé par la colonne obstruée et ressort par le premier siphon "
    "disponible.",
    "À l'inverse, si vous êtes seul touché et que tout l'immeuble fonctionne, votre "
    "évacuation privative est en cause, et l'intervention est à votre charge."],
   None),
  ("Le bon ordre d'appel, et pourquoi il compte",
   ["L'erreur classique consiste à faire venir un plombier à titre personnel, à payer "
    "l'intervention, puis à tenter de se faire rembourser par la copropriété. Cela "
    "fonctionne rarement sans validation préalable.",
    "L'ordre efficace est le suivant&nbsp;: prévenir les voisins, appeler le syndic — "
    "la plupart disposent d'une astreinte hors horaires — et laisser le syndic mandater "
    "l'entreprise. La facture part alors directement sur les charges communes, et "
    "personne n'avance d'argent.",
    "Nous intervenons régulièrement sur mandat de syndics et de bailleurs rennais, et "
    "nous fournissons le rapport nécessaire à la répartition des charges. Si le syndic "
    "est injoignable et que le dommage s'aggrave, l'occupant peut faire intervenir à "
    "titre conservatoire&nbsp;: il faut alors conserver l'ensemble des preuves — heure "
    "des appels, photos, rapport d'intervention — car c'est ce dossier qui permettra la "
    "prise en charge."],
   None),
  ("Rennes : pourquoi les colonnes lâchent plus souvent ici",
   ["La métropole rennaise concentre une part importante du parc collectif breton, avec "
    "deux profils qui posent chacun leur problème. Les immeubles anciens de "
    "l'intra-rocade ont des colonnes en fonte dont les diamètres se sont réduits par "
    "dépôts successifs&nbsp;; ceux des grands ensembles des années soixante-dix ont des "
    "colonnes en PVC de faible section, avec des dévoiements horizontaux dans lesquels "
    "tout stagne.",
    "S'ajoute la rotation locative, très forte dans une ville universitaire&nbsp;: les "
    "usages changent chaque année, les consignes d'immeuble ne se transmettent pas, et "
    "les lingettes finissent invariablement dans les WC. Une colonne qui reçoit les "
    "rejets de huit logements ne pardonne pas ce qu'une maison individuelle encaisse "
    "sans broncher.",
    "Sur le secteur de Saint-Malo, l'enjeu se déplace vers les réseaux de bord de "
    "mer&nbsp;: forte fréquentation saisonnière, réseaux anciens en centre historique et "
    "épisodes pluvieux qui saturent ponctuellement les collecteurs."],
   None),
  ("Ce qu'une intervention sur colonne implique vraiment",
   [],
   ["Un accès en pied de colonne, souvent en sous-sol ou dans un local technique&nbsp;: "
    "prévoir la clé auprès du gardien ou du syndic.",
    "Un hydrocurage par le bas, qui décolle le dépôt sur toute la hauteur plutôt que "
    "de percer un simple passage.",
    "Une inspection caméra quand la colonne se rebouche à intervalles réguliers&nbsp;: "
    "elle distingue l'encrassement de la casse.",
    "L'information des occupants pendant l'intervention&nbsp;: aucun rejet dans la "
    "colonne tant que le technicien travaille dessous.",
    "Un rapport écrit destiné au syndic, indispensable pour la répartition des charges "
    "et pour l'assurance si des logements ont été touchés."],
   ),
 ],
 "faq": [
  ("Le syndic est injoignable la nuit, que faire&nbsp;?",
   "Si le dommage s'aggrave — l'eau continue de monter, d'autres logements sont "
   "menacés — vous pouvez faire intervenir à titre conservatoire. Conservez tout&nbsp;: "
   "heure des appels passés au syndic, photos horodatées, rapport d'intervention. La "
   "prise en charge se discute ensuite sur pièces, et un dossier documenté change tout."),
  ("Qui paie le débouchage d'une colonne&nbsp;?",
   "La colonne verticale desservant plusieurs logements est une partie commune&nbsp;: "
   "son entretien relève de la copropriété, donc des charges. Seule l'évacuation "
   "privative qui relie votre appareil à la colonne est à votre charge. C'est la raison "
   "pour laquelle il faut identifier la nature du bouchon avant de payer quoi que ce soit."),
  ("Mon assurance couvre-t-elle les dégâts causés par un refoulement&nbsp;?",
   "Les dommages aux biens consécutifs à un refoulement d'eaux usées sont généralement "
   "couverts par les contrats multirisque habitation, avec des modalités qui varient "
   "d'un contrat à l'autre. Déclarez rapidement, joignez les photos et le rapport "
   "d'intervention, et laissez votre assureur se rapprocher de celui de la copropriété."),
  ("Intervenez-vous pour les syndics et les bailleurs rennais&nbsp;?",
   "Oui, sur mandat, en urgence comme en entretien programmé. Nous fournissons le "
   "rapport d'intervention et, lorsque l'inspection caméra est réalisée, l'état du "
   "réseau par écrit — les deux pièces que réclament les conseils syndicaux."),
 ],
},

{
 "slug": "degat-des-eaux-venant-du-voisin-ille-et-vilaine",
 "court": "Dégât des eaux du voisin (35)",
 "dept": "35", "act": "plomberie", "date": "2026-09-30",
 "titre": 'Dégât des eaux du voisin (35) : que faire vite — ETS-BZH',
 "h1": 'Dégât des eaux venant du voisin en Ille-et-Vilaine&nbsp;: les gestes des deux premières heures',
 "meta": "De l'eau coule chez vous depuis le logement du dessus en Ille-et-Vilaine : l'ordre des gestes et les preuves à réunir. Urgence au 02 20 06 00 75.",
 "mots_cles": ("dégât des eaux voisin, fuite plafond appartement Rennes, constat "
               "amiable dégât des eaux, recherche de fuite Ille-et-Vilaine"),
 "chapo": ("Une auréole qui s'étend au plafond, un goutte-à-goutte qui devient filet, "
           "et personne ne répond à l'étage du dessus. Ce qui se joue dans les deux "
           "premières heures ne détermine pas seulement l'ampleur des dégâts&nbsp;: cela "
           "détermine aussi ce que votre assurance acceptera de prendre en charge."),
 "urgent": [
   "Coupez l'électricité de la pièce touchée avant d'y manipuler quoi que ce soit&nbsp;: "
   "l'eau au plafond atteint souvent les points lumineux en premier.",
   "Dégagez et surélevez ce qui peut l'être, et posez un récipient plutôt que de "
   "laisser l'eau se répandre.",
   "Montez prévenir le voisin. S'il est absent, prévenez le syndic ou le "
   "gardien&nbsp;: eux seuls peuvent faire ouvrir un logement en cas d'urgence.",
   "Photographiez tout, largement, avec l'heure&nbsp;: plafond, murs, sol, mobilier, et "
   "même ce qui n'est pas encore abîmé.",
   "Ne repeignez rien, ne jetez rien et ne faites aucune réparation définitive avant "
   "le passage de l'expert.",
 ],
 "danger": ("Une poche d'eau qui gonfle dans un plafond en plaque de plâtre finit par "
            "céder d'un coup, avec plusieurs dizaines de litres. Si vous voyez un "
            "bombement, évacuez la zone, ne restez pas dessous, et laissez un "
            "professionnel percer le point bas de façon contrôlée."),
 "sections": [
  ("La chronologie qui protège vos droits",
   ["Un dégât des eaux se règle sur pièces. Ce que vous aurez documenté dans les deux "
    "premières heures pèsera plus que tout ce que vous direz ensuite.",
    "Première heure&nbsp;: sécuriser et limiter. Couper l'électricité, protéger les "
    "biens, prévenir le voisin, le syndic ou le gardien. Si l'origine est identifiée et "
    "accessible, couper l'arrivée d'eau concernée.",
    "Deuxième heure&nbsp;: documenter. Photos horodatées, vue d'ensemble et détails, "
    "liste des biens touchés, et le constat amiable dégât des eaux rempli avec le voisin "
    "si le contact est établi. Ce document contradictoire, signé des deux parties, est "
    "ce qui évite des mois de discussion entre assureurs.",
    "Ensuite&nbsp;: déclarer à votre assureur, dans le délai prévu par votre contrat — "
    "généralement cinq jours ouvrés. Déclarez même si vous pensez être uniquement "
    "victime&nbsp;: c'est votre propre assureur qui pilote votre indemnisation."],
   None),
  ("« Ça vient du dessus » n'est pas toujours vrai",
   ["L'eau suit les pentes, les gaines et les dalles&nbsp;: elle ressort rarement à "
    "l'aplomb de son origine. Nous voyons régulièrement des fuites attribuées au voisin "
    "du dessus alors qu'elles proviennent d'une colonne encastrée, d'une canalisation "
    "encastrée dans la dalle, ou d'une infiltration par une façade ou une terrasse.",
    "C'est précisément l'objet de la recherche de fuite non destructive&nbsp;: localiser "
    "l'origine réelle sans casser. Selon les cas, nous utilisons la caméra thermique, "
    "qui révèle les différences de température derrière les parois, le gaz traceur, qui "
    "remonte par le point de fuite, ou la mise en pression du circuit pour isoler la "
    "portion en cause.",
    "Le rapport qui en résulte sert à deux choses&nbsp;: réparer au bon endroit, et "
    "établir la responsabilité. Sans lui, deux assureurs se renvoient le dossier, et "
    "c'est l'occupant qui attend."],
   None),
  ("Ille-et-Vilaine : un parc collectif qui multiplie les cas",
   ["Rennes métropole concentre une densité d'appartements et de copropriétés sans "
    "équivalent en Bretagne, et le dégât des eaux entre voisins y est, de loin, le "
    "sinistre le plus courant. Les immeubles intra-rocade des années soixante et "
    "soixante-dix cumulent deux facteurs&nbsp;: des canalisations encastrées dans les "
    "dalles, difficiles à atteindre, et des salles de bain superposées sur toute la "
    "hauteur du bâtiment.",
    "Le bassin locatif ajoute une contrainte de calendrier&nbsp;: entre un locataire, un "
    "propriétaire souvent non résident, un syndic et deux assureurs, les décisions "
    "prennent du temps — pendant que l'eau, elle, n'attend pas. D'où l'intérêt de "
    "séparer nettement les deux sujets&nbsp;: l'intervention technique d'abord, la "
    "répartition des responsabilités ensuite, sur la base d'un rapport écrit.",
    "Sur le littoral malouin, la configuration change&nbsp;: bâti ancien en pierre, "
    "infiltrations par les façades exposées et résidences occupées par intermittence, où "
    "une fuite peut couler plusieurs jours avant d'être découverte."],
   None),
  ("Les erreurs qui coûtent cher",
   [],
   ["Réparer et repeindre avant le passage de l'expert&nbsp;: les dégâts ne sont plus "
    "constatables, et l'indemnisation s'en ressent.",
    "Jeter les biens abîmés sans les avoir photographiés ni conservés.",
    "Attendre que le voisin « règle ça » sans déclarer à son propre assureur.",
    "Casser un plafond ou une cloison pour chercher la fuite&nbsp;: la recherche non "
    "destructive coûte presque toujours moins cher que la remise en état de ce qu'on a "
    "ouvert au hasard.",
    "Négliger l'assèchement&nbsp;: une cloison qui garde l'humidité fait apparaître des "
    "moisissures des semaines après, et ce second sinistre se discute mal."],
   ),
 ],
 "faq": [
  ("Qui paie la recherche de fuite&nbsp;?",
   "Elle est fréquemment prise en charge par l'assurance dans le cadre d'un dégât des "
   "eaux, selon les garanties du contrat. Avant d'engager la recherche, un appel à votre "
   "assureur permet de vérifier la couverture et d'éviter une avance inutile. Nous "
   "fournissons dans tous les cas un rapport exploitable par l'expert."),
  ("Le voisin refuse de signer le constat amiable, que faire&nbsp;?",
   "Déclarez seul à votre assureur, en indiquant précisément la date, l'heure, "
   "l'origine présumée, les démarches entreprises et les refus opposés. Un constat "
   "signé des deux parties accélère le traitement, mais son absence ne bloque pas votre "
   "indemnisation&nbsp;: les assureurs se rapprochent alors directement."),
  ("Combien de temps avant de pouvoir refaire les peintures&nbsp;?",
   "Il faut que le support soit sec, ce qui prend souvent plusieurs semaines sur une "
   "cloison ou une dalle imprégnée, et il faut que l'expert soit passé. Repeindre trop "
   "tôt fait cloquer la peinture et peut compromettre l'indemnisation."),
  ("Intervenez-vous en urgence la nuit sur Rennes&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur l'ensemble de l'Ille-et-Vilaine. En pleine nuit, l'objectif "
   "est d'abord d'arrêter l'écoulement et de sécuriser&nbsp;; la recherche de fuite fine "
   "et la réparation définitive se programment ensuite, dans de meilleures conditions."),
 ],
},

# ================================================================ 56 — MORBIHAN
{
 "slug": "chauffe-eau-qui-fuit-morbihan",
 "court": "Chauffe-eau qui fuit (56)",
 "dept": "56", "act": "plomberie", "date": "2026-09-30",
 "titre": 'Chauffe-eau qui fuit (56) : réparer ou changer — ETS-BZH',
 "h1": 'Chauffe-eau qui fuit dans le Morbihan&nbsp;: couper, limiter les dégâts, et ce qui se répare vraiment',
 "meta": 'Chauffe-eau qui fuit dans le Morbihan : 4 points de fuite, 4 verdicts. Savoir si cela se répare avant de payer un appareil neuf. 02 20 06 00 75.',
 "mots_cles": ("chauffe-eau qui fuit, ballon d'eau chaude fuite Vannes, groupe de "
               "sécurité qui coule, remplacement chauffe-eau Morbihan, plombier Lorient"),
 "chapo": ("Un chauffe-eau qui goutte n'est pas forcément un chauffe-eau à "
           "remplacer&nbsp;: tout dépend de l'endroit d'où vient l'eau. Une fuite au "
           "groupe de sécurité est bénigne et se répare en une demi-heure&nbsp;; une "
           "cuve percée ne se répare pas. Savoir faire la différence vous évite de payer "
           "un appareil neuf pour une pièce à trente euros — ou d'attendre trop "
           "longtemps avec deux cents litres au-dessus de la tête."),
 "urgent": [
   "Coupez l'alimentation électrique du chauffe-eau au tableau, pas seulement "
   "l'interrupteur de l'appareil.",
   "Fermez l'arrivée d'eau froide du ballon&nbsp;: c'est la vanne située juste avant le "
   "groupe de sécurité, en bas de l'appareil.",
   "Placez un récipient et épongez&nbsp;: un ballon de deux cents litres qui se vide "
   "traverse un plancher.",
   "Regardez précisément d'où vient l'eau — groupe de sécurité, raccord, ou "
   "dessous de la cuve. C'est la seule information qui compte pour la suite.",
   "Si vous êtes en appartement ou à l'étage, prévenez le voisin du dessous&nbsp;: "
   "mieux vaut le prévenir que le découvrir.",
 ],
 "danger": ("Ne bouchez jamais l'écoulement du groupe de sécurité et ne le remplacez "
            "pas par un bouchon pour « arrêter la fuite ». Ce petit organe est la "
            "soupape qui évacue la surpression quand l'eau chauffe. Neutralisé, il "
            "transforme le ballon en récipient sous pression — avec un risque "
            "d'éclatement parfaitement réel."),
 "sections": [
  ("Quatre points de fuite, quatre verdicts",
   ["Avant tout devis, il faut savoir d'où l'eau sort. Quatre cas couvrent la quasi-"
    "totalité des situations.",
    "<strong>Un goutte-à-goutte au groupe de sécurité pendant la chauffe.</strong> Ce "
    "n'est pas une panne&nbsp;: c'est le fonctionnement normal. L'eau se dilate en "
    "chauffant et le surplus est évacué. Le volume attendu est de l'ordre de quelques "
    "pour cent du volume du ballon sur un cycle. Si c'est bien plus, ou si cela coule en "
    "continu, le groupe est entartré ou fatigué — pièce peu coûteuse, remplacement rapide.",
    "<strong>Une fuite aux raccords, en haut ou en bas de l'appareil.</strong> Joint "
    "durci, écrou desserré, flexible fendu. Réparation simple, appareil conservé.",
    "<strong>Une fuite au niveau de la trappe de visite ou de la bride.</strong> Le "
    "joint de bride est en cause. Cela se remplace, mais c'est aussi le moment de "
    "vérifier l'anode et l'état intérieur de la cuve&nbsp;: sur un appareil âgé, la "
    "question du remplacement se pose honnêtement.",
    "<strong>De l'eau qui suinte sous la cuve, sans raccord en cause.</strong> La cuve "
    "est percée par corrosion. Il n'y a pas de réparation possible, et il n'y en a "
    "jamais eu&nbsp;: l'appareil doit être remplacé. Méfiez-vous de quiconque vous "
    "propose de « souder »."],
   None),
  ("Faire durer un chauffe-eau plus longtemps",
   ["L'eau distribuée sur une grande partie du Morbihan est peu calcaire&nbsp;: le "
    "sous-sol granitique donne une eau douce, ce qui épargne les résistances et les "
    "robinetteries. L'avantage a son revers&nbsp;: une eau douce est plus agressive pour "
    "les métaux, et c'est l'anode — cette tige sacrificielle qui se consume à la place "
    "de la cuve — qui encaisse.",
    "Une anode épuisée et personne ne le sait&nbsp;: la cuve se corrode en silence "
    "pendant deux ou trois ans, puis perce d'un coup. C'est pour cela qu'un contrôle "
    "tous les deux ans, avec vérification de l'anode et du groupe de sécurité, prolonge "
    "réellement la durée de vie de l'appareil.",
    "Deux réflexes simples complètent cela&nbsp;: manœuvrer le robinet du groupe de "
    "sécurité une fois par mois pour éviter qu'il ne se bloque, et régler la "
    "température autour de 55 à 60&nbsp;°C — assez chaud pour la sécurité sanitaire, "
    "assez modéré pour limiter la corrosion et l'entartrage."],
   None),
  ("Locations saisonnières : le scénario morbihannais",
   ["Du golfe du Morbihan à Quiberon, une part importante du parc est louée à la "
    "saison. Le chauffe-eau y subit un régime particulier&nbsp;: sollicité fortement "
    "pendant huit semaines, puis laissé sous tension et sous pression pendant dix mois "
    "sans soutirage.",
    "C'est le pire des cycles pour une cuve. L'eau stagnante accélère la corrosion, le "
    "groupe de sécurité se bloque faute d'être manœuvré, et la fuite se déclare "
    "typiquement à la première remise en service de la saison — ou pire, en plein hiver, "
    "dans une maison vide.",
    "La consigne que nous donnons aux propriétaires de location est courte&nbsp;: à la "
    "fermeture de saison, coupez l'électricité du ballon et fermez l'arrivée d'eau. Si "
    "le logement reste vide tout l'hiver, vidangez. À la réouverture, remplissez avant "
    "de remettre le courant&nbsp;: une résistance alimentée à vide grille en quelques "
    "minutes."],
   None),
  ("Réparer ou remplacer : les critères honnêtes",
   [],
   ["Fuite au groupe de sécurité ou à un raccord&nbsp;: on répare, quel que soit l'âge "
    "de l'appareil.",
    "Fuite au joint de bride sur un appareil de moins de huit ans&nbsp;: on répare et on "
    "contrôle l'anode.",
    "Cuve percée&nbsp;: on remplace, il n'existe aucune réparation durable.",
    "Plus d'eau chaude sans fuite&nbsp;: c'est souvent la résistance ou le thermostat, "
    "et cela se répare — inutile de changer l'appareil.",
    "Appareil de plus de quinze ans avec panne lourde&nbsp;: le remplacement se discute, "
    "chiffres en main, sans que personne ne décide à votre place."],
   ),
 ],
 "faq": [
  ("Mon groupe de sécurité goutte en permanence, est-ce normal&nbsp;?",
   "Un écoulement pendant la phase de chauffe est normal. Un écoulement continu, y "
   "compris quand le ballon ne chauffe pas, ne l'est pas&nbsp;: le groupe est entartré ou "
   "sa soupape ne referme plus. La pièce est peu coûteuse et le remplacement rapide — ne "
   "le bouchez surtout pas en attendant."),
  ("Combien de temps sans eau chaude après une panne&nbsp;?",
   "Si la pièce en cause est courante — groupe de sécurité, thermostat, résistance — "
   "nos véhicules l'ont à bord et l'eau chaude revient dans la journée. Un remplacement "
   "complet d'appareil demande en général une demi-journée, une fois le modèle choisi."),
  ("Une cuve percée peut-elle vraiment être réparée&nbsp;?",
   "Non. La corrosion qui a percé un point a fragilisé l'ensemble de la paroi&nbsp;: "
   "toute réparation ne fait que déplacer la prochaine fuite de quelques semaines. "
   "L'appareil doit être remplacé, et c'est ce que nous vous dirons."),
  ("Intervenez-vous sur les chauffe-eau de toutes marques dans le Morbihan&nbsp;?",
   "Oui, sur l'ensemble du département, de Vannes à Lorient en passant par Pontivy et "
   "Auray. Le diagnostic et le devis sont gratuits, et le tarif est validé avec vous "
   "avant tout démarrage."),
 ],
},

{
 "slug": "odeur-de-brule-tableau-electrique-morbihan",
 "court": "Odeur de brûlé au tableau (56)",
 "dept": "56", "act": "electricite", "date": "2026-09-30",
 "titre": 'Odeur de brûlé au tableau (56) : que faire — ETS-BZH',
 "h1": "Odeur de brûlé au tableau électrique dans le Morbihan&nbsp;: ce qu'il faut faire dans les cinq minutes",
 "meta": "Odeur de brûlé, prise qui chauffe ou tableau qui grésille dans le Morbihan : les gestes des 5 premières minutes. Électricien d'urgence au 02 20 06 00 75.",
 "mots_cles": ("odeur de brûlé tableau électrique, prise qui chauffe, électricien "
               "urgence Vannes, risque incendie électrique Morbihan, tableau qui grésille"),
 "chapo": ("Une odeur de plastique chaud près du tableau, une prise tiède, un "
           "grésillement discret&nbsp;: ce sont les seuls avertissements que donne un "
           "défaut électrique avant l'incendie, et ils ne durent pas. Voici quoi faire "
           "dans les cinq minutes, et ce qui se cache réellement derrière ces signes."),
 "urgent": [
   "Coupez le disjoncteur général — le gros, près du compteur. Pas seulement le "
   "circuit suspect&nbsp;: tant que l'origine n'est pas identifiée, on coupe tout.",
   "Ne touchez pas au tableau, ne démontez rien, ne débranchez pas à main nue un "
   "appareil dont la prise est chaude.",
   "N'utilisez jamais d'eau sur un départ de feu électrique. Si le feu a pris, "
   "sortez, fermez la porte et appelez les secours au 18 ou au 112.",
   "Aérez, et laissez le courant coupé&nbsp;: l'inconfort d'une soirée sans électricité "
   "n'est rien comparé au risque.",
   "Appelez. Une odeur de brûlé au tableau fait partie des rares situations qui "
   "justifient un déplacement de nuit.",
 ],
 "danger": ("Une odeur de brûlé n'est jamais un faux signal. Ce que vous sentez, ce "
            "sont des isolants qui se dégradent sous l'effet de la chaleur, c'est-à-dire "
            "un échauffement déjà avancé. Un point chaud dans un tableau peut passer de "
            "l'odeur à la flamme en quelques heures. Aucune de ces situations ne peut "
            "attendre le lendemain matin."),
 "sections": [
  ("Ce qui chauffe réellement, et pourquoi",
   ["Dans la quasi-totalité des cas, l'échauffement ne vient pas d'un appareil "
    "défectueux mais d'un contact qui ne serre plus assez. Un conducteur mal serré sur "
    "une borne présente une résistance de contact&nbsp;: le courant y dissipe de la "
    "chaleur, la chaleur dilate le métal, le serrage se relâche encore, et le phénomène "
    "s'emballe tout seul.",
    "Les endroits où cela se produit sont toujours les mêmes&nbsp;: les bornes du "
    "tableau, les prises sur lesquelles sont branchés des appareils de forte puissance "
    "— sèche-linge, plaque, chauffage d'appoint, borne de recharge — et les vieilles "
    "boîtes de dérivation à dominos, dans les combles ou derrière une cloison.",
    "Deux autres causes reviennent régulièrement&nbsp;: les multiprises en cascade, qui "
    "font passer par une seule prise le courant de plusieurs appareils, et les rallonges "
    "enroulées sur elles-mêmes, qui ne dissipent plus la chaleur qu'elles produisent.",
    "Un détail qui trompe souvent&nbsp;: un disjoncteur ne protège pas contre un mauvais "
    "contact. Il coupe sur une surintensité ou un défaut d'isolement, pas sur un point "
    "chaud. C'est pourquoi une installation peut brûler sans que rien ne saute."],
   None),
  ("Les signes à ne jamais ignorer",
   ["Certains symptômes sont des alertes tardives et demandent une coupure immédiate, "
    "d'autres sont des alertes précoces et demandent un contrôle rapide.",
    "<strong>Coupez tout de suite</strong> si vous constatez&nbsp;: une odeur de "
    "plastique chaud ou de brûlé, une trace noire ou un jaunissement autour d'une prise "
    "ou d'un interrupteur, un grésillement ou un claquement dans le tableau, une prise "
    "ou une fiche trop chaude pour être tenue en main, de la fumée, même fugace.",
    "<strong>Faites contrôler rapidement</strong> si vous constatez&nbsp;: des lumières "
    "qui faiblissent à chaque démarrage d'un appareil, un disjoncteur qui saute de plus "
    "en plus souvent sans raison apparente, une prise devenue lâche, un tableau "
    "sensiblement tiède au toucher, ou un tableau encore équipé de fusibles à broche.",
    "Une remarque sur les installations anciennes&nbsp;: l'absence de protection "
    "différentielle 30&nbsp;mA ne provoque pas l'échauffement, mais elle supprime le "
    "filet de sécurité au moment où le défaut survient. C'est ce cumul qui rend les "
    "installations non rénovées réellement dangereuses."],
   None),
  ("Morbihan : pics d'usage et installations de bord de mer",
   ["Le département cumule deux facteurs que nous retrouvons intervention après "
    "intervention. D'abord la saisonnalité&nbsp;: du golfe à Quiberon, des logements "
    "conçus pour un usage modéré reçoivent en été plusieurs occupants supplémentaires, "
    "avec chauffe-eau sollicité en continu, plaques de cuisson, climatiseurs mobiles et "
    "rallonges partout. Une installation qui tenait sans broncher se retrouve chargée "
    "près de sa limite pendant des semaines.",
    "Ensuite l'air marin. Sur le littoral, le sel et l'humidité s'attaquent aux "
    "contacts et aux bornes, y compris à l'intérieur des logements des premières lignes. "
    "Les coffrets de comptage extérieurs, les tableaux installés en garage ou en "
    "buanderie et les prises de terrasse sont les premiers concernés.",
    "À cela s'ajoutent les extensions successives&nbsp;: une véranda, un abri de jardin, "
    "un portail motorisé, une borne de recharge ajoutée sur un circuit qui n'était pas "
    "prévu pour. Chaque ajout est un raccordement de plus, donc un point de contact de "
    "plus."],
   None),
  ("Ce que nous contrôlons quand nous arrivons",
   [],
   ["Contrôle du tableau sous tension, y compris la recherche des points chauds sur les "
    "bornes.",
    "Reprise du serrage de l'ensemble des connexions — c'est souvent tout ce qui "
    "manquait.",
    "Remplacement des appareillages dégradés&nbsp;: prise noircie, porte-fusible fondu, "
    "disjoncteur fatigué.",
    "Vérification de la protection différentielle et de la prise de terre.",
    "Contrôle des circuits dédiés aux appareils de forte puissance, et de leur "
    "adéquation avec ce qui y est réellement branché.",
    "Remise sous tension progressive en votre présence, et rapport écrit de ce qui a "
    "été constaté."],
   ),
 ],
 "faq": [
  ("Je ne sens plus l'odeur, puis-je remettre le courant&nbsp;?",
   "Non. L'odeur disparaît dès que l'échauffement cesse, c'est-à-dire dès que le "
   "courant est coupé&nbsp;: sa disparition ne prouve rien du tout. Le défaut, lui, est "
   "toujours là et reprendra à la remise sous tension. Le contrôle doit être fait avant."),
  ("Une prise qui chauffe, est-ce vraiment grave&nbsp;?",
   "Oui. Une prise tiède signale déjà un mauvais contact, et une prise trop chaude pour "
   "être tenue est à quelques étapes de la carbonisation de son support. Cessez de "
   "l'utiliser, coupez le circuit correspondant, et faites-la remplacer&nbsp;: c'est une "
   "intervention courte."),
  ("Mon assurance couvre-t-elle un incendie d'origine électrique&nbsp;?",
   "Les contrats multirisque habitation couvrent l'incendie, mais un assureur peut "
   "examiner l'état de l'installation et l'existence d'un entretien. Conserver les "
   "rapports d'intervention et les factures de mise en sécurité est toujours dans votre "
   "intérêt."),
  ("Intervenez-vous la nuit dans le Morbihan pour ce type d'urgence&nbsp;?",
   "Oui. Une odeur de brûlé, un tableau qui grésille ou une prise qui a noirci font "
   "partie des situations que nous traitons en astreinte, 24h/24 et 7j/7, de Vannes à "
   "Lorient et sur l'ensemble du département. Le délai est annoncé dès l'appel."),
 ],
},

]
