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

# ------------------------------------------------- 22 — CÔTES-D'ARMOR (suite)
{
 "slug": "wc-bouche-que-faire-cotes-d-armor",
 "court": "WC bouché (22)",
 "dept": "22", "act": "degorgement", "date": "2026-09-30",
 "titre": "WC bouché (22) : les gestes avant le dépanneur — ETS-BZH",
 "h1": "WC bouché dans les Côtes-d'Armor&nbsp;: les gestes qui marchent, et ceux qui aggravent",
 "meta": ("WC bouché dans les Côtes-d'Armor : la ventouse bien utilisée, ce qu'il ne "
          "faut jamais verser, et quand appeler. Débouchage 7j/7 au 02 20 06 00 75."),
 "mots_cles": ("WC bouché que faire, débouchage WC Saint-Brieuc, ventouse WC, "
               "déboucheur chimique danger, plombier urgence Côtes-d'Armor"),
 "chapo": ("La cuvette est pleine, le niveau ne descend pas, et la tentation est de "
           "tirer la chasse « pour voir ». C'est précisément ce qui transforme un "
           "bouchon en inondation. Voici l'ordre des gestes, celui qui fonctionne dans "
           "la majorité des cas, et le moment où insister devient contre-productif."),
 "urgent": [
   "Ne retirez pas la chasse une seconde fois&nbsp;: la cuvette déborderait.",
   "Écopez jusqu'à mi-hauteur avec un récipient&nbsp;: la ventouse a besoin d'eau, "
   "mais pas d'une cuvette pleine.",
   "Bouchez le trop-plein s'il y en a un, et posez une serviette au sol.",
   "Ventouse à cloche, bien à plat sur l'évacuation&nbsp;: une quinzaine de "
   "mouvements francs, sans décoller le bord.",
   "Si rien ne bouge après deux séries, arrêtez. Au-delà, on tasse le bouchon.",
 ],
 "danger": ("Ne versez jamais de déboucheur chimique dans une cuvette qui ne "
            "s'évacue pas. Le produit stagne, il ne descend pas jusqu'au bouchon, et il "
            "reste là&nbsp;: au moment du débouchage mécanique, les projections de soude "
            "brûlent la peau et les yeux. Sur une évacuation ancienne en fonte, "
            "certaines formules attaquent en plus le métal. Et si la maison est sur "
            "fosse septique, le produit détruit les bactéries qui la font fonctionner."),
 "sections": [
  ("Ce que le comportement du bouchon vous apprend",
   ["Un WC ne se bouche pas de la même manière selon ce qui l'obstrue, et le "
    "diagnostic se lit à l'œil.",
    "<strong>Le niveau descend très lentement puis se vide.</strong> Le passage est "
    "réduit, pas fermé&nbsp;: dépôt de calcaire ou de papier accumulé. La ventouse ou un "
    "furet court suffisent presque toujours.",
    "<strong>Le niveau ne bouge pas du tout.</strong> Le bouchon est compact et proche "
    "— lingette, bloc désodorisant tombé, objet. La ventouse échoue souvent, le furet "
    "électrique règle la situation en quelques minutes.",
    "<strong>Ça bouchonne et ça remonte ailleurs.</strong> Si la douche ou l'évier "
    "gargouillent quand vous tirez la chasse, le bouchon n'est plus dans le WC&nbsp;: il "
    "est sur l'évacuation commune, en aval. Inutile d'insister sur la cuvette.",
    "Ce dernier cas est le plus fréquent dans les maisons de bourg costarmoricaines où "
    "les évacuations d'étage se rejoignent tôt&nbsp;: le WC n'est que le premier appareil "
    "à manifester le problème."],
   None),
  ("Pourquoi les lingettes reviennent dans presque chaque intervention",
   ["Le mot « biodégradable » imprimé sur un paquet de lingettes décrit une "
    "dégradation en station d'épuration, dans des conditions et sur une durée qui n'ont "
    "rien à voir avec un coude d'évacuation. Dans une canalisation, la lingette garde sa "
    "trame, s'accroche à la moindre aspérité et capte tout ce qui passe ensuite.",
    "Le même raisonnement vaut pour le papier essuie-tout, les cotons, le fil dentaire "
    "et la litière dite « jetable dans les WC ». Dans les communes de l'arrière-pays où "
    "l'assainissement est individuel, le problème est double&nbsp;: ce qui ne bouche pas "
    "la canalisation finit dans la fosse, qu'il faut alors vidanger plus souvent.",
    "Un cas revient chaque été sur le littoral&nbsp;: la location de vacances. Les "
    "occupants changent toutes les semaines, personne ne connaît les habitudes de la "
    "maison, et le bouchon se déclare un dimanche soir. C'est la seule prévention qui "
    "marche vraiment&nbsp;: une consigne affichée près des WC."],
   None),
  ("Quand il faut arrêter d'essayer",
   [],
   ["Deux séries de ventouse sans aucun résultat&nbsp;: insister tasse le bouchon.",
    "Un autre appareil gargouille ou refoule&nbsp;: le problème est en aval, pas dans "
    "la cuvette.",
    "Un objet est tombé dans la cuvette&nbsp;: le pousser au furet l'enfoncera plus loin.",
    "Le WC est un broyeur&nbsp;: la ventouse ne sert à rien et le démontage demande de "
    "l'outillage.",
    "L'eau remonte en même temps dans plusieurs logements&nbsp;: c'est une colonne, donc "
    "une affaire collective.",
    "La maison est sur fosse et plusieurs appareils sont lents&nbsp;: contrôlez la fosse "
    "avant de forcer sur les évacuations."],
   ),
 ],
 "faq": [
  ("La ventouse ne marche pas, puis-je utiliser un cintre&nbsp;?",
   "Mieux vaut éviter. Un fil de fer rigide raye l'émail et, surtout, il pousse le "
   "bouchon au lieu de le ramener. Un furet à tête souple est fait pour cela&nbsp;: il "
   "épouse le siphon sans l'abîmer. Un furet électrique va plus loin, jusqu'au collecteur."),
  ("Combien coûte un débouchage de WC&nbsp;?",
   "Nos tarifs indicatifs commencent à 129 € TTC pour un débouchage simple. Le prix "
   "exact est annoncé après diagnostic et validé avec vous avant le démarrage&nbsp;: la "
   "facture ne dépasse jamais le devis accepté."),
  ("Je suis locataire, qui paie&nbsp;?",
   "L'usage veut que le débouchage courant relève de l'entretien, donc du locataire, et "
   "que la réparation d'une canalisation dégradée ou affaissée revienne au propriétaire. "
   "Si le bouchon révèle un défaut du réseau, notre diagnostic écrit fait la preuve."),
  ("Intervenez-vous la nuit dans les Côtes-d'Armor&nbsp;?",
   "Oui, 24h/24 et 7j/7. Un WC bouché dans un logement qui n'en a qu'un seul fait "
   "partie des situations que nous traitons en astreinte. Le délai est annoncé dès "
   "l'appel."),
 ],
},

{
 "slug": "cave-inondee-apres-orage-cotes-d-armor",
 "court": "Cave inondée (22)",
 "dept": "22", "act": "degorgement", "date": "2026-09-30",
 "titre": "Cave inondée après un orage (22) : que faire — ETS-BZH",
 "h1": "Cave ou sous-sol inondé dans les Côtes-d'Armor&nbsp;: pomper, mais dans le bon ordre",
 "meta": ("Cave inondée après un orage dans les Côtes-d'Armor : couper l'électricité, "
          "pomper sans aggraver, et trouver l'origine. Pompage 7j/7 au 02 20 06 00 75."),
 "mots_cles": ("cave inondée que faire, pompage cave Saint-Brieuc, sous-sol inondé "
               "orage, remontée de nappe Côtes-d'Armor, pompe vide-cave"),
 "chapo": ("Vingt centimètres d'eau dans le sous-sol après une nuit d'orage, et le "
           "réflexe est de pomper tout de suite. Ce n'est pas toujours le bon&nbsp;: mal "
           "conduit, un pompage rapide peut fissurer un dallage ou faire remonter l'eau "
           "aussi vite qu'on la sort. Voici l'ordre qui protège la maison."),
 "urgent": [
   "Coupez l'électricité du sous-sol au tableau avant d'y descendre. N'entrez "
   "jamais dans une pièce inondée sans avoir coupé.",
   "Ne descendez pas pieds nus et n'utilisez aucun appareil branché restant dans "
   "l'eau.",
   "Photographiez avant de toucher à quoi que ce soit&nbsp;: niveau atteint, biens "
   "touchés, heure.",
   "Surélevez ce qui peut l'être, à commencer par ce qui craint l'humidité durable.",
   "Si l'eau continue de monter alors que la pluie a cessé, ce n'est pas un "
   "ruissellement&nbsp;: appelez.",
 ],
 "danger": ("Ne vidangez pas une cave inondée d'un seul coup quand l'eau vient d'une "
            "nappe remontée. La pression de l'eau extérieure équilibre celle de "
            "l'intérieur&nbsp;: en supprimant l'une brutalement, on expose le dallage et "
            "les murs enterrés à une poussée qu'ils n'ont pas à encaisser seuls. Dans ce "
            "cas, on abaisse par paliers."),
 "sections": [
  ("Trois origines, trois traitements",
   ["Avant de pomper, il faut savoir d'où vient l'eau, parce que la réponse n'est pas "
    "la même.",
    "<strong>Le ruissellement de surface.</strong> L'eau est entrée par un soupirail, "
    "une rampe de garage ou une porte. Elle est souvent chargée de terre. Le pompage "
    "règle le problème, et la prévention est extérieure&nbsp;: seuil, caniveau, "
    "relèvement du soupirail.",
    "<strong>Le refoulement du réseau.</strong> L'eau qui monte est sale et sent "
    "l'égout, elle sort par le siphon de sol ou la bonde. Le réseau est saturé et "
    "refoule chez vous parce que vous êtes le point bas. Le pompage ne suffit pas&nbsp;: "
    "seul un clapet anti-retour empêche la récidive.",
    "<strong>La remontée de nappe.</strong> L'eau est claire, elle suinte par le "
    "dallage et les joints, et elle continue de monter après la pluie. C'est le cas le "
    "plus courant en hiver dans l'arrière-pays, sur des sols schisteux qui drainent "
    "mal. On abaisse par paliers et on envisage un drainage ou une pompe de relevage "
    "permanente."],
   None),
  ("Le pompage, puis l'assèchement — les deux comptent",
   ["Sortir l'eau ne termine pas le chantier. Une cave enterrée qui a pris vingt "
    "centimètres reste saturée d'humidité pendant des semaines, et c'est là que se "
    "jouent les dégâts durables&nbsp;: salpêtre sur les murs, moisissures, décollement "
    "des enduits, odeur qui monte dans la maison.",
    "Après pompage, nous rinçons ce qui a été en contact avec des eaux usées, nous "
    "dégageons les évacuations obstruées par les boues, et nous vérifions que le siphon "
    "de sol fonctionne dans le bon sens. La ventilation fait ensuite l'essentiel du "
    "travail&nbsp;: portes ouvertes, air en mouvement, et patience.",
    "Sur les communes littorales, entre Paimpol, Erquy et Saint-Cast, s'ajoute un "
    "facteur qu'on oublie&nbsp;: à marée haute, le réseau évacue moins bien. Un "
    "refoulement qui se produit toujours aux mêmes heures n'est pas une coïncidence."],
   None),
  ("Ce qui se met en place pour que cela ne recommence pas",
   [],
   ["Un clapet anti-retour sur le branchement quand l'eau vient du réseau.",
    "Une pompe de relevage avec flotteur et alarme dans un puisard, sur les maisons "
    "régulièrement touchées.",
    "Le nettoyage des regards et des descentes d'eaux pluviales avant l'automne.",
    "Un caniveau et un seuil relevé devant une rampe de garage.",
    "L'éloignement des rejets de gouttière&nbsp;: un exutoire au pied du mur alimente "
    "directement la nappe sous la maison.",
    "Un tableau électrique jamais installé en sous-sol inondable&nbsp;: c'est la "
    "première chose que l'eau atteint."],
   ),
 ],
 "faq": [
  ("Ma pompe vide-cave suffit-elle&nbsp;?",
   "Pour quelques centimètres d'eau claire, oui. Elle atteint vite ses limites sur une "
   "eau chargée de boue ou de gravats, qui bloque la turbine, et elle ne dit rien de "
   "l'origine. Si l'eau revient après chaque pompage, le problème n'est pas le débit."),
  ("L'assurance couvre-t-elle une cave inondée&nbsp;?",
   "Cela dépend de l'origine et de votre contrat&nbsp;: un refoulement de réseau, une "
   "infiltration et une remontée de nappe ne relèvent pas des mêmes garanties, et un "
   "arrêté de catastrophe naturelle change encore la donne. Photographiez tout, gardez "
   "notre rapport, et déclarez rapidement."),
  ("Combien de temps pour assécher&nbsp;?",
   "Comptez plusieurs semaines pour un sous-sol enterré, davantage si les murs sont en "
   "pierre. Ne refermez pas, ne recouvrez pas et ne repeignez pas avant que le support "
   "soit sec&nbsp;: l'humidité enfermée ressort toujours."),
  ("Intervenez-vous en urgence sur tout le département&nbsp;?",
   "Oui, de l'agglomération briochine aux communes rurales, 24h/24 et 7j/7. En période "
   "d'orages, les demandes arrivent en rafale&nbsp;: nous annonçons un délai réaliste dès "
   "l'appel et traitons en priorité les situations présentant un risque."),
 ],
},

{
 "slug": "odeur-egout-dans-la-maison-cotes-d-armor",
 "court": "Odeur d'égout (22)",
 "dept": "22", "act": "degorgement", "date": "2026-09-30",
 "titre": "Odeur d'égout dans la maison (22) : d'où ça vient — ETS-BZH",
 "h1": "Odeur d'égout dans la maison&nbsp;: siphon désamorcé, ventilation bouchée ou réseau en cause",
 "meta": ("Odeur d'égout dans une maison des Côtes-d'Armor : les 4 causes possibles, le "
          "test du verre d'eau, et quand appeler. Intervention 7j/7 au 02 20 06 00 75."),
 "mots_cles": ("odeur d'égout maison, siphon désamorcé, ventilation primaire bouchée, "
               "mauvaise odeur canalisation Côtes-d'Armor"),
 "chapo": ("Une odeur d'égout qui apparaît dans une pièce n'est jamais anodine, mais "
           "elle est rarement grave&nbsp;: dans la majorité des cas, un siphon s'est "
           "simplement vidé. Encore faut-il savoir lequel. Voici comment remonter à "
           "l'origine en quelques minutes, sans rien démonter."),
 "urgent": [
   "Aérez largement la pièce concernée.",
   "Faites couler de l'eau une trentaine de secondes dans chaque bonde, évier, "
   "lavabo, douche, et dans le siphon de sol s'il y en a un.",
   "Repérez dans quelle pièce l'odeur est la plus forte, et à quel moment de la "
   "journée elle apparaît&nbsp;: c'est l'indice le plus utile.",
   "Vérifiez si l'odeur suit l'usage d'un appareil précis&nbsp;: lave-linge, "
   "lave-vaisselle, WC.",
 ],
 "danger": ("Une odeur d'égout persistante accompagnée de maux de tête, ou qui "
            "s'accentue dans une pièce fermée, ne doit pas être ignorée&nbsp;: les gaz "
            "d'égout ne sont pas seulement désagréables. Aérez, n'allumez pas de flamme, "
            "et faites contrôler. Si l'odeur ressemble à du gaz de ville et non à de "
            "l'égout, sortez, n'actionnez aucun interrupteur et appelez le service "
            "d'urgence gaz depuis l'extérieur."),
 "sections": [
  ("Le test du verre d'eau",
   ["Chaque appareil sanitaire est protégé par un siphon&nbsp;: un coude qui retient un "
    "peu d'eau et forme un bouchon liquide entre la canalisation et la pièce. Si cette "
    "eau disparaît, l'air de la canalisation entre librement.",
    "Un siphon se vide de trois façons. Par évaporation, quand l'appareil n'a pas servi "
    "depuis des semaines — c'est le cas classique de la chambre d'amis, du garage ou de "
    "la résidence secondaire. Par siphonnage, quand un gros rejet dans la colonne aspire "
    "l'eau des siphons voisins. Par refoulement, quand la pression de la canalisation "
    "chasse l'eau du coude.",
    "Le test&nbsp;: versez un verre d'eau dans chaque bonde suspecte, y compris celles "
    "qui ne servent jamais. Si l'odeur disparaît en quelques minutes, vous aviez un "
    "siphon à sec, et l'affaire est close. Si elle revient au bout de quelques jours au "
    "même endroit, le siphon se vide à chaque fois&nbsp;: il y a une cause, et c'est "
    "souvent la ventilation."],
   None),
  ("Quand c'est la ventilation du réseau",
   ["Une évacuation a besoin d'entrées d'air pour fonctionner&nbsp;: sans elles, l'eau "
    "qui descend crée une dépression et aspire les siphons sur son passage. Cette "
    "fonction est assurée par la colonne de ventilation qui sort en toiture, ou par un "
    "clapet aérateur.",
    "Dans les maisons anciennes des Côtes-d'Armor, cette sortie de toiture est souvent "
    "obstruée&nbsp;: un nid, des feuilles, parfois un chapeau posé lors d'une réfection "
    "de couverture. Les symptômes sont caractéristiques&nbsp;: glouglous dans les "
    "siphons quand on tire la chasse, évacuations lentes sans bouchon, et odeur "
    "intermittente qui revient toujours après un gros rejet.",
    "Autre configuration fréquente localement&nbsp;: la longère rénovée dont la salle de "
    "bain a été créée loin du réseau existant, avec une longue horizontale et sans "
    "ventilation secondaire. Cela fonctionne tant que les débits restent faibles, et "
    "cela se manifeste le jour où la maison se remplit."],
   None),
  ("Les autres causes, plus rares mais réelles",
   [],
   ["Un siphon de sol de garage ou de buanderie, jamais alimenté, qui s'évapore.",
    "Un joint de pied de cuvette desserré&nbsp;: l'odeur est alors très localisée au WC.",
    "Un tuyau d'évacuation de lave-linge ou de lave-vaisselle branché sans siphon.",
    "Une canalisation fissurée sous dallage&nbsp;: l'odeur est diffuse, permanente et "
    "ne cède à aucun verre d'eau. Elle se localise à la caméra.",
    "Sur fosse septique, une ventilation d'extraction absente ou bouchée&nbsp;: les gaz "
    "ressortent alors par le point le plus faible du réseau intérieur.",
    "Un regard extérieur dont le tampon ne joint plus, par vent portant."],
   ),
 ],
 "faq": [
  ("L'odeur revient toujours au même endroit, est-ce grave&nbsp;?",
   "Pas nécessairement, mais il y a une cause mécanique. Un siphon qui se vide à "
   "répétition signale un problème de ventilation ou de pente. Cela se corrige, et "
   "c'est plus durable que de reverser un verre d'eau chaque semaine."),
  ("Puis-je verser de l'eau de Javel pour supprimer l'odeur&nbsp;?",
   "Cela masque quelques heures, sans traiter la cause, et sur une installation reliée "
   "à une fosse septique, la Javel nuit aux bactéries qui la font fonctionner. Mieux "
   "vaut trouver le siphon fautif."),
  ("L'odeur apparaît surtout quand il y a du vent, pourquoi&nbsp;?",
   "C'est un signe assez net d'un problème de ventilation du réseau ou d'un regard mal "
   "fermé&nbsp;: le vent crée une dépression qui tire l'air de la canalisation vers "
   "l'intérieur. Cela oriente le diagnostic vers la sortie de toiture."),
  ("Combien de temps dure le diagnostic&nbsp;?",
   "Le test des siphons et le contrôle des évacuations prennent moins d'une heure. Si "
   "l'origine reste introuvable, l'inspection caméra permet de localiser une fissure ou "
   "un défaut de pente, avec rapport écrit."),
 ],
},

{
 "slug": "fuite-enterree-entre-compteur-et-maison-cotes-d-armor",
 "court": "Fuite enterrée (22)",
 "dept": "22", "act": "plomberie", "date": "2026-09-30",
 "titre": "Fuite enterrée entre compteur et maison (22) — ETS-BZH",
 "h1": "Fuite enterrée entre le compteur et la maison&nbsp;: la repérer avant de creuser",
 "meta": ("Facture d'eau anormale dans les Côtes-d'Armor : localiser une fuite enterrée "
          "sans creuser au hasard, et faire jouer l'écrêtement. 02 20 06 00 75."),
 "mots_cles": ("fuite enterrée, facture d'eau anormale, recherche de fuite "
               "Côtes-d'Armor, compteur qui tourne, dégrèvement fuite"),
 "chapo": ("Une facture d'eau qui double sans explication, un compteur qui tourne "
           "alors que tout est fermé, un coin de terrain toujours vert&nbsp;: la fuite "
           "est probablement sur la conduite enterrée entre le compteur et la maison. "
           "Cette portion vous appartient, et il existe une procédure précise à suivre "
           "avant de sortir la pelle."),
 "urgent": [
   "Fermez tous les robinets et arrêtez les appareils, y compris le remplissage des "
   "WC et l'adoucisseur.",
   "Relevez le compteur, attendez une heure sans consommer, relevez à nouveau. Si "
   "l'index a bougé, il y a une fuite.",
   "Fermez maintenant la vanne d'arrêt à l'entrée de la maison et refaites "
   "l'essai&nbsp;: si le compteur tourne encore, la fuite est sur la portion enterrée.",
   "Photographiez les relevés avec l'heure&nbsp;: ce sont les pièces qui serviront à "
   "votre demande d'écrêtement.",
 ],
 "danger": ("Ne creusez pas au jugé pour « voir ». Sur une conduite enterrée, la zone "
            "humide en surface est rarement à l'aplomb de la fuite&nbsp;: l'eau suit la "
            "tranchée de pose et ressort parfois à plusieurs mètres. Une tranchée ouverte "
            "au mauvais endroit coûte plus cher que la localisation, et elle risque "
            "d'endommager d'autres réseaux enterrés — électricité, télécoms, gaz."),
 "sections": [
  ("Localiser sans casser",
   ["Sur une conduite enterrée, la recherche s'appuie sur plusieurs techniques qui se "
    "confirment l'une l'autre, et aucune ne nécessite d'ouvrir le terrain.",
    "La <strong>corrélation acoustique</strong> écoute le bruit caractéristique de "
    "l'eau qui s'échappe sous pression, et recoupe les mesures prises en deux points "
    "pour situer la fuite le long du tracé. La <strong>mise en pression avec gaz "
    "traceur</strong> remplit la conduite d'un mélange inoffensif qui remonte à travers "
    "le sol au droit du percement, et qu'un détecteur repère en surface. La "
    "<strong>caméra thermique</strong> révèle les écarts de température au sol quand la "
    "conduite est peu profonde.",
    "L'objectif est toujours le même&nbsp;: ouvrir une fouille d'un mètre carré au bon "
    "endroit plutôt qu'une tranchée de vingt mètres."],
   None),
  ("Le terrain costarmoricain complique un peu les choses",
   ["Beaucoup de maisons de l'arrière-pays sont implantées loin de la limite de "
    "propriété&nbsp;: entre le compteur en limite et la maison, il n'est pas rare de "
    "compter trente ou quarante mètres de conduite enterrée, souvent posée il y a "
    "plusieurs décennies.",
    "Sur ces réseaux anciens, deux causes dominent. Le <strong>polyéthylène des "
    "premières générations</strong>, qui se fragilise et se fend sur les raccords. Et "
    "les <strong>racines</strong>, en particulier sous une haie ou un talus breton, qui "
    "exercent une pression lente sur la conduite jusqu'à la déformer.",
    "Un troisième facteur, plus insidieux, tient au sol lui-même&nbsp;: sur un terrain "
    "schisteux, une fuite ne crée pas toujours de flaque. L'eau part dans les fissures "
    "de la roche, et rien n'apparaît en surface. C'est pourquoi une facture anormale "
    "sans trace visible ne veut jamais dire qu'il n'y a pas de fuite."],
   None),
  ("La démarche auprès du service des eaux",
   [],
   ["Conservez les relevés de compteur horodatés et les photos.",
    "Demandez au service des eaux le détail de la consommation comparée aux années "
    "précédentes&nbsp;: c'est la base du dossier.",
    "Faites réparer, et gardez la facture de réparation détaillée, qui doit mentionner "
    "la localisation et la nature de la fuite.",
    "Transmettez cette facture au service des eaux&nbsp;: un écrêtement de la part "
    "excédentaire est prévu pour les fuites sur canalisation après compteur dans les "
    "logements, sous conditions et dans un délai à respecter.",
    "Renseignez-vous sur ce délai dès le départ&nbsp;: il court à compter de "
    "l'information reçue du service, et il se rate facilement."],
   ),
 ],
 "faq": [
  ("Comment savoir si la fuite est avant ou après le compteur&nbsp;?",
   "Fermez la vanne située juste après le compteur. Si le compteur continue de tourner, "
   "la fuite est en amont et relève du service des eaux. S'il s'arrête, elle est sur "
   "votre portion, entre le compteur et la maison, ou dans la maison."),
  ("La recherche de fuite est-elle prise en charge&nbsp;?",
   "Certains contrats multirisque habitation la couvrent, avec des modalités variables. "
   "Un appel à votre assureur avant l'intervention évite une avance inutile. Nous "
   "fournissons dans tous les cas un rapport exploitable."),
  ("Combien de temps dure une recherche de fuite&nbsp;?",
   "Comptez en général une demi-journée sur une conduite enterrée, selon la longueur du "
   "tracé et la nature du sol. La réparation se programme ensuite, une fois le point "
   "exact connu."),
  ("Et si la fuite est sous la dalle de la maison&nbsp;?",
   "C'est possible, et la méthode reste la même&nbsp;: localiser avant d'ouvrir. Selon "
   "la position, il est parfois plus économique d'abandonner la portion défectueuse et "
   "de refaire un tracé en apparent ou en contournement plutôt que de casser la dalle."),
 ],
},

{
 "slug": "plus-d-eau-chaude-que-faire-cotes-d-armor",
 "court": "Plus d'eau chaude (22)",
 "dept": "22", "act": "plomberie", "date": "2026-09-30",
 "titre": "Plus d'eau chaude (22) : les 4 vérifications — ETS-BZH",
 "h1": "Plus d'eau chaude dans les Côtes-d'Armor&nbsp;: quatre vérifications avant d'appeler",
 "meta": "Plus d'eau chaude dans les Côtes-d'Armor : contacteur, disjoncteur, thermostat ou résistance ? Les vérifications avant d'appeler. 02 20 06 00 75.",
 "mots_cles": ("plus d'eau chaude, ballon qui ne chauffe plus, contacteur jour nuit, "
               "résistance chauffe-eau, dépannage Saint-Brieuc"),
 "chapo": ("Une panne d'eau chaude est rarement une panne d'appareil. Dans une bonne "
           "part des interventions, le ballon est en parfait état&nbsp;: c'est son "
           "alimentation ou sa commande qui a lâché. Quatre vérifications, faisables "
           "sans outil, permettent souvent de récupérer l'eau chaude le soir même — ou "
           "au moins de nous dire où chercher."),
 "urgent": [
   "Vérifiez que le disjoncteur du chauffe-eau, au tableau, n'est pas abaissé.",
   "Cherchez le contacteur jour/nuit — un petit boîtier au tableau — et placez-le "
   "en position I ou « marche forcée » pendant deux heures.",
   "Contrôlez que l'eau froide arrive bien&nbsp;: si la pression est faible partout, "
   "le problème n'est pas le ballon.",
   "Regardez sous l'appareil&nbsp;: la moindre trace d'eau change le diagnostic et la "
   "conduite à tenir.",
 ],
 "danger": ("N'ouvrez pas le capot du chauffe-eau et ne touchez pas à la résistance "
            "sans avoir coupé le disjoncteur correspondant&nbsp;: les bornes restent sous "
            "tension même appareil « éteint ». Et ne mettez jamais un ballon sous tension "
            "s'il a été vidangé&nbsp;: une résistance alimentée à vide grille en quelques "
            "minutes."),
 "sections": [
  ("Les quatre causes, de la plus fréquente à la plus rare",
   ["<strong>Le contacteur jour/nuit.</strong> C'est lui qui autorise la chauffe "
    "pendant les heures creuses. Quand il se bloque ou que son contact s'use, le ballon "
    "ne reçoit plus rien alors que tout paraît normal. La marche forcée est le test&nbsp;: "
    "si l'eau chaude revient au bout de deux heures, vous avez votre réponse.",
    "<strong>Le thermostat.</strong> Il commande la chauffe et se met en sécurité en "
    "cas d'échauffement anormal. Un réarmement suffit parfois, mais s'il se déclenche à "
    "nouveau, c'est qu'il y a une cause — le plus souvent un entartrage ou une "
    "résistance en fin de vie.",
    "<strong>La résistance.</strong> Elle chauffe l'eau et finit par lâcher, brutalement "
    "ou progressivement. Symptôme typique&nbsp;: de l'eau tiède, en quantité insuffisante, "
    "alors que rien d'autre n'a changé. Elle se remplace, l'appareil est conservé.",
    "<strong>L'appareil lui-même.</strong> Cuve percée, entartrage massif ou corrosion "
    "avancée. C'est le seul des quatre cas où la question du remplacement se pose, et "
    "elle se pose alors honnêtement, chiffres en main."],
   None),
  ("Ce que l'eau douce bretonne change au diagnostic",
   ["Le sous-sol granitique des Côtes-d'Armor donne une eau peu calcaire. C'est une "
    "bonne nouvelle pour les résistances, qui s'entartrent lentement, et pour les "
    "robinetteries.",
    "Mais une eau douce est plus agressive pour les métaux, et la protection de la cuve "
    "repose alors entièrement sur l'anode, cette tige sacrificielle qui se consume à la "
    "place de l'acier. Personne ne la surveille, elle s'épuise en silence, et la cuve "
    "commence à se corroder sans aucun signe extérieur.",
    "Conséquence pratique&nbsp;: dans ce département, quand un ballon de plus de dix ans "
    "tombe en panne, le diagnostic ne doit pas s'arrêter à la pièce défectueuse. On "
    "regarde aussi l'anode et l'état intérieur, parce que remplacer une résistance sur "
    "une cuve déjà percée à moitié n'a aucun sens."],
   None),
  ("Récupérer de l'eau chaude tout de suite",
   [],
   ["Passez le contacteur en marche forcée&nbsp;: deux heures suffisent pour une "
    "douche.",
    "Baissez les soutirages inutiles le temps du dépannage — un ballon vidé met "
    "plusieurs heures à remonter en température.",
    "Vérifiez le réglage&nbsp;: entre 55 et 60&nbsp;°C, c'est le bon compromis entre "
    "sécurité sanitaire, corrosion et consommation.",
    "Si l'eau est chaude mais insuffisante, le ballon est peut-être simplement "
    "sous-dimensionné pour le nombre d'occupants actuel.",
    "Si l'eau chaude se termine bien plus vite qu'avant sans changement d'habitudes, "
    "suspectez la résistance ou le thermostat plutôt que le volume."],
   ),
 ],
 "faq": [
  ("La marche forcée fonctionne mais l'eau redevient froide le lendemain&nbsp;?",
   "C'est le contacteur jour/nuit ou son signal qui est en cause&nbsp;: la chauffe ne "
   "se déclenche plus automatiquement en heures creuses. La pièce se remplace "
   "rapidement, et le fonctionnement normal revient."),
  ("Combien de temps pour récupérer l'eau chaude&nbsp;?",
   "Si la pièce est courante — thermostat, résistance, contacteur — nos véhicules "
   "l'ont à bord et l'eau chaude revient dans la journée. Comptez ensuite deux à quatre "
   "heures de chauffe selon le volume du ballon."),
  ("Faut-il détartrer un chauffe-eau en Bretagne&nbsp;?",
   "Moins souvent qu'ailleurs, l'eau étant peu calcaire sur une grande partie du "
   "territoire. En revanche, le contrôle de l'anode et du groupe de sécurité reste "
   "utile tous les deux ans&nbsp;: c'est ce qui allonge réellement la durée de vie ici."),
  ("Intervenez-vous le week-end pour une panne d'eau chaude&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur l'ensemble des Côtes-d'Armor. Le devis est gratuit et le "
   "tarif validé avec vous avant tout démarrage."),
 ],
},

{
 "slug": "radiateur-ou-chauffage-qui-fuit-cotes-d-armor",
 "court": "Radiateur qui fuit (22)",
 "dept": "22", "act": "plomberie", "date": "2026-09-30",
 "titre": "Radiateur ou chauffage qui fuit (22) : que faire — ETS-BZH",
 "h1": "Radiateur qui fuit dans les Côtes-d'Armor&nbsp;: isoler la fuite sans vider le circuit",
 "meta": ("Radiateur ou circuit de chauffage qui fuit dans les Côtes-d'Armor : isoler, "
          "limiter les dégâts, et ce qui se répare. Plombier 7j/7 au 02 20 06 00 75."),
 "mots_cles": ("radiateur qui fuit, fuite circuit chauffage, purgeur qui goutte, "
               "pression chaudière qui baisse, plombier chauffage Côtes-d'Armor"),
 "chapo": ("Une flaque sous un radiateur au premier jour de chauffe, c'est presque un "
           "classique de l'automne breton. La bonne nouvelle&nbsp;: dans la plupart des "
           "cas, on isole le radiateur concerné sans vider toute l'installation. Encore "
           "faut-il savoir d'où vient l'eau et manœuvrer les bons robinets."),
 "urgent": [
   "Glissez un récipient et des serviettes sous la fuite, et protégez le sol — "
   "l'eau de chauffage tache durablement un parquet.",
   "Fermez les deux robinets du radiateur&nbsp;: celui d'arrivée et le té de réglage, "
   "de l'autre côté. Sur beaucoup d'installations, cela suffit à isoler l'appareil.",
   "Surveillez la pression de la chaudière&nbsp;: si elle chute, le circuit se vide "
   "quelque part.",
   "Ne remettez pas de l'eau en boucle pour compenser une pression qui rebaisse&nbsp;: "
   "vous ne faites qu'alimenter la fuite.",
 ],
 "danger": ("L'eau d'un circuit de chauffage peut être brûlante et elle est chargée de "
            "boues et de traitements&nbsp;: protégez-vous les mains, ne la laissez pas "
            "sur une peau ou sur un revêtement. Et ne desserrez jamais un raccord pour "
            "« voir » pendant que le circuit est chaud et sous pression&nbsp;: laissez "
            "refroidir, et coupez la chaudière avant toute manipulation."),
 "sections": [
  ("D'où vient l'eau, exactement",
   ["Sous un radiateur, quatre points fuient couramment, et le remède n'est pas le même.",
    "<strong>Le purgeur</strong>, en haut du radiateur. Souvent laissé entrouvert après "
    "une purge, ou dont le joint est fatigué. C'est bénin, et cela se règle en quelques "
    "minutes.",
    "<strong>Le robinet thermostatique ou le té de réglage</strong>, en bas. Le presse-"
    "étoupe se dessèche et laisse passer un suintement le long de la tige. Le "
    "remplacement de la tête ou du robinet règle la situation.",
    "<strong>Le raccord entre le radiateur et le tube.</strong> Joint durci ou écrou "
    "desserré par les cycles de dilatation, typiques d'une remise en chauffe après "
    "l'été.",
    "<strong>Le corps du radiateur lui-même</strong>, percé par corrosion interne. Là, "
    "il n'y a pas de réparation durable&nbsp;: l'élément se remplace. Le signe qui ne "
    "trompe pas est une eau noirâtre et une perforation en partie basse."],
   None),
  ("La pression qui baisse : le symptôme à ne pas laisser traîner",
   ["Sur une installation fermée, la pression doit rester stable, en général autour de "
    "1,5 bar à froid. Si vous devez remettre de l'eau toutes les semaines, le circuit "
    "perd de l'eau quelque part&nbsp;— et chaque appoint apporte de l'eau neuve, donc de "
    "l'oxygène, donc de la corrosion. Le remède devient alors la cause du mal suivant.",
    "La fuite n'est pas toujours visible&nbsp;: elle peut être sur une liaison encastrée "
    "dans une chape, sous un plancher, ou sur un raccord dans un vide sanitaire. Là "
    "encore, la recherche non destructive — caméra thermique, mise en pression — évite "
    "d'ouvrir au hasard.",
    "Dans le bâti ancien costarmoricain, une configuration revient souvent&nbsp;: des "
    "canalisations de chauffage passées sous dallage lors d'une rénovation, sans gaine "
    "ni protection, dans une maison où l'humidité du sol est permanente. La corrosion "
    "extérieure fait le reste, en dix ou quinze ans."],
   None),
  ("Avant la saison de chauffe, ce qui évite l'appel d'urgence",
   [],
   ["Une mise en route avant les premiers froids, plutôt que le soir de la première "
    "gelée.",
    "Une purge complète des radiateurs, du plus proche au plus éloigné de la chaudière.",
    "Un contrôle de la pression à froid et un œil sur son évolution après quelques "
    "jours.",
    "Un désembouage quand les radiateurs chauffent inégalement ou restent froids en "
    "bas&nbsp;: les boues accélèrent la corrosion et donc les fuites.",
    "Le remplacement préventif des têtes thermostatiques bloquées, qui finissent par "
    "fuir à la tige.",
    "La vérification du vase d'expansion&nbsp;: une pression qui varie fortement entre "
    "chaud et froid vient souvent de là."],
   ),
 ],
 "faq": [
  ("Puis-je juste serrer le raccord qui goutte&nbsp;?",
   "Parfois, mais avec prudence&nbsp;: sur un tube ancien, un serrage excessif casse le "
   "raccord et transforme un suintement en fuite franche. Si un huitième de tour ne "
   "suffit pas, arrêtez et isolez le radiateur."),
  ("Mon radiateur est percé, faut-il tout changer&nbsp;?",
   "Non, un radiateur se remplace seul&nbsp;: le reste de l'installation n'est pas en "
   "cause. En revanche, si plusieurs éléments percent en peu de temps, c'est le circuit "
   "qu'il faut regarder — boues, oxygène, qualité de l'eau."),
  ("Je n'ai pas de robinet sur mon radiateur, comment isoler&nbsp;?",
   "Sur les installations anciennes sans organe d'isolement, il faut vidanger la "
   "portion concernée. C'est plus long, et c'est aussi l'occasion d'ajouter les "
   "robinets qui manquaient — cela vous évitera la même situation la prochaine fois."),
  ("Intervenez-vous en urgence pour une fuite de chauffage&nbsp;?",
   "Oui, 7j/7 sur l'ensemble du département. En pleine saison de chauffe, l'objectif "
   "est d'abord d'isoler et de rétablir le chauffage sur le reste du logement, puis de "
   "réparer dans de bonnes conditions."),
 ],
},

{
 "slug": "disjoncteur-qui-saute-sans-arret-cotes-d-armor",
 "court": "Disjoncteur qui saute (22)",
 "dept": "22", "act": "electricite", "date": "2026-09-30",
 "titre": 'Disjoncteur qui saute sans arrêt (22) — ETS-BZH',
 "h1": "Disjoncteur qui saute sans arrêt&nbsp;: trouver le circuit fautif en quinze minutes",
 "meta": ("Disjoncteur ou différentiel qui saute sans arrêt dans les Côtes-d'Armor : la "
          "méthode pour isoler le circuit en cause, et quand appeler. 02 20 06 00 75."),
 "mots_cles": ("disjoncteur qui saute, différentiel qui saute, trouver le circuit "
               "fautif, électricien urgence Côtes-d'Armor, tableau électrique"),
 "chapo": ("Un disjoncteur qui saute n'est pas une panne&nbsp;: c'est une protection qui "
           "fait son travail. La question n'est donc jamais « comment l'empêcher de "
           "sauter » mais « qu'est-ce qu'il protège, et de quoi ». Voici la méthode que "
           "nous appliquons, et que vous pouvez mener vous-même sans risque."),
 "urgent": [
   "Notez ce qui a déclenché la coupure&nbsp;: quel appareil venait d'être allumé, "
   "dans quelle pièce, à quel moment. C'est l'information la plus utile.",
   "Identifiez lequel a sauté&nbsp;: le petit disjoncteur d'un circuit, l'interrupteur "
   "différentiel plus large, ou le gros disjoncteur de branchement.",
   "Débranchez l'appareil suspect avant de réarmer.",
   "Si le disjoncteur refuse de remonter, ne forcez pas et ne le maintenez pas en "
   "position&nbsp;: il y a une raison.",
 ],
 "danger": ("Ne neutralisez jamais une protection qui saute&nbsp;: ni en la remplaçant "
            "par un calibre supérieur, ni en la bloquant, ni en pontant. Un disjoncteur "
            "qui se déclenche protège soit les personnes, soit le câble contre "
            "l'échauffement. Le neutraliser ne supprime pas le défaut&nbsp;: il supprime "
            "l'alerte, et laisse le risque intact."),
 "sections": [
  ("La méthode d'isolement, pas à pas",
   ["Elle consiste uniquement à manœuvrer des protections, ce que vous pouvez faire "
    "sans danger.",
    "Abaissez tous les disjoncteurs divisionnaires — les petits, alignés en rangée. "
    "Remontez ensuite la protection qui sautait&nbsp;: elle doit tenir. Puis remontez "
    "les divisionnaires un par un, en attendant quelques secondes entre chaque.",
    "Celui qui provoque le déclenchement désigne le circuit en défaut. Laissez-le "
    "abaissé&nbsp;: vous avez récupéré le courant partout ailleurs, et vous pouvez "
    "attendre l'intervention sans vivre dans le noir.",
    "Il reste à savoir ce qui, sur ce circuit, pose problème. Débranchez tout ce qui y "
    "est raccordé, remontez, puis rebranchez appareil par appareil. Si le défaut "
    "n'apparaît avec aucun appareil, il est dans l'installation elle-même — câble, "
    "boîte de dérivation, point lumineux."],
   None),
  ("Ce que le type de protection vous dit du défaut",
   ["<strong>Un divisionnaire seul qui saute</strong> signale en général une "
    "surintensité&nbsp;: trop d'appareils sur le même circuit, ou un appareil en "
    "court-circuit. Le défaut est circonscrit.",
    "<strong>L'interrupteur différentiel qui saute</strong> signale un courant de fuite "
    "vers la terre. Autrement dit, du courant part où il ne devrait pas&nbsp;: humidité "
    "dans un boîtier, appareil dont l'isolement est dégradé, câble blessé. C'est le cas "
    "le plus courant après une entrée d'eau, et c'est aussi le plus important, car ce "
    "dispositif protège les personnes.",
    "<strong>Le disjoncteur de branchement qui saute</strong> — le gros, près du "
    "compteur — signale soit un dépassement de la puissance souscrite, soit un défaut "
    "général. S'il refuse de se réarmer, arrêtez là.",
    "Un cas typique dans le département&nbsp;: la longère ou la maison de bourg dont "
    "l'installation a été étendue par tranches, avec des dérivations dans les combles "
    "ou une dépendance. L'humidité entre par la toiture, et le différentiel se met à "
    "sauter sans qu'aucun appareil ne soit en cause."],
   None),
  ("Les situations où il ne faut pas chercher soi-même",
   [],
   ["Odeur de brûlé, trace noire, grésillement&nbsp;: coupez tout et appelez.",
    "Le disjoncteur de branchement refuse de se réarmer.",
    "Le différentiel saute même avec tous les divisionnaires abaissés.",
    "Chocs électriques ressentis au contact d'un robinet ou d'un appareil.",
    "Tableau à fusibles à broche, sans protection différentielle 30&nbsp;mA&nbsp;: le "
    "défaut ne sera pas détecté du tout.",
    "Installation partiellement mouillée&nbsp;: le contrôle d'isolement doit être fait "
    "avant remise en service."],
   ),
 ],
 "faq": [
  ("Mon disjoncteur saute uniquement quand j'allume le four, est-ce grave&nbsp;?",
   "C'est le signe que ce circuit n'est pas dimensionné pour cet usage, ou que "
   "l'appareil présente un défaut. Un four, une plaque, un sèche-linge ou une borne de "
   "recharge demandent un circuit dédié&nbsp;: c'est une reprise simple, et elle supprime "
   "définitivement le problème."),
  ("Puis-je augmenter la puissance de mon abonnement&nbsp;?",
   "Oui, cela se demande à votre fournisseur, et c'est la bonne réponse quand le "
   "disjoncteur de branchement saute par dépassement. Mais avant d'augmenter, il faut "
   "vérifier que l'installation supporte cette puissance&nbsp;: augmenter sans contrôler, "
   "c'est déplacer la contrainte sur les câbles."),
  ("Le différentiel saute quand il pleut, pourquoi&nbsp;?",
   "Parce qu'un point de l'installation prend l'eau&nbsp;: luminaire extérieur, prise de "
   "terrasse, coffret de jardin, portail motorisé, ou infiltration en toiture qui "
   "atteint une dérivation. La méthode d'isolement décrite plus haut désigne le circuit, "
   "nous localisons ensuite le point exact."),
  ("Intervenez-vous la nuit dans les Côtes-d'Armor&nbsp;?",
   "Oui, 24h/24 et 7j/7. Une coupure totale qu'on n'arrive pas à rétablir fait partie "
   "des situations traitées en astreinte. Le délai est annoncé dès l'appel."),
 ],
},

{
 "slug": "tableau-a-fusibles-a-broche-cotes-d-armor",
 "court": "Tableau à fusibles (22)",
 "dept": "22", "act": "electricite", "date": "2026-09-30",
 "titre": "Tableau à fusibles à broche (22) : l'urgence — ETS-BZH",
 "h1": "Tableau à fusibles à broche dans une longère&nbsp;: pourquoi cela ne peut plus attendre",
 "meta": "Tableau électrique à fusibles à broche dans les Côtes-d'Armor : ce qui n'est pas protégé et comment se passe un remplacement. 02 20 06 00 75.",
 "mots_cles": ("fusibles à broche, tableau électrique ancien, mise en sécurité "
               "électrique, différentiel 30 mA, rénovation électrique Côtes-d'Armor"),
 "chapo": ("Un tableau à fusibles à broche fonctionne&nbsp;: il coupe en cas de "
           "court-circuit, et c'est ce qui rassure. Le problème n'est pas ce qu'il fait, "
           "c'est ce qu'il ne fait pas. Dans une maison humide et ancienne, ce qu'il ne "
           "détecte pas est précisément ce qui blesse."),
 "urgent": [
   "Ne remplacez jamais un fusible fondu par un fil de cuivre, une pièce de monnaie "
   "ou un fusible de calibre supérieur. C'est la cause d'incendie la plus documentée "
   "sur ces installations.",
   "Si un fusible fond à répétition sur le même circuit, laissez-le hors service et "
   "faites contrôler&nbsp;: il y a un défaut réel derrière.",
   "Repérez si votre tableau comporte un interrupteur différentiel — un appareil "
   "plus large avec un bouton « test ». S'il n'y en a aucun, signalez-le à l'appel.",
   "Testez le différentiel s'il existe&nbsp;: le bouton « test » doit le faire "
   "déclencher. S'il ne se déclenche pas, il ne protège plus personne.",
 ],
 "danger": ("Un fusible protège le câble, pas la personne. Il fond sur une "
            "surintensité, c'est-à-dire sur un courant fort. Le courant qui traverse un "
            "corps humain lors d'un contact avec une masse sous tension est très "
            "inférieur à ce seuil&nbsp;: le fusible ne fondra pas, et rien ne coupera. "
            "C'est exactement ce que fait un dispositif différentiel 30&nbsp;mA, et c'est "
            "pour cela qu'il est devenu obligatoire dans les installations neuves."),
 "sections": [
  ("Ce qui manque réellement dans ces tableaux",
   ["Trois fonctions font défaut sur une installation d'époque, et elles se cumulent.",
    "<strong>La protection différentielle.</strong> Sans elle, aucun défaut d'isolement "
    "n'est détecté. Une machine à laver dont la carcasse devient conductrice, un "
    "luminaire de salle de bain qui prend l'humidité, un câble blessé dans une "
    "cloison&nbsp;: rien ne coupe.",
    "<strong>La prise de terre.</strong> Dans beaucoup de longères, elle est absente, "
    "ou réduite à un piquet corrodé. Sans terre, même un différentiel n'a pas toujours "
    "de quoi détecter le défaut.",
    "<strong>Les circuits dédiés.</strong> Les installations anciennes ont été conçues "
    "pour l'éclairage et quelques prises. On y a branché depuis un lave-linge, un "
    "sèche-linge, un four, une plaque, parfois une borne de recharge. Les câbles n'ont "
    "pas changé de section pour autant.",
    "S'ajoute, dans le bâti breton en pierre, un facteur aggravant permanent&nbsp;: "
    "l'humidité des murs. Elle rend les défauts d'isolement plus fréquents et les "
    "contacts plus dangereux, parce qu'un sol ou un mur humide conduit bien mieux qu'un "
    "sol sec."],
   None),
  ("Faut-il tout refaire ? Non, et c'est important",
   ["La crainte qui bloque la décision est toujours la même&nbsp;: refaire toute "
    "l'électricité d'une maison ancienne, casser les murs, ouvrir les plafonds. Ce n'est "
    "pas ce que nous proposons dans la majorité des cas.",
    "La première étape est une <strong>mise en sécurité</strong>&nbsp;: remplacer le "
    "tableau par un tableau moderne avec protections différentielles 30&nbsp;mA, créer "
    "ou reprendre la prise de terre, ajouter les circuits dédiés aux appareils de forte "
    "puissance, et repérer les circuits existants. Cela se fait en général en une "
    "journée, sans toucher aux murs.",
    "Le reste — refaire des câbles trop anciens, remplacer des appareillages sans "
    "terre, sécuriser les volumes de la salle de bain — se planifie ensuite, "
    "par étapes, au rythme des travaux de la maison. Ce qui compte est de ne plus vivre "
    "sans protection différentielle."],
   None),
  ("Comment se passe un remplacement de tableau",
   [],
   ["Un état des lieux de l'existant, circuit par circuit, avec mesure de la terre.",
    "Une coupure d'alimentation limitée à la durée du chantier, annoncée à l'avance.",
    "La pose du nouveau tableau avec protections différentielles et disjoncteurs "
    "adaptés à chaque circuit.",
    "Le repérage et l'étiquetage de tous les départs&nbsp;: vous saurez enfin ce que "
    "coupe chaque protection.",
    "La reprise ou la création de la prise de terre et de la liaison équipotentielle "
    "dans les pièces d'eau.",
    "Les essais en votre présence, protection par protection, et un rapport écrit de "
    "ce qui a été fait et de ce qui reste à prévoir."],
   ),
 ],
 "faq": [
  ("Mon installation fonctionne depuis quarante ans, pourquoi changer&nbsp;?",
   "Parce qu'elle protège contre ce pour quoi elle a été conçue, et que les usages ont "
   "changé&nbsp;: la puissance installée dans un logement a été multipliée, et la "
   "protection des personnes n'existait pas à l'époque. Ce n'est pas une question de "
   "vétusté, c'est une question de fonction absente."),
  ("Un contrôle est-il obligatoire&nbsp;?",
   "Un diagnostic électrique est exigé lors de la vente et de la mise en location d'un "
   "logement de plus de quinze ans. Un tableau à fusibles à broche sans différentiel y "
   "figure systématiquement en anomalie, et cela pèse au moment de vendre ou de louer."),
  ("Combien de temps sans électricité pendant les travaux&nbsp;?",
   "Un remplacement de tableau demande en général une journée, coupure comprise. Nous "
   "annonçons la plage précise à l'avance pour que vous puissiez vous organiser."),
  ("Intervenez-vous dans les communes rurales du département&nbsp;?",
   "Oui, sur l'ensemble des Côtes-d'Armor, de Saint-Brieuc et Lannion aux communes de "
   "l'arrière-pays. Le diagnostic et le devis sont gratuits et sans engagement."),
 ],
},

# ----------------------------------------------------- 29 — FINISTÈRE (suite)
{
 "slug": "evier-de-cuisine-bouche-finistere",
 "court": "Évier de cuisine bouché (29)",
 "dept": "29", "act": "degorgement", "date": "2026-09-30",
 "titre": "Évier de cuisine bouché (29) : la bonne méthode — ETS-BZH",
 "h1": "Évier de cuisine bouché en Finistère&nbsp;: pourquoi l'eau chaude ne suffit plus",
 "meta": ("Évier de cuisine bouché en Finistère : démonter le siphon sans dégât, ce "
          "qu'il ne faut pas verser, et quand le bouchon est plus loin. 02 20 06 00 75."),
 "mots_cles": ("évier bouché que faire, bouchon de graisse canalisation, débouchage "
               "cuisine Brest, siphon évier, dégorgement Finistère"),
 "chapo": ("Un évier de cuisine se bouche presque toujours pour la même raison&nbsp;: la "
           "graisse. Elle part liquide et tiède, elle refroidit dans le tuyau, elle se "
           "fige, et elle capte tout ce qui passe ensuite. Ce qui change, c'est "
           "l'endroit où elle s'est figée — et c'est ce qui détermine si vous réglez la "
           "situation en vingt minutes ou pas du tout."),
 "urgent": [
   "Videz l'eau stagnante à l'écope avant toute chose&nbsp;: travailler dans un évier "
   "plein ne sert à rien.",
   "Placez un seau sous le siphon et dévissez-le à la main&nbsp;: sur la plupart des "
   "modèles, aucun outil n'est nécessaire.",
   "Nettoyez la cloche du siphon, elle retient l'essentiel des bouchons de cuisine.",
   "Remontez, faites couler, et observez&nbsp;: si l'eau part maintenant, c'était le "
   "siphon. Si elle stagne encore, le bouchon est plus loin.",
 ],
 "danger": ("Ne versez pas de déboucheur chimique avant de démonter le siphon. Vous "
            "retrouverez le produit dans le seau, sur les mains, parfois au visage. Et "
            "n'utilisez jamais de soude sur une évacuation en fonte ancienne, "
            "fréquente dans le bâti brestois&nbsp;: elle attaque le métal et transforme "
            "un bouchon en fuite."),
 "sections": [
  ("Trois endroits, trois niveaux de difficulté",
   ["<strong>Le siphon.</strong> C'est le coude sous l'évier, conçu pour être démonté. "
    "Il retient les graisses, les résidus alimentaires et les petits objets. Dans plus "
    "de la moitié des cas, tout est là.",
    "<strong>L'horizontale après le siphon.</strong> Le tuyau part vers le mur avec une "
    "pente faible, parfois nulle sur une cuisine aménagée après coup. La graisse s'y "
    "dépose sur plusieurs mètres et réduit le diamètre utile. Le siphon est propre, et "
    "pourtant l'eau ne part pas&nbsp;: c'est le cas typique qui demande un furet.",
    "<strong>La colonne ou le collecteur.</strong> Si l'évier ne part pas <em>et</em> "
    "qu'un autre appareil gargouille, le bouchon est en aval de tout le monde. Démonter "
    "le siphon ne changera rien.",
    "Un indice simple pour trancher&nbsp;: versez deux litres d'eau d'un coup. Si "
    "l'évacuation accepte un filet mais refuse un débit, le passage est rétréci sur la "
    "longueur — donc pas dans le siphon."],
   None),
  ("L'eau bouillante et le marc de café : deux idées reçues",
   ["Verser de l'eau bouillante fonctionne au tout début, quand la graisse est encore "
    "molle et proche. Sur un bouchon installé, l'eau refroidit avant de l'atteindre, "
    "fait fondre la surface, et la graisse se re-fige un peu plus loin — souvent dans "
    "une portion moins accessible. On déplace le problème.",
    "Le marc de café versé dans l'évier « pour nettoyer » est une idée tenace et "
    "exactement contre-productive&nbsp;: c'est une matière granuleuse qui s'agglomère "
    "parfaitement à la graisse. Nous en retirons régulièrement des bouchons compacts "
    "faits uniquement de cela.",
    "Ce qui marche vraiment est en amont&nbsp;: essuyer les poêles au papier avant de "
    "les laver, ne jamais vider une friture ou une graisse de cuisson dans l'évier, et "
    "poser une grille sur la bonde. Dans les crêperies et les restaurants du littoral "
    "finistérien, le même raisonnement s'applique à une autre échelle&nbsp;: sans "
    "entretien régulier du bac à graisse, le réseau se colmate en une saison."],
   None),
  ("Le bâti finistérien complique un peu la donne",
   [],
   ["Beaucoup d'évacuations en fonte ou en grès dans le centre de Brest et les bourgs "
    "anciens&nbsp;: parois rugueuses, la graisse y accroche bien mieux que sur du PVC.",
    "Des cuisines réaménagées avec de longues horizontales et des pentes faibles.",
    "Des joints de grès déchaussés qui créent des ressauts invisibles, où tout "
    "s'arrête.",
    "Des résidences secondaires utilisées par à-coups&nbsp;: les dépôts sèchent et "
    "durcissent pendant les mois d'inoccupation.",
    "Des locations saisonnières où l'usage double en été, sur un réseau dimensionné "
    "pour un foyer."],
   ),
 ],
 "faq": [
  ("Le siphon est propre mais l'eau ne part toujours pas&nbsp;?",
   "C'est que le bouchon est sur l'horizontale, après le siphon. Un furet manuel "
   "atteint parfois les premiers mètres&nbsp;; au-delà, il faut un furet électrique, et "
   "sur un réseau encrassé sur toute la longueur, c'est l'hydrocurage qui règle "
   "durablement la situation."),
  ("Les produits « entretien canalisation » servent-ils à quelque chose&nbsp;?",
   "En prévention sur une évacuation qui fonctionne, certains produits enzymatiques "
   "ralentissent l'accumulation. Sur un bouchon déjà formé, aucun ne fonctionne, et les "
   "déboucheurs caustiques présentent un vrai risque lors de l'intervention qui suivra."),
  ("Mon évier se rebouche tous les deux mois, que faire&nbsp;?",
   "Une récidive régulière n'est pas un problème d'usage mais de réseau&nbsp;: pente "
   "insuffisante, diamètre réduit, joint déchaussé. L'inspection caméra le montre, et "
   "un hydrocurage remet le diamètre utile à sa valeur d'origine."),
  ("Intervenez-vous à Brest et Quimper le week-end&nbsp;?",
   "Oui, 7j/7 sur l'ensemble du Finistère. Sur les agglomérations, nous visons l'heure&nbsp;; "
   "sur les communes éloignées, deux à trois heures. Le délai est annoncé dès l'appel."),
 ],
},

{
 "slug": "racines-dans-canalisation-finistere",
 "court": "Racines dans la canalisation (29)",
 "dept": "29", "act": "degorgement", "date": "2026-09-30",
 "titre": "Racines dans la canalisation (29) : les signes — ETS-BZH",
 "h1": "Racines dans une canalisation enterrée&nbsp;: le bouchon qui revient toujours",
 "meta": ("Canalisation envahie par les racines en Finistère : reconnaître les signes, "
          "l'inspection caméra et les vraies solutions. Dégorgement au 02 20 06 00 75."),
 "mots_cles": ("racines canalisation, bouchon qui revient, inspection caméra "
               "canalisation, hydrocurage racines Finistère, canalisation enterrée"),
 "chapo": ("Un bouchon qui revient tous les six mois au même endroit n'est pas une "
           "malchance&nbsp;: c'est un symptôme. Dans les jardins bretons bordés de haies "
           "et de talus, la première cause est presque toujours la même — des racines "
           "ont trouvé le chemin de votre canalisation, et elles ne repartiront pas "
           "d'elles-mêmes."),
 "urgent": [
   "Notez les dates des précédents débouchages&nbsp;: une récidive régulière au même "
   "endroit est l'information la plus utile que vous puissiez nous donner.",
   "Repérez ce qui pousse au-dessus du tracé&nbsp;: haie, talus, saule, peuplier, "
   "bambou, ou une simple bordure de laurier.",
   "Cessez d'enchaîner les débouchages à l'aveugle&nbsp;: chacun coûte, et aucun ne "
   "traite la cause.",
   "Demandez une inspection caméra plutôt qu'un énième passage de furet.",
 ],
 "danger": ("N'utilisez pas de produits « anti-racines » à base de sulfate de cuivre "
            "sur une installation reliée à une fosse septique ou à un épandage&nbsp;: ils "
            "détruisent les bactéries qui font fonctionner le système, et leur rejet "
            "dans le milieu naturel n'est pas anodin. Sur un réseau collectif, leur "
            "efficacité réelle sur une racine installée est très limitée."),
 "sections": [
  ("Comment une racine entre dans un tuyau",
   ["Une racine ne perce pas une canalisation saine&nbsp;: elle profite d'un défaut "
    "existant. Un joint de grès déchaussé, une fissure fine, un raccord mal emboîté sur "
    "une réparation ancienne. Il suffit d'une ouverture de quelques millimètres.",
    "Ce qui l'attire est l'humidité et les nutriments&nbsp;: une canalisation d'eaux "
    "usées est, du point de vue d'un arbre, le meilleur endroit du jardin. Une fois "
    "entrée, la racine se ramifie à l'intérieur du tuyau et forme un filet qui retient "
    "papier, graisses et lingettes. Le bouchon se construit dessus.",
    "C'est pour cela que le furet donne l'illusion de régler le problème&nbsp;: il "
    "perce le dépôt accumulé, l'écoulement revient, et le filet de racines reste en "
    "place. Quelques mois plus tard, tout recommence.",
    "En Finistère, deux configurations reviennent&nbsp;: les talus plantés qui bordent "
    "les parcelles, dont les essences ont un système racinaire agressif, et les jardins "
    "de bord de mer où les pins et les cyprès cherchent activement l'eau douce dans un "
    "sol sableux et pauvre."],
   None),
  ("L'inspection caméra change la conversation",
   ["Une caméra d'inspection descend dans la canalisation et filme la paroi. En une "
    "heure, on sait exactement ce qui se passe et où&nbsp;: à quel mètre la racine est "
    "entrée, par quel type de défaut, sur quelle longueur elle s'est développée, et dans "
    "quel état est le tuyau autour.",
    "Cela change tout, pour deux raisons. D'abord parce qu'on arrête de traiter un "
    "symptôme&nbsp;: on sait s'il faut simplement curer, ou s'il faut reprendre une "
    "portion. Ensuite parce que le rapport écrit sert de preuve — auprès d'un "
    "propriétaire si vous êtes locataire, auprès d'une assurance, ou auprès d'un voisin "
    "dont l'arbre est en cause.",
    "Nous remettons systématiquement ce diagnostic par écrit, avec la localisation au "
    "mètre près. Vous n'avez pas à nous croire sur parole&nbsp;: vous voyez l'image."],
   None),
  ("Les solutions, de la plus légère à la plus lourde",
   [],
   ["<strong>Le fraisage au furet à tête coupante</strong>&nbsp;: la racine est "
    "sectionnée à ras de la paroi. Efficace, mais elle repoussera si le défaut d'entrée "
    "subsiste.",
    "<strong>L'hydrocurage haute pression</strong>&nbsp;: il nettoie la paroi sur toute "
    "la longueur et retire les dépôts qui s'accrochaient au filet racinaire.",
    "<strong>Un entretien programmé</strong>&nbsp;: quand la reprise est lente et la "
    "réparation lourde, un curage tous les deux ans coûte moins cher qu'une tranchée.",
    "<strong>Le remplacement de la portion défectueuse</strong>&nbsp;: c'est la seule "
    "solution définitive quand le joint ou le tuyau est déchaussé sur plusieurs mètres.",
    "<strong>L'abattage ou l'éloignement de la plantation</strong>&nbsp;: rarement la "
    "première option, mais parfois la plus raisonnable si l'arbre est jeune et mal placé.",
    "Dans tous les cas, on décide après avoir vu l'image, pas avant."],
   ),
 ],
 "faq": [
  ("Mon voisin a un arbre dont les racines bouchent ma canalisation, que faire&nbsp;?",
   "Commencez par documenter&nbsp;: l'inspection caméra localise l'entrée des racines et "
   "le rapport constitue une pièce. La suite se règle d'abord à l'amiable&nbsp;; les "
   "règles de distance de plantation et de responsabilité existent, mais un dossier "
   "technique vaut mieux qu'une discussion de principe."),
  ("Combien de temps avant que les racines reviennent après un fraisage&nbsp;?",
   "Selon l'essence et la saison, comptez généralement d'un à trois ans si le défaut "
   "d'entrée n'est pas traité. C'est précisément pour cela que nous vous disons, après "
   "inspection, si un curage périodique suffit ou si la portion doit être reprise."),
  ("Une canalisation en PVC est-elle à l'abri&nbsp;?",
   "Mieux protégée que le grès, dont les joints sont les points faibles, mais pas "
   "invulnérable&nbsp;: un emboîtement mal fait ou une fissure après tassement suffit. "
   "Les réseaux anciens en grès ou en fonte restent les plus concernés."),
  ("Intervenez-vous sur tout le Finistère pour une inspection caméra&nbsp;?",
   "Oui, de Brest à Quimper et Morlaix comme sur les communes littorales et rurales. Le "
   "diagnostic est remis par écrit, avec la localisation du défaut."),
 ],
},

{
 "slug": "regard-assainissement-qui-deborde-finistere",
 "court": "Regard qui déborde (29)",
 "dept": "29", "act": "degorgement", "date": "2026-09-30",
 "titre": "Regard d'assainissement qui déborde (29) — ETS-BZH",
 "h1": "Regard qui déborde dans le jardin&nbsp;: ce que cela dit de votre réseau",
 "meta": ("Regard d'assainissement qui déborde en Finistère : lire le niveau dans les "
          "regards pour situer le bouchon, et savoir qui intervient. 02 20 06 00 75."),
 "mots_cles": ("regard qui déborde, regard assainissement plein, bouchon branchement "
               "eaux usées, débouchage Finistère, limite de propriété assainissement"),
 "chapo": ("Le regard du jardin est plein, parfois il déborde, et la maison commence à "
           "mal s'évacuer. C'est désagréable, mais c'est surtout une information "
           "précieuse&nbsp;: en ouvrant les regards dans le bon ordre, on situe le "
           "bouchon en quelques minutes — et on sait à qui revient l'intervention."),
 "urgent": [
   "Arrêtez tout rejet d'eau dans la maison&nbsp;: chaque litre aggrave le "
   "débordement.",
   "Écartez enfants et animaux de la zone, et ne marchez pas dans les eaux "
   "répandues.",
   "Ouvrez les tampons des regards en vous écartant, sans vous pencher au-dessus.",
   "Notez lesquels sont pleins et lesquels sont vides&nbsp;: c'est exactement ce que "
   "nous vous demanderons au téléphone.",
   "Photographiez avant nettoyage.",
 ],
 "danger": ("Ne descendez jamais dans un regard, même peu profond, et n'y plongez pas "
            "la tête. Les gaz de fermentation s'accumulent dans ces volumes fermés et "
            "endorment l'odorat avant d'assommer. On ouvre, on recule, on laisse "
            "ventiler. Rien de ce qu'il y a à voir ne justifie de s'y pencher."),
 "sections": [
  ("Lire les regards comme une carte",
   ["Une installation comporte en général plusieurs regards en chaîne&nbsp;: un près de "
    "la maison, parfois un intermédiaire, et un regard de branchement à l'approche de la "
    "limite de propriété. L'eau va de l'un à l'autre. Le bouchon se trouve toujours "
    "juste après le dernier regard plein.",
    "<strong>Le regard près de la maison est plein, celui du bas est vide</strong>&nbsp;: "
    "le bouchon est entre les deux, sur votre terrain.",
    "<strong>Tous les regards sont pleins jusqu'au dernier</strong>&nbsp;: le bouchon "
    "est en aval du dernier regard, donc sur le branchement, à la limite ou au-delà.",
    "<strong>Les regards sont vides mais la maison refoule</strong>&nbsp;: le bouchon "
    "est en amont, entre les appareils et le premier regard — donc à l'intérieur.",
    "Ce simple relevé fait gagner une heure sur place, et il oriente aussi la question "
    "de la prise en charge."],
   None),
  ("Où s'arrête votre responsabilité",
   ["La règle générale est simple à énoncer&nbsp;: la partie du branchement située en "
    "domaine privé est à votre charge, la partie située sous le domaine public relève du "
    "service d'assainissement de la collectivité. Le regard de branchement matérialise "
    "en général cette limite.",
    "En pratique, la répartition exacte dépend du règlement de service de votre "
    "commune ou de votre communauté d'agglomération, et il vaut la peine de le "
    "consulter une fois pour toutes&nbsp;: certains services prennent en charge le "
    "branchement jusqu'au regard, d'autres s'arrêtent à la limite de propriété.",
    "Si le relevé des regards montre que le bouchon est en aval du dernier regard, "
    "appelez le service d'assainissement avant de faire intervenir à vos frais. Nous "
    "vous le dirons d'ailleurs au téléphone si votre description le laisse penser&nbsp;: "
    "il n'y a aucun intérêt à vous déplacer une entreprise pour un ouvrage qui ne vous "
    "appartient pas."],
   None),
  ("Pourquoi cela arrive plus souvent ici",
   [],
   ["Des réseaux enterrés anciens en grès ou en fonte, aux joints fragiles, dans les "
    "bourgs et le centre de Brest.",
    "Des haies et talus plantés au-dessus des tracés&nbsp;: les racines entrent par les "
    "joints.",
    "Des eaux pluviales raccordées par erreur sur le réseau d'eaux usées, qui saturent "
    "le branchement à chaque gros épisode pluvieux.",
    "Des résidences secondaires où le réseau sèche plusieurs mois puis reçoit un usage "
    "intense en quelques semaines.",
    "Des tampons de regard mal refermés, par lesquels terre et feuilles finissent dans "
    "le réseau.",
    "Sur les communes littorales, des collecteurs qui évacuent moins bien à marée "
    "haute&nbsp;: un refoulement toujours aux mêmes heures n'est pas une coïncidence."],
   ),
 ],
 "faq": [
  ("Puis-je déboucher moi-même depuis le regard&nbsp;?",
   "Un furet manuel depuis un regard accessible traite parfois un bouchon proche. Mais "
   "sans savoir dans quelle direction ni sur quelle distance travailler, on tasse plus "
   "souvent qu'on ne débouche&nbsp;— et on ne voit pas la cause. Le relevé des regards "
   "d'abord, l'intervention ensuite."),
  ("Le regard se remplit dès qu'il pleut fort, est-ce normal&nbsp;?",
   "Non, et cela signale en général des eaux pluviales raccordées au réseau d'eaux "
   "usées, ou un réseau public saturé. Dans le premier cas, la correction est chez vous&nbsp;; "
   "dans le second, un clapet anti-retour protège votre maison."),
  ("Faut-il curer les regards régulièrement&nbsp;?",
   "Un contrôle visuel une à deux fois par an suffit sur une installation saine, et un "
   "hydrocurage préventif tous les deux à trois ans sur une maison individuelle évite "
   "les mauvaises surprises. C'est peu de chose comparé à une urgence un dimanche."),
  ("Intervenez-vous le dimanche sur le littoral&nbsp;?",
   "Oui, l'astreinte couvre les nuits, les week-ends et les jours fériés sur "
   "l'ensemble du Finistère, y compris les communes de la côte et de la presqu'île."),
 ],
},

{
 "slug": "fuite-sous-evier-finistere",
 "court": "Fuite sous l'évier (29)",
 "dept": "29", "act": "plomberie", "date": "2026-09-30",
 "titre": "Fuite sous l'évier (29) : couper vite, réparer juste — ETS-BZH",
 "h1": "Fuite sous l'évier ou le lavabo&nbsp;: couper en trente secondes, puis chercher",
 "meta": ("Fuite sous l'évier ou le lavabo en Finistère : couper la bonne vanne, "
          "identifier le point de fuite et éviter le meuble gonflé. 02 20 06 00 75."),
 "mots_cles": ("fuite sous évier, flexible qui fuit, robinet d'arrêt sous évier, "
               "joint siphon qui fuit, plombier urgence Brest"),
 "chapo": ("Une fuite sous un meuble de cuisine se remarque toujours trop tard&nbsp;: "
           "quand le fond du meuble gonfle, l'eau coule depuis des jours. La bonne "
           "nouvelle, c'est que presque tout ce qui fuit à cet endroit se répare en une "
           "intervention courte. Encore faut-il couper au bon endroit et savoir "
           "distinguer une fuite d'arrivée d'une fuite d'évacuation."),
 "urgent": [
   "Videz le meuble et essuyez&nbsp;: vous verrez immédiatement si l'eau revient, et "
   "d'où.",
   "Cherchez les deux petits robinets d'arrêt sous l'évier, un par flexible, et "
   "fermez-les. S'ils sont absents ou grippés, coupez l'arrivée générale.",
   "Faites le test simple&nbsp;: si l'eau coule en permanence, c'est l'arrivée sous "
   "pression. Si elle ne coule que quand vous utilisez l'évier, c'est l'évacuation.",
   "Glissez une bassine et surélevez ce qui est stocké dessous — produits, cartons, "
   "électroménager.",
 ],
 "danger": ("Sous un évier se trouvent souvent une prise et l'alimentation du "
            "lave-vaisselle. Si l'eau a atteint une prise ou un bloc multiprise, ne le "
            "manipulez pas&nbsp;: coupez le circuit correspondant au tableau avant de "
            "débrancher quoi que ce soit. Un meuble bas de cuisine humide et une "
            "multiprise au sol sont une association fréquente et dangereuse."),
 "sections": [
  ("Arrivée ou évacuation : le diagnostic en un test",
   ["C'est la première question, et elle se tranche sans outil. Une <strong>fuite "
    "d'arrivée</strong> est sous pression en permanence&nbsp;: elle coule même si "
    "personne ne touche au robinet, souvent en jet fin ou en goutte régulière. Une "
    "<strong>fuite d'évacuation</strong> ne se manifeste que pendant et juste après "
    "l'usage&nbsp;: on ouvre le robinet, ça goutte&nbsp;; on ferme, ça s'arrête.",
    "Côté arrivée, les coupables sont peu nombreux&nbsp;: le flexible de robinet, dont "
    "la tresse se fatigue et finit par percer, l'écrou de raccordement, ou le robinet "
    "d'arrêt lui-même dont le presse-étoupe suinte. Les flexibles sont des "
    "consommables&nbsp;: sur une installation de plus de dix ans, ils se remplacent sans "
    "état d'âme.",
    "Côté évacuation, c'est le siphon ou l'un de ses joints, le raccord de "
    "lave-vaisselle mal serré, ou la bonde de l'évier dont le joint s'est écrasé. "
    "Aucune de ces pièces n'est coûteuse, et aucune ne demande de gros travaux."],
   None),
  ("Le vrai dégât n'est pas la fuite, c'est le meuble",
   ["Quelques gouttes par heure font un litre par jour. Dans un meuble fermé, sans "
    "ventilation, ce litre ne s'évapore pas&nbsp;: il imprègne le panneau de particules "
    "du fond, qui gonfle, se délite, et entraîne la façade et le plan de travail.",
    "En Finistère, l'humidité ambiante est déjà élevée une bonne partie de l'année, et "
    "beaucoup de cuisines de maisons anciennes sont installées contre un mur en pierre "
    "qui respire mal derrière un meuble. Une petite fuite met deux fois plus de temps à "
    "sécher qu'ailleurs, et les moisissures s'installent vite.",
    "Réflexe utile&nbsp;: une fois par an, sortez ce qu'il y a sous l'évier et passez la "
    "main au fond du meuble. Un panneau légèrement bombé ou un point noir au niveau du "
    "siphon annonce une fuite qui n'a pas encore été vue. C'est l'inspection la plus "
    "rentable de la maison, et elle prend deux minutes."],
   None),
  ("Ce qui se remplace en une intervention",
   [],
   ["Les flexibles d'alimentation, systématiquement par paire.",
    "Les robinets d'arrêt sous évier, souvent grippés faute d'avoir jamais été "
    "manœuvrés — et c'est ce qui vous permettra de couper la prochaine fois.",
    "Le siphon complet, joints compris, quand les joints sont durcis.",
    "La bonde et son joint, quand la fuite apparaît à la jonction avec la cuve.",
    "Le raccord d'évacuation du lave-vaisselle ou du lave-linge, souvent simplement "
    "emboîté et jamais collerisé.",
    "Le mitigeur lui-même s'il fuit à la base&nbsp;: la cartouche ou l'ensemble, selon "
    "l'état."],
   ),
 ],
 "faq": [
  ("Mes robinets d'arrêt sont bloqués, comment couper&nbsp;?",
   "Coupez l'arrivée générale du logement, puis ouvrez un robinet en point bas pour "
   "faire tomber la pression. Ne forcez pas sur un robinet d'arrêt grippé&nbsp;: il "
   "casse, et la fuite devient franche. Leur remplacement fait partie de l'intervention."),
  ("Combien coûte la réparation d'une fuite sous évier&nbsp;?",
   "Cela reste une intervention courte dans la grande majorité des cas. Le devis est "
   "gratuit et le tarif validé avec vous avant le démarrage&nbsp;: la facture ne dépasse "
   "jamais le devis accepté."),
  ("Mon meuble est déjà gonflé, l'assurance intervient-elle&nbsp;?",
   "Un dégât des eaux consécutif à une fuite accidentelle est généralement couvert, "
   "selon les termes de votre contrat. Photographiez avant réparation, conservez notre "
   "facture détaillée, et déclarez dans le délai prévu."),
  ("Puis-je juste resserrer l'écrou qui goutte&nbsp;?",
   "Souvent oui, d'un huitième de tour, à la main ou à la clé sans forcer. Si cela ne "
   "suffit pas, le joint est en cause et il faut démonter&nbsp;: insister sur le serrage "
   "fend l'écrou plastique et aggrave franchement la situation."),
 ],
},

{
 "slug": "chasse-d-eau-qui-fuit-en-continu-finistere",
 "court": "Chasse d'eau qui fuit (29)",
 "dept": "29", "act": "plomberie", "date": "2026-09-30",
 "titre": "Chasse d'eau qui fuit (29) : la facture invisible — ETS-BZH",
 "h1": "Chasse d'eau qui fuit en continu&nbsp;: le filet d'eau qui coûte le plus cher",
 "meta": ("Chasse d'eau qui fuit en continu en Finistère : le test du papier, les deux "
          "pièces en cause et le coût réel du filet d'eau. 02 20 06 00 75."),
 "mots_cles": ("chasse d'eau qui fuit, WC qui coule en permanence, joint de clapet, "
               "robinet flotteur, surconsommation d'eau Finistère"),
 "chapo": ("Un filet d'eau qui ruisselle dans la cuvette ne fait pas de bruit, ne cause "
           "aucun dégât et n'inquiète personne. C'est pourtant la fuite la plus coûteuse "
           "d'un logement&nbsp;: elle passe inaperçue pendant des mois et se voit "
           "uniquement sur la facture, quand il est trop tard pour agir."),
 "urgent": [
   "Faites le test du papier&nbsp;: posez une feuille de papier toilette contre la "
   "paroi arrière de la cuvette, au-dessus du niveau d'eau. Si elle se mouille, il y a "
   "fuite.",
   "Fermez le robinet d'arrêt du WC — le petit robinet sur l'alimentation — pour "
   "arrêter la consommation en attendant.",
   "Relevez votre compteur le soir et le lendemain matin sans rien consommer&nbsp;: "
   "vous mesurerez l'ampleur exacte.",
   "Ouvrez le réservoir et regardez si l'eau s'échappe par le clapet du fond ou par "
   "le trop-plein.",
 ],
 "danger": ("Ne calez pas le mécanisme avec un objet et ne bloquez pas le flotteur "
            "pour arrêter la fuite&nbsp;: sur un réservoir dont le trop-plein déborde, "
            "vous transformez un écoulement contrôlé vers la cuvette en débordement "
            "dans la pièce. Fermez le robinet d'arrêt, c'est plus sûr et c'est fait pour."),
 "sections": [
  ("Deux pièces, deux symptômes",
   ["Un réservoir de WC ne comporte que deux organes susceptibles de fuir, et ils se "
    "distinguent facilement en soulevant le couvercle.",
    "<strong>Le clapet de vidage</strong>, au fond du réservoir, referme le passage vers "
    "la cuvette après la chasse. Son joint se tartre, se déforme, ou un dépôt s'y coince. "
    "Symptôme&nbsp;: le niveau du réservoir baisse tout seul, et un filet d'eau descend "
    "en permanence dans la cuvette. C'est le cas le plus fréquent.",
    "<strong>Le robinet flotteur</strong>, sur le côté, remplit le réservoir et doit se "
    "fermer au bon niveau. Quand il ne ferme plus, l'eau monte jusqu'au trop-plein et "
    "s'écoule par là. Symptôme&nbsp;: le réservoir est plein à ras et le bruit de "
    "remplissage ne s'arrête jamais.",
    "Dans les deux cas, ce sont des pièces courantes que nos véhicules ont à bord. "
    "L'intervention est brève, et elle ne nécessite pas de changer le WC."],
   None),
  ("Ce que cela coûte réellement",
   ["Un filet d'eau continu dans une cuvette représente un volume que personne "
    "n'imagine. Selon l'ouverture, on parle de plusieurs dizaines à plusieurs centaines "
    "de litres par jour, sans aucun signe dans le logement. Sur une année, cela se "
    "compte en dizaines de mètres cubes.",
    "Le problème est que rien ne vous alerte&nbsp;: pas de flaque, pas de bruit fort, "
    "pas de dégât. La découverte se fait à la facture annuelle, et à ce moment-là le "
    "volume est consommé — et il vous sera facturé, car une fuite sur un appareil "
    "sanitaire n'ouvre pas droit aux mêmes dispositifs d'écrêtement qu'une fuite sur "
    "canalisation enterrée.",
    "Le réflexe qui protège tient en une minute par trimestre&nbsp;: relever le compteur "
    "le soir, ne rien consommer pendant la nuit, et le relire au réveil. Un index qui a "
    "bougé, c'est une fuite quelque part. Dans une résidence secondaire du littoral "
    "finistérien, ce contrôle est encore plus rentable&nbsp;: une chasse qui fuit d'octobre "
    "à avril consomme dans une maison vide."],
   None),
  ("Les autres fuites silencieuses du logement",
   [],
   ["Le mitigeur qui goutte&nbsp;: une cartouche à changer, quelques minutes.",
    "Le groupe de sécurité du chauffe-eau qui coule en dehors des phases de chauffe.",
    "Le robinet extérieur de jardin, qui fuit sans que personne le voie.",
    "Le trop-plein de l'adoucisseur, qui s'écoule à l'égout en continu quand la vanne "
    "est en défaut.",
    "Une chasse de WC dans une pièce peu utilisée — chambre d'amis, dépendance, "
    "location&nbsp;: c'est là que la fuite dure le plus longtemps.",
    "Le remplissage automatique d'une piscine, qui masque parfaitement une fuite du "
    "bassin."],
   ),
 ],
 "faq": [
  ("Le test du papier est négatif mais mon compteur tourne&nbsp;?",
   "Alors la fuite est ailleurs&nbsp;: autre WC, robinet, chauffe-eau, ou canalisation "
   "enterrée. Fermez la vanne d'arrivée de la maison et refaites l'essai&nbsp;: si le "
   "compteur tourne encore, la fuite est sur la portion enterrée, avant la maison."),
  ("Faut-il changer tout le mécanisme ou juste le joint&nbsp;?",
   "Sur un mécanisme récent et en bon état, le joint de clapet suffit souvent. Sur un "
   "ensemble ancien, entartré et dont les pièces ne se trouvent plus, remplacer le "
   "mécanisme complet coûte à peine plus cher et évite un second déplacement."),
  ("Puis-je obtenir un dégrèvement sur ma facture d'eau&nbsp;?",
   "Les dispositifs d'écrêtement visent les fuites sur canalisation après compteur, pas "
   "les appareils sanitaires comme une chasse d'eau ou un robinet. Renseignez-vous "
   "auprès de votre service des eaux, mais ne comptez pas dessus&nbsp;: la vraie réponse "
   "est de contrôler le compteur régulièrement."),
  ("Intervenez-vous pour une simple chasse d'eau&nbsp;?",
   "Oui, et c'est souvent l'intervention la plus rentable que nous faisons pour un "
   "client. Devis gratuit, tarif validé avant démarrage, sur l'ensemble du Finistère."),
 ],
},

{
 "slug": "plus-d-eau-au-robinet-finistere",
 "court": "Plus d'eau au robinet (29)",
 "dept": "29", "act": "plomberie", "date": "2026-09-30",
 "titre": "Plus d'eau au robinet (29) : les vérifications — ETS-BZH",
 "h1": "Plus une goutte au robinet&nbsp;: réseau, vanne, gel ou pompe&nbsp;?",
 "meta": ("Plus d'eau au robinet en Finistère : les vérifications dans l'ordre pour "
          "savoir si c'est le réseau, une vanne, le gel ou votre installation. "
          "02 20 06 00 75."),
 "mots_cles": ("plus d'eau au robinet, coupure d'eau, pression d'eau faible, vanne "
               "d'arrêt bloquée, plombier urgence Finistère"),
 "chapo": ("Le robinet crachote puis ne donne plus rien. Avant d'appeler qui que ce "
           "soit, quatre vérifications dans l'ordre permettent de savoir si le problème "
           "vient du réseau public, de votre branchement, d'une vanne ou d'un gel — et "
           "elles évitent un déplacement inutile."),
 "urgent": [
   "Testez plusieurs robinets, à l'étage et au rez-de-chaussée&nbsp;: si un seul est "
   "concerné, c'est lui ou son alimentation.",
   "Demandez aux voisins immédiats&nbsp;: une coupure générale sur le secteur se "
   "confirme en trente secondes.",
   "Vérifiez la vanne d'arrêt générale de la maison et celle du compteur&nbsp;: "
   "elles doivent être en position ouverte.",
   "Fermez tous les robinets et regardez si le compteur tourne&nbsp;: s'il tourne "
   "alors que rien ne coule chez vous, l'eau part ailleurs — il y a une rupture.",
 ],
 "danger": ("Après une coupure, ne buvez pas la première eau qui revient et ne la "
            "faites pas passer dans un appareil&nbsp;: elle entraîne les dépôts décollés "
            "dans le réseau. Ouvrez d'abord un robinet en point bas, laissez couler "
            "jusqu'à ce que l'eau soit claire, et nettoyez ensuite les mousseurs, qui "
            "auront capté le gravier."),
 "sections": [
  ("La démarche dans l'ordre",
   ["<strong>Un seul robinet est sec.</strong> Le mousseur est colmaté, ou le petit "
    "robinet d'arrêt sous l'appareil est fermé ou grippé. C'est la panne la plus "
    "fréquente et la plus vite réglée.",
    "<strong>Toute la maison est sèche, les voisins aussi.</strong> C'est le réseau "
    "public&nbsp;: intervention programmée, casse sur une conduite, ou manœuvre du "
    "service des eaux. Le numéro figure sur votre facture d'eau, et les services publient "
    "généralement les coupures en cours.",
    "<strong>Toute la maison est sèche, les voisins non.</strong> Le problème est sur "
    "votre branchement ou dans la maison&nbsp;: vanne fermée, filtre colmaté, "
    "réducteur de pression bloqué, ou conduite rompue.",
    "<strong>La pression est faible mais il y a de l'eau.</strong> Regardez du côté du "
    "filtre en entrée, du réducteur de pression, ou d'un mousseur entartré. Une baisse "
    "générale et progressive vient souvent du filtre que personne n'a nettoyé depuis "
    "l'installation."],
   None),
  ("En Finistère, deux causes saisonnières",
   ["<strong>Le gel.</strong> Le climat breton descend rarement bas, et c'est le "
    "piège&nbsp;: peu d'installations sont protégées. Un compteur en regard extérieur, "
    "une conduite en garage non chauffé ou dans une dépendance, et deux nuits à "
    "-4&nbsp;°C suffisent. Le symptôme est net&nbsp;: plus rien nulle part, un matin de "
    "gel, sans coupure sur le secteur. Ne chauffez jamais un tuyau à la flamme, et "
    "gardez à l'esprit que la fuite se déclare souvent au moment où la glace cède.",
    "<strong>La saison touristique.</strong> Sur les communes littorales et les "
    "presqu'îles, la population est multipliée en été et la pression du réseau chute "
    "aux heures de pointe, en fin de journée. Ce n'est pas une panne&nbsp;: c'est un "
    "réseau à sa limite. Si votre pression est structurellement faible, un surpresseur "
    "règle la situation.",
    "Les maisons alimentées par un puits ou un forage privé ajoutent une troisième "
    "cause&nbsp;: la pompe, son clapet, son ballon ou son pressostat, qui lâchent "
    "presque toujours au pire moment."],
   None),
  ("Ce que nous vérifions à l'arrivée",
   [],
   ["Le compteur et sa vanne, ainsi que l'état du regard si le compteur est extérieur.",
    "La vanne générale d'entrée et le clapet anti-retour.",
    "Le filtre d'entrée et le réducteur de pression, très souvent en cause dans les "
    "baisses progressives.",
    "La pression mesurée en entrée et en point haut&nbsp;: c'est ce qui distingue un "
    "défaut de réseau d'un défaut d'installation.",
    "La recherche d'une rupture si le compteur tourne alors que tout est fermé.",
    "La pompe, le ballon et le pressostat sur les installations alimentées par forage."],
   ),
 ],
 "faq": [
  ("L'eau est revenue mais elle est marron, est-ce grave&nbsp;?",
   "C'est en général le dépôt du réseau remis en suspension par la coupure. Laissez "
   "couler un robinet en point bas jusqu'à ce que l'eau redevienne claire, sans passer "
   "par un adoucisseur ni un appareil électroménager, et nettoyez ensuite les mousseurs. "
   "Si la coloration persiste au-delà, appelez le service des eaux."),
  ("Ma pression est faible uniquement à l'étage, pourquoi&nbsp;?",
   "Parce que la pression disponible diminue avec la hauteur. Si elle est juste au "
   "départ, l'étage en pâtit le premier. Un réducteur mal réglé, un filtre colmaté ou "
   "un diamètre insuffisant aggravent le phénomène&nbsp;; un surpresseur le corrige."),
  ("Mon compteur tourne alors que tout est fermé&nbsp;?",
   "Il y a une fuite quelque part entre le compteur et vos robinets. Fermez la vanne "
   "d'entrée de la maison&nbsp;: si le compteur tourne encore, la fuite est sur la "
   "portion enterrée, ce qui demande une recherche avant de creuser."),
  ("Intervenez-vous en urgence pour une coupure d'eau&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur le Finistère, dès lors que le problème est sur votre "
   "installation. Si votre description indique une coupure du réseau public, nous vous "
   "le dirons au téléphone plutôt que de nous déplacer pour rien."),
 ],
},

{
 "slug": "surtension-apres-orage-finistere",
 "court": "Surtension après orage (29)",
 "dept": "29", "act": "electricite", "date": "2026-09-30",
 "titre": "Appareils grillés après un orage (29) : que faire — ETS-BZH",
 "h1": "Surtension après un orage en Finistère&nbsp;: appareils grillés, que faire ensuite",
 "meta": ("Appareils grillés par une surtension après un orage en Finistère : ce qu'il "
          "faut vérifier, les preuves à réunir et comment se protéger. 02 20 06 00 75."),
 "mots_cles": ("surtension orage appareils grillés, parafoudre, foudre installation "
               "électrique, électricien Brest, déclaration assurance surtension"),
 "chapo": ("Après l'orage, la box ne redémarre plus, le lave-vaisselle affiche un code, "
           "la plaque ne répond plus. Une surtension n'a pas besoin d'un impact direct "
           "pour faire des dégâts&nbsp;: une décharge à plusieurs centaines de mètres "
           "suffit. Voici quoi vérifier, quoi conserver pour l'assurance, et comment "
           "éviter la prochaine."),
 "urgent": [
   "Coupez les circuits concernés au tableau avant de manipuler un appareil qui a "
   "grillé.",
   "Ne rebranchez pas un appareil qui sent le brûlé ou qui a fumé, même s'il "
   "semble fonctionner.",
   "Faites la liste des appareils touchés, avec photos, marques et modèles&nbsp;: "
   "c'est la pièce centrale du dossier d'assurance.",
   "Vérifiez le tableau&nbsp;: trace noire, odeur, appareil qui ne se réarme plus. "
   "Une surtension a pu l'atteindre en premier.",
   "Notez l'heure de l'orage&nbsp;: elle sera demandée, et elle est vérifiable.",
 ],
 "danger": ("Un appareil qui a subi une surtension peut fonctionner en apparence tout "
            "en ayant une isolation dégradée à l'intérieur. S'il a fumé, senti le "
            "brûlé, ou si son boîtier a chauffé, ne le remettez pas en service&nbsp;: le "
            "défaut ressortira, et cette fois sous forme d'échauffement ou de choc "
            "électrique. C'est particulièrement vrai pour les appareils reliés à l'eau."),
 "sections": [
  ("Par où la surtension est entrée",
   ["Contrairement à l'image que l'on s'en fait, la foudre n'a pas besoin de tomber sur "
    "la maison. Trois chemins d'entrée expliquent la quasi-totalité des dégâts.",
    "<strong>Par le réseau électrique.</strong> Une décharge sur une ligne à plusieurs "
    "centaines de mètres se propage jusqu'aux prises. C'est le chemin le plus courant.",
    "<strong>Par la ligne téléphonique ou la fibre.</strong> Les box, décodeurs et "
    "modems sont les victimes les plus fréquentes, parce qu'ils sont raccordés à deux "
    "réseaux en même temps — courant et données — et servent de passage entre les deux.",
    "<strong>Par l'antenne de télévision.</strong> Un mât en toiture est un point haut, "
    "et le câble descend directement vers le téléviseur.",
    "Le Finistère est particulièrement exposé aux épisodes venteux et orageux "
    "atlantiques, et le réseau y compte encore de longues portions aériennes, notamment "
    "sur les communes rurales et les presqu'îles. C'est ce qui explique que les "
    "surtensions y soient plus fréquentes que la moyenne."],
   None),
  ("Le parafoudre : ce qu'il fait, ce qu'il ne fait pas",
   ["Un parafoudre se pose dans le tableau électrique, en tête d'installation. Son rôle "
    "est d'écrêter les pointes de tension et de les diriger vers la terre avant qu'elles "
    "n'atteignent vos appareils. Il ne supprime pas le risque, il le réduit fortement.",
    "Deux conditions font toute son efficacité. La première est une <strong>prise de "
    "terre en bon état</strong>&nbsp;: sans elle, le parafoudre n'a nulle part où "
    "envoyer l'énergie, et il ne sert à rien. C'est la première chose que nous mesurons. "
    "La seconde est la <strong>protection des autres arrivées</strong>&nbsp;: un "
    "parafoudre sur le tableau ne protège pas une box attaquée par la ligne de données.",
    "La réglementation impose le parafoudre dans certaines zones et configurations, "
    "notamment lorsque l'alimentation est en aérien dans des départements à forte "
    "densité de foudroiement, ou en présence d'un paratonnerre. Au-delà de l'obligation, "
    "c'est un équipement dont le coût se compare vite à celui d'une box, d'un "
    "téléviseur et d'un lave-vaisselle remplacés la même nuit."],
   None),
  ("Constituer le dossier d'assurance",
   [],
   ["Photographier chaque appareil touché, y compris les traces sur les prises.",
    "Conserver les appareils défectueux&nbsp;: l'expert peut demander à les voir, et "
    "les jeter affaiblit le dossier.",
    "Retrouver factures d'achat ou preuves de possession, même anciennes.",
    "Noter la date et l'heure de l'épisode orageux.",
    "Demander un rapport d'intervention à l'électricien&nbsp;: un constat "
    "professionnel de l'origine électrique du sinistre pèse dans l'instruction.",
    "Déclarer dans le délai prévu par le contrat, sans attendre d'avoir tout chiffré."],
   ),
 ],
 "faq": [
  ("Mon assurance couvre-t-elle les appareils grillés par la foudre&nbsp;?",
   "La plupart des contrats multirisque habitation comportent une garantie dommages "
   "électriques, avec des plafonds et des franchises qui varient beaucoup d'un contrat "
   "à l'autre. Relisez cette clause&nbsp;: c'est là que se joue l'indemnisation, pas dans "
   "la discussion sur l'origine."),
  ("Une multiprise « parafoudre » suffit-elle&nbsp;?",
   "Elle protège un peu, à l'échelle d'un appareil, et seulement contre des surtensions "
   "modérées. Elle ne remplace pas un parafoudre de tableau, qui intervient en tête "
   "d'installation et encaisse une énergie sans commune mesure."),
  ("Puis-je tout rebrancher dès que le courant revient&nbsp;?",
   "Attendez la fin de l'épisode orageux, et rebranchez appareil par appareil en "
   "surveillant. Si un différentiel saute au rebranchement d'un appareil précis, c'est "
   "que son isolement est atteint&nbsp;: laissez-le débranché."),
  ("Intervenez-vous après un orage en Finistère&nbsp;?",
   "Oui, 24h/24 et 7j/7. Après un épisode important, les demandes arrivent en "
   "nombre&nbsp;: nous annonçons un délai réaliste dès l'appel et traitons en priorité "
   "les situations à risque — odeur de brûlé, tableau touché, installation mouillée."),
 ],
},

{
 "slug": "installation-electrique-inondee-finistere",
 "court": "Installation inondée (29)",
 "dept": "29", "act": "electricite", "date": "2026-09-30",
 "titre": 'Installation électrique inondée (29) — ETS-BZH',
 "h1": "Installation électrique mouillée&nbsp;: pourquoi on ne remet jamais le courant sans contrôle",
 "meta": ("Installation électrique inondée ou mouillée en Finistère : les gestes, "
          "pourquoi attendre le contrôle d'isolement, et ce qui se remplace. "
          "02 20 06 00 75."),
 "mots_cles": ("installation électrique inondée, tableau électrique mouillé, contrôle "
               "isolement, remise en service après dégât des eaux, électricien Finistère"),
 "chapo": ("Une infiltration en toiture, une fuite à l'étage, un sous-sol qui a pris "
           "l'eau&nbsp;: dès qu'une installation électrique est mouillée, la question "
           "n'est plus de savoir si ça marche encore, mais si c'est sûr. Et cela ne se "
           "décide pas à l'œil&nbsp;: cela se mesure."),
 "urgent": [
   "Coupez l'alimentation du secteur concerné au tableau. Si l'eau est proche du "
   "tableau lui-même, coupez le disjoncteur de branchement, en amont.",
   "N'entrez pas dans une pièce inondée avant d'avoir coupé, et jamais pieds nus.",
   "Ne débranchez aucun appareil resté dans l'eau tant que le circuit est sous "
   "tension.",
   "Laissez le courant coupé sur ce secteur, même si tout semble sec&nbsp;: c'est le "
   "point le plus important de cette page.",
   "Photographiez tout avant nettoyage&nbsp;: niveau atteint, appareils, tableau.",
 ],
 "danger": ("Une installation peut être sèche en surface et saturée à l'intérieur. "
            "L'eau circule dans les gaines par capillarité et stagne dans les boîtes de "
            "dérivation et les points bas des conduits, parfois pendant des semaines. "
            "Remettre sous tension sur la seule impression que « ça a séché » est la "
            "faute la plus courante après un dégât des eaux — et la plus dangereuse, "
            "parce que le défaut se manifeste alors sur un contact humain."),
 "sections": [
  ("Pourquoi le contrôle d'isolement ne se remplace pas par une observation",
   ["Ce que l'on mesure après un sinistre n'est pas la présence d'eau, c'est la "
    "<strong>résistance d'isolement</strong>&nbsp;: la capacité des gaines et des "
    "conducteurs à empêcher le courant de partir là où il ne doit pas. L'humidité fait "
    "chuter cette valeur bien avant qu'elle ne provoque une panne visible.",
    "Le contrôle se fait circuit par circuit, avec un appareil de mesure, installation "
    "hors tension. Il donne trois réponses possibles&nbsp;: le circuit est sain et peut "
    "être remis en service&nbsp;; il est dégradé et doit sécher avant nouveau "
    "contrôle&nbsp;; il est compromis et doit être repris.",
    "C'est aussi ce contrôle qui permet de remettre le courant <em>partiellement</em>, "
    "ce qui compte énormément dans une maison sinistrée&nbsp;: on isole les circuits "
    "atteints et on rétablit le reste, plutôt que de laisser tout le logement dans le "
    "noir pendant l'assèchement."],
   None),
  ("Ce qui se remplace, ce qui se sèche",
   ["Tout ne se jette pas, et tout ne se garde pas. La ligne de partage est assez nette.",
    "<strong>Se remplace systématiquement</strong>&nbsp;: tout appareillage immergé — "
    "prises, interrupteurs, boîtes de dérivation — et tout matériel du tableau ayant été "
    "en contact avec l'eau. Un disjoncteur ou un différentiel mouillé ne se sèche pas "
    "et ne se répare pas&nbsp;: son mécanisme interne et ses contacts sont atteints, et "
    "la protection qu'il est censé assurer n'est plus garantie.",
    "<strong>Peut sécher et être recontrôlé</strong>&nbsp;: les circuits dont seules les "
    "gaines ont pris l'humidité, sans immersion prolongée. On sèche, on ventile, on "
    "remesure. Cela peut prendre plusieurs semaines dans une maison en pierre.",
    "<strong>Doit être repris</strong>&nbsp;: les circuits dont l'isolement reste "
    "insuffisant après séchage, et les installations anciennes sans protection "
    "différentielle, où le défaut ne serait de toute façon jamais détecté.",
    "Dans les maisons finistériennes en pierre, l'assèchement est plus long qu'ailleurs "
    "et un mur peut rester humide des mois. C'est une raison de plus pour mesurer plutôt "
    "que d'estimer."],
   None),
  ("L'ordre des choses après un dégât des eaux",
   [],
   ["Couper, sécuriser, photographier.",
    "Arrêter l'origine de l'eau — c'est la priorité absolue, avant tout le reste.",
    "Faire contrôler l'installation et rétablir les circuits sains.",
    "Déclarer à l'assurance, avec le rapport d'intervention à l'appui.",
    "Assécher réellement&nbsp;: ventilation, chauffage doux, temps. C'est long et cela "
    "ne se contourne pas.",
    "Faire recontrôler avant remise en service définitive des circuits qui avaient été "
    "isolés.",
    "Ne refermer, ne recouvrir et ne repeindre qu'après."],
   ),
 ],
 "faq": [
  ("Le courant marche encore, dois-je vraiment couper&nbsp;?",
   "Oui. Le fait que ça fonctionne ne dit rien de la sécurité&nbsp;: un défaut "
   "d'isolement ne coupe pas le courant, il crée un chemin de fuite. En l'absence de "
   "différentiel 30&nbsp;mA, rien ne l'interrompra avant qu'une personne ne le referme."),
  ("Combien de temps faut-il sécher avant remise en service&nbsp;?",
   "Il n'y a pas de durée standard&nbsp;: cela dépend du volume d'eau, des matériaux et "
   "de la ventilation, et cela va de quelques jours à plusieurs semaines. La seule "
   "réponse fiable est la mesure d'isolement, refaite après séchage."),
  ("L'assurance prend-elle en charge la remise en état électrique&nbsp;?",
   "Les dommages électriques consécutifs à un dégât des eaux sont généralement couverts "
   "selon les termes du contrat. Le rapport d'intervention, qui distingue ce qui est "
   "atteint de ce qui ne l'est pas, est la pièce qui fait avancer le dossier."),
  ("Intervenez-vous en urgence pour sécuriser&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur le Finistère. La première visite vise à couper ce qui doit "
   "l'être et à rétablir les circuits sains pour que le logement reste habitable&nbsp;; "
   "le contrôle définitif se fait après assèchement."),
 ],
},

# ----------------------------------------------- 35 — ILLE-ET-VILAINE (suite)
{
 "slug": "wc-bouche-en-appartement-ille-et-vilaine",
 "court": "WC bouché en appartement (35)",
 "dept": "35", "act": "degorgement", "date": "2026-09-30",
 "titre": "WC bouché en appartement (35) : qui paie quoi — ETS-BZH",
 "h1": "WC bouché en appartement à Rennes&nbsp;: ce qui vous revient, ce qui revient au syndic",
 "meta": ("WC bouché en appartement à Rennes : distinguer une évacuation privative "
          "d'une colonne commune, et savoir qui paie. Débouchage au 02 20 06 00 75."),
 "mots_cles": ("WC bouché appartement, qui paie débouchage location, colonne ou "
               "privatif, débouchage Rennes, charges copropriété canalisation"),
 "chapo": ("En maison, un WC bouché est une affaire simple. En appartement, la même "
           "panne soulève une question de plus&nbsp;: est-ce votre évacuation ou la "
           "colonne de l'immeuble&nbsp;? La réponse ne change rien à l'urgence, mais elle "
           "change tout à la facture — et elle se détermine en cinq minutes."),
 "urgent": [
   "Ne tirez pas la chasse une deuxième fois&nbsp;: la cuvette déborderait sur le "
   "sol, et en étage cela devient tout de suite un dégât des eaux.",
   "Écopez jusqu'à mi-hauteur, posez des serviettes, et tentez la ventouse à plat "
   "sur l'évacuation.",
   "Appelez un voisin du dessus et un du dessous&nbsp;: si eux aussi ont un "
   "problème, c'est la colonne, et vous arrêtez tout de suite d'essayer.",
   "Écoutez vos autres appareils&nbsp;: un gargouillis dans la douche ou l'évier "
   "quand vous tirez la chasse indique un bouchon en aval, pas dans la cuvette.",
 ],
 "danger": ("Ne versez pas de déboucheur chimique dans une cuvette qui ne s'évacue "
            "pas, et encore moins en immeuble&nbsp;: le produit stagne, il ne descend pas "
            "jusqu'au bouchon, et s'il y a refoulement, il ressort chez le voisin du "
            "dessous. Les projections lors du débouchage mécanique brûlent la peau et "
            "les yeux."),
 "sections": [
  ("Privatif ou commun : la frontière exacte",
   ["Dans un immeuble, la limite est claire dans son principe. La <strong>canalisation "
    "qui dessert votre seul logement</strong> — de la cuvette jusqu'à son raccordement — "
    "est privative&nbsp;: elle est à votre charge. La <strong>colonne verticale qui "
    "dessert plusieurs logements</strong> est une partie commune&nbsp;: elle relève de la "
    "copropriété, donc du syndic et des charges.",
    "En pratique, trois signes désignent la colonne. Plusieurs logements sont touchés "
    "en même temps. L'eau remonte chez vous alors que vous n'avez rien fait couler. Des "
    "glouglous remontent d'appareils situés à l'autre bout du logement quand un voisin "
    "utilise l'eau.",
    "À l'inverse, si vous êtes seul concerné et que l'immeuble fonctionne normalement, "
    "l'évacuation privative est en cause, et l'intervention est à votre charge — ou à "
    "celle de votre propriétaire selon la nature du défaut.",
    "Ce relevé ne prend que quelques minutes et il évite l'erreur la plus coûteuse&nbsp;: "
    "faire intervenir à titre personnel sur un ouvrage commun, puis tenter de se faire "
    "rembourser après coup."],
   None),
  ("Locataire ou propriétaire : l'autre question",
   ["Une fois établi que l'évacuation est privative, reste à savoir qui paie entre "
    "l'occupant et le bailleur. L'usage, largement appliqué, distingue l'entretien "
    "courant de la réparation.",
    "Le <strong>débouchage courant</strong> — un bouchon dû à l'usage — relève de "
    "l'entretien, donc du locataire. La <strong>réparation d'une canalisation dégradée, "
    "affaissée, fissurée ou entartrée par vétusté</strong> relève du propriétaire, parce "
    "qu'il s'agit alors d'un défaut de l'ouvrage et non d'un usage.",
    "C'est précisément pour trancher ce genre de situation que l'inspection caméra est "
    "utile. Elle montre l'état réel de la canalisation, et notre rapport écrit dit "
    "clairement si le bouchon vient d'un usage ou d'un défaut. Un document technique "
    "règle une discussion que les arguments ne règlent jamais.",
    "Sur Rennes, où le parc locatif est considérable et la rotation rapide, c'est un "
    "sujet quotidien&nbsp;: nous intervenons aussi bien pour des occupants que sur "
    "mandat de bailleurs et d'agences."],
   None),
  ("Le bon ordre d'appel en immeuble",
   [],
   ["Vérifier chez les voisins immédiats&nbsp;: c'est gratuit et cela tranche la "
    "question principale.",
    "Si plusieurs logements sont touchés&nbsp;: appeler le syndic ou son astreinte, qui "
    "mandate l'entreprise et fait passer la facture en charges communes.",
    "Si vous êtes seul concerné et locataire&nbsp;: prévenir le propriétaire ou "
    "l'agence, puis faire intervenir.",
    "Si le syndic est injoignable et que le dommage s'aggrave&nbsp;: faire intervenir à "
    "titre conservatoire, en conservant l'heure des appels, les photos et le rapport.",
    "Dans tous les cas&nbsp;: photographier avant nettoyage, et demander un rapport "
    "écrit si la cause paraît structurelle."],
   ),
 ],
 "faq": [
  ("Mon propriétaire refuse de payer, que faire&nbsp;?",
   "Appuyez-vous sur un document. Si notre inspection montre une canalisation "
   "affaissée, fissurée ou obstruée par un défaut de pente, le rapport écrit établit "
   "qu'il ne s'agit pas d'un problème d'usage. C'est la pièce qui fait avancer la "
   "discussion, à l'amiable comme ensuite."),
  ("Combien de temps pour intervenir sur Rennes&nbsp;?",
   "Sur l'agglomération rennaise, nous visons l'heure&nbsp;; sur les communes plus "
   "éloignées du département, deux à trois heures. Le délai est annoncé au téléphone "
   "avant tout déplacement."),
  ("Le bouchon est dans la colonne, dois-je quand même prévenir mes voisins&nbsp;?",
   "Oui, et c'est le geste le plus efficace des premières minutes&nbsp;: tant que les "
   "étages du dessus continuent d'utiliser l'eau, tout redescend vers le point bas. Une "
   "note dans la cage d'escalier fait souvent plus qu'un coup de furet."),
  ("Intervenez-vous sur mandat de syndic&nbsp;?",
   "Oui, en urgence comme en entretien programmé, avec rapport d'intervention et, si "
   "une inspection caméra a été faite, l'état du réseau par écrit — les deux pièces que "
   "réclament les conseils syndicaux."),
 ],
},

{
 "slug": "odeur-egout-appartement-ille-et-vilaine",
 "court": "Odeur d'égout en appartement (35)",
 "dept": "35", "act": "degorgement", "date": "2026-09-30",
 "titre": "Odeur d'égout en appartement (35) : la ventilation — ETS-BZH",
 "h1": "Odeur d'égout dans un appartement&nbsp;: quand c'est la ventilation de la colonne",
 "meta": ("Odeur d'égout dans un appartement à Rennes : siphons désamorcés, ventilation "
          "de colonne, clapet aérateur. Le diagnostic et qui intervient. 02 20 06 00 75."),
 "mots_cles": ("odeur d'égout appartement, siphon désamorcé, ventilation colonne "
               "immeuble, clapet aérateur, mauvaise odeur salle de bain Rennes"),
 "chapo": ("En appartement, une odeur d'égout se règle presque toujours en deux temps&nbsp;: "
           "un geste immédiat qui la fait disparaître, et une question de fond sur la "
           "raison pour laquelle elle est revenue. La première est à votre portée&nbsp;; "
           "la seconde relève souvent de la copropriété, et il vaut mieux le savoir avant "
           "de faire venir quelqu'un."),
 "urgent": [
   "Aérez et versez un verre d'eau dans chaque bonde, y compris celles qui ne "
   "servent jamais&nbsp;: lavabo d'une chambre, siphon de sol, bac à douche peu utilisé.",
   "Faites tourner l'eau trente secondes dans chaque appareil.",
   "Notez le moment où l'odeur apparaît&nbsp;: après un usage, la nuit, quand il y a "
   "du vent, ou en permanence. C'est l'indice décisif.",
   "Vérifiez le raccordement du lave-linge et du lave-vaisselle&nbsp;: un tuyau "
   "enfoncé dans une évacuation sans siphon laisse passer l'air directement.",
 ],
 "danger": ("Si l'odeur ressemble à du gaz et non à de l'égout — une odeur piquante, "
            "soufrée, ajoutée volontairement au gaz de ville — ne cherchez pas&nbsp;: "
            "n'actionnez aucun interrupteur, n'allumez rien, sortez, et appelez le "
            "service d'urgence gaz depuis l'extérieur. C'est une situation entièrement "
            "différente, qui ne relève ni de la plomberie ni de l'assainissement."),
 "sections": [
  ("Le siphon, puis la question de la ventilation",
   ["Chaque appareil est protégé par un siphon, ce coude qui retient un peu d'eau et "
    "sépare la pièce de la canalisation. Si l'eau s'en va, l'air de la colonne entre "
    "librement dans le logement.",
    "Un verre d'eau règle le cas de l'évaporation — l'appareil ne servait plus. Mais si "
    "l'odeur revient au bout de quelques jours, le siphon se vide activement, et c'est "
    "presque toujours un problème d'<strong>équilibre de pression dans la colonne</strong>.",
    "Une colonne d'eaux usées a besoin d'entrées d'air. Quand un volume important "
    "descend depuis les étages supérieurs, il crée une dépression derrière lui, et cette "
    "dépression aspire l'eau des siphons qu'elle croise. C'est ce qu'on appelle le "
    "désamorçage par siphonnage, et il touche en priorité les logements situés sous les "
    "gros consommateurs.",
    "Les symptômes sont caractéristiques et faciles à reconnaître&nbsp;: des glouglous "
    "dans vos siphons quand un voisin tire la chasse, et une odeur qui revient toujours "
    "après un pic d'usage — le matin, le soir."],
   None),
  ("Pourquoi cela concerne le syndic",
   ["La ventilation de la colonne n'est pas dans votre appartement&nbsp;: elle est en "
    "toiture, ou assurée par un clapet aérateur placé en partie haute de la colonne. "
    "Dans les deux cas, c'est une partie commune.",
    "Les deux défauts que nous rencontrons le plus souvent sur le parc rennais sont "
    "simples. Une <strong>sortie de ventilation obstruée</strong> en toiture — nid, "
    "feuilles, ou chapeau posé lors d'une réfection de couverture. Et un <strong>clapet "
    "aérateur en fin de vie</strong>, dont la membrane ne s'ouvre plus&nbsp;: il laisse "
    "alors la colonne en dépression, et parfois il laisse au contraire passer l'odeur "
    "dans le local où il se trouve.",
    "Si votre diagnostic pointe dans cette direction, prévenez le syndic avant de faire "
    "intervenir à vos frais&nbsp;: l'intervention relève des charges communes, et elle "
    "règle le problème pour tous les logements de la colonne, pas seulement le vôtre. "
    "Nous fournissons le rapport nécessaire à cette démarche."],
   None),
  ("Les causes qui restent de votre côté",
   [],
   ["Un siphon simplement évaporé, dans une pièce peu utilisée.",
    "Un joint de pied de cuvette desserré&nbsp;: l'odeur est alors très localisée au WC "
    "et permanente.",
    "Un tuyau de lave-linge ou de lave-vaisselle enfoncé dans une évacuation sans "
    "siphon ni dispositif anti-retour d'air.",
    "Une bonde de douche dont le joint ne fait plus l'étanchéité avec le receveur.",
    "Un siphon plat sous une douche à l'italienne, dont la garde d'eau est faible par "
    "conception et s'évapore vite.",
    "Un meuble qui obstrue une grille de ventilation de salle de bain&nbsp;: sans "
    "extraction, tout stagne."],
   ),
 ],
 "faq": [
  ("L'odeur revient après chaque chasse d'eau du voisin&nbsp;?",
   "C'est un cas d'école de désamorçage par siphonnage&nbsp;: la colonne manque "
   "d'entrée d'air. Le sujet est collectif et doit être porté au syndic. Un rapport "
   "d'intervention qui le documente facilite la décision en conseil syndical."),
  ("Puis-je poser un clapet anti-odeur sur ma bonde&nbsp;?",
   "Cela existe et cela peut soulager ponctuellement, mais c'est un pansement&nbsp;: la "
   "cause reste le manque de ventilation, et les autres appareils continueront de se "
   "désamorcer. À réserver aux siphons de sol rarement alimentés."),
  ("Mon logement est en location, à qui m'adresser&nbsp;?",
   "Prévenez le propriétaire ou l'agence, qui saisira le syndic si la colonne est en "
   "cause. Si l'origine est dans le logement — joint, siphon, raccordement d'appareil — "
   "l'intervention est plus simple et se règle directement."),
  ("Intervenez-vous pour un diagnostic d'odeur&nbsp;?",
   "Oui. Le test des siphons et le contrôle des évacuations prennent moins d'une heure. "
   "Si l'origine reste introuvable, l'inspection caméra localise une fissure ou un "
   "défaut, avec rapport écrit exploitable par le syndic."),
 ],
},

{
 "slug": "evacuation-lente-salle-de-bain-ille-et-vilaine",
 "court": "Évacuation lente (35)",
 "dept": "35", "act": "degorgement", "date": "2026-09-30",
 "titre": "Douche qui s'évacue mal (35) : agir avant le bouchon — ETS-BZH",
 "h1": "Douche ou baignoire qui s'évacue lentement&nbsp;: le signal qu'il ne faut pas laisser passer",
 "meta": ("Douche qui s'évacue lentement en Ille-et-Vilaine : pourquoi c'est un bouchon "
          "en formation, comment le traiter tôt, et ce qui ne marche pas. 02 20 06 00 75."),
 "mots_cles": ("douche qui s'évacue mal, eau stagnante douche, bonde bouchée cheveux, "
               "évacuation lente salle de bain, débouchage Ille-et-Vilaine"),
 "chapo": ("Une douche qui met une minute à se vider n'est pas encore bouchée&nbsp;: "
           "elle est en train de le devenir. C'est exactement le moment où "
           "l'intervention est la plus simple et la moins coûteuse — et c'est aussi le "
           "moment où presque personne n'appelle."),
 "urgent": [
   "Retirez la grille de bonde et sortez ce qui s'y trouve&nbsp;: dans une salle de "
   "bain, c'est là que se joue la moitié des cas.",
   "Si la bonde est accessible, dévissez-la et nettoyez le panier ou la cloche "
   "en-dessous.",
   "Faites couler à grand débit pendant une minute et observez&nbsp;: si le "
   "rétablissement n'est que partiel, le dépôt est plus loin.",
   "Notez si d'autres appareils ralentissent en même temps&nbsp;: cela déplace le "
   "diagnostic vers l'évacuation commune.",
 ],
 "danger": ("Sur un receveur en résine, un acrylique ou un émail ancien, n'utilisez "
            "aucun déboucheur caustique et ne versez pas d'eau bouillante&nbsp;: les "
            "premiers ternissent et fragilisent le matériau, la seconde peut le fissurer "
            "par choc thermique. Sur une douche à l'italienne avec siphon plat, les "
            "produits stagnent en plus dans un très faible volume, juste au-dessus du "
            "joint d'étanchéité."),
 "sections": [
  ("Cheveux et savon : le bouchon le plus prévisible du logement",
   ["Le mécanisme est toujours le même, et il est très régulier dans le temps. Les "
    "cheveux passent la grille, s'accrochent à la moindre aspérité juste après la bonde, "
    "et forment une trame. Le savon et les gels douche, riches en corps gras, viennent "
    "s'y déposer et transforment cette trame en masse compacte.",
    "Ce qui rend le phénomène particulier, c'est sa progressivité&nbsp;: l'écoulement se "
    "dégrade sur plusieurs mois, si lentement qu'on s'y habitue. On commence à faire "
    "des pauses pendant la douche pour laisser l'eau descendre, et un matin plus rien ne "
    "part.",
    "Sur les douches à l'italienne, très répandues dans les rénovations récentes du parc "
    "rennais, le siphon est plat et son accès est réduit. Le dépôt s'y installe plus "
    "vite, et l'accès à la main y est presque impossible&nbsp;: c'est le cas où l'on "
    "gagne vraiment à traiter tôt.",
    "Dans les logements étudiants et les colocations, très nombreux sur l'agglomération, "
    "l'usage est simplement plus intense&nbsp;: une même salle de bain sert trois ou "
    "quatre fois plus, et le bouchon se forme d'autant plus vite."],
   None),
  ("Les gestes qui marchent, dans l'ordre",
   ["<strong>La grille et la bonde d'abord.</strong> Les retirer et les nettoyer règle "
    "une grande part des situations, et cela ne demande aucun outil sur la plupart des "
    "modèles.",
    "<strong>Le siphon ensuite.</strong> Sur une baignoire ou une douche surélevée, il "
    "est souvent accessible par une trappe. Un seau dessous, on dévisse, on nettoie, on "
    "remonte.",
    "<strong>Le furet à tête souple</strong>, si l'écoulement reste dégradé. Il traverse "
    "le coude et racle la paroi sur quelques mètres sans abîmer la canalisation. Sur un "
    "siphon plat, mieux vaut un furet fin et souple qu'un outil rigide.",
    "<strong>L'hydrocurage</strong> quand le réseau est encrassé sur la longueur et que "
    "tout revient au bout de quelques semaines. Il rétablit le diamètre utile d'origine, "
    "ce que le furet ne fait pas.",
    "Une remarque sur les produits&nbsp;: les enzymatiques, versés régulièrement sur une "
    "évacuation qui fonctionne encore, ralentissent l'accumulation. Sur un bouchon "
    "installé, aucun produit ne fonctionne, et les caustiques créent surtout un risque "
    "pour l'intervention suivante."],
   None),
  ("Ce qui évite d'en arriver là",
   [],
   ["Une grille anti-cheveux posée sur la bonde&nbsp;: c'est dérisoire et c'est ce qui "
    "marche le mieux.",
    "Un nettoyage de la bonde une fois par mois, avant que cela ne ralentisse.",
    "Une eau chaude laissée couler une minute après la douche, pour entraîner les corps "
    "gras plutôt que de les laisser figer.",
    "En colocation ou en location, une consigne affichée&nbsp;: la moitié des appels "
    "viennent d'un usage que personne n'a expliqué.",
    "Un hydrocurage préventif quand le logement a plus de vingt ans et que les "
    "évacuations n'ont jamais été nettoyées.",
    "Ne jamais vider un fond de peinture, de plâtre ou d'enduit dans une douche pendant "
    "des travaux&nbsp;: c'est le bouchon le plus dur à retirer."],
   ),
 ],
 "faq": [
  ("Le bicarbonate et le vinaigre, ça marche&nbsp;?",
   "Sur un ralentissement léger et récent, cela peut aider marginalement. Sur un bouchon "
   "de cheveux et de savon constitué, non&nbsp;: la réaction se produit en surface et ne "
   "dissout pas la trame. L'avantage est qu'au moins, cela n'abîme rien."),
  ("Ma douche à l'italienne se rebouche tous les trois mois&nbsp;?",
   "Le siphon plat et la faible pente sont en cause. Un nettoyage régulier de la bonde "
   "aide, mais si la récidive est aussi rapide, il faut vérifier la pente et l'état de "
   "l'évacuation&nbsp;: une contre-pente sur quelques centimètres suffit à tout retenir."),
  ("Puis-je utiliser un furet acheté en magasin de bricolage&nbsp;?",
   "Oui sur une évacuation classique, avec prudence&nbsp;: tête souple, sans forcer, et "
   "en tournant plutôt qu'en poussant. Sur un receveur fragile ou un siphon plat, le "
   "risque de rayer ou de déboîter est réel."),
  ("Intervenez-vous rapidement sur Rennes pour ce type de problème&nbsp;?",
   "Oui, et c'est typiquement l'intervention qu'il vaut mieux programmer tôt plutôt que "
   "d'attendre l'urgence. Devis gratuit, tarif validé avant démarrage."),
 ],
},

{
 "slug": "lave-linge-qui-inonde-ille-et-vilaine",
 "court": "Lave-linge qui inonde (35)",
 "dept": "35", "act": "plomberie", "date": "2026-09-30",
 "titre": "Lave-linge qui inonde (35) : couper et comprendre — ETS-BZH",
 "h1": "Lave-linge ou lave-vaisselle qui inonde&nbsp;: couper d'abord, comprendre ensuite",
 "meta": "Lave-linge ou lave-vaisselle qui inonde en Ille-et-Vilaine : couper, distinguer l'appareil du raccordement, protéger le voisin. 02 20 06 00 75.",
 "mots_cles": ("lave-linge qui inonde, lave-vaisselle fuite, vidange qui refoule, "
               "aquastop, dégât des eaux électroménager Rennes"),
 "chapo": ("Une flaque devant le lave-linge peut venir de l'appareil, de son "
           "raccordement, ou de l'évacuation dans laquelle il rejette. Ce sont trois "
           "problèmes différents, avec trois interlocuteurs différents — et en "
           "appartement, il y a une quatrième urgence&nbsp;: le voisin du dessous."),
 "urgent": [
   "Coupez le robinet d'arrivée d'eau de l'appareil, derrière ou sous l'évier. S'il "
   "ne ferme plus, coupez l'arrivée générale.",
   "Coupez l'alimentation électrique de l'appareil au tableau, pas seulement son "
   "bouton&nbsp;: il y a de l'eau au sol et une prise à proximité.",
   "Épongez immédiatement et surélevez ce qui est au sol&nbsp;: en appartement, "
   "chaque minute compte pour l'étage du dessous.",
   "Prévenez le voisin du dessous avant qu'il ne découvre la tache&nbsp;: cela change "
   "tout à la suite.",
   "Photographiez avant de nettoyer.",
 ],
 "danger": ("Ne touchez pas un appareil électroménager posé dans l'eau sans avoir "
            "coupé son circuit au tableau. Le fait qu'il soit « éteint » ne suffit "
            "pas&nbsp;: il reste sous tension tant que la prise est alimentée. Et ne "
            "passez pas la serpillière autour d'un bloc multiprise resté au sol&nbsp;: "
            "c'est l'association la plus fréquente derrière les accidents domestiques "
            "en buanderie."),
 "sections": [
  ("Trois origines, trois responsables",
   ["<strong>L'appareil lui-même.</strong> Joint de hublot fatigué, pompe de vidange "
    "fissurée, cuve percée, électrovanne bloquée en position ouverte. C'est le fabricant "
    "ou un réparateur électroménager qui intervient, pas un plombier. Un indice&nbsp;: "
    "l'eau apparaît sous l'appareil, au centre, et pas au niveau des raccords.",
    "<strong>Le raccordement.</strong> Le flexible d'arrivée qui a percé — c'est une "
    "pièce d'usure, et sa tresse se fatigue après quelques années —, l'écrou desserré, "
    "ou le tuyau de vidange mal fixé qui ressort de son évacuation pendant l'essorage. "
    "Là, c'est de la plomberie, et c'est rapide.",
    "<strong>L'évacuation.</strong> L'appareil rejette normalement, mais la canalisation "
    "n'absorbe pas le débit&nbsp;: l'eau remonte et déborde. Si c'est le cas, vous le "
    "verrez à un détail — ça ne déborde que pendant la vidange, jamais au repos, et "
    "souvent l'évier voisin gargouille en même temps.",
    "Ce dernier cas est le plus courant dans le parc rennais ancien, où les machines "
    "ont été raccordées après coup sur des évacuations d'évier au diamètre modeste."],
   None),
  ("En appartement, le vrai enjeu est en dessous",
   ["Un lave-linge qui déborde de vingt litres dans une maison fait une flaque. Au "
    "troisième étage d'un immeuble rennais, les mêmes vingt litres traversent un "
    "plancher, ressortent au plafond du dessous et abîment un logement qui n'y est pour "
    "rien.",
    "La séquence qui protège tout le monde est simple&nbsp;: couper, éponger, prévenir. "
    "Prévenir en premier, même avant d'avoir tout compris. Un voisin averti protège ses "
    "biens, et la discussion qui suivra sera d'une tout autre nature que s'il découvre "
    "la tache trois jours plus tard.",
    "Remplissez ensuite un constat amiable dégât des eaux avec lui, même si les dégâts "
    "paraissent minimes&nbsp;: une auréole au plafond met plusieurs jours à révéler son "
    "ampleur, et un document signé le jour même vaut mieux qu'une reconstitution après "
    "coup. Déclarez à votre assureur dans le délai prévu par votre contrat.",
    "Enfin, ne réparez pas et ne repeignez rien chez le voisin avant le passage de "
    "l'expert&nbsp;: les dégâts doivent rester constatables."],
   None),
  ("Ce qui évite la récidive",
   [],
   ["Remplacer les flexibles d'arrivée tous les cinq ans environ&nbsp;: ce sont des "
    "consommables, et ils coûtent une fraction du sinistre qu'ils provoquent.",
    "Poser un flexible à sécurité intégrée, qui coupe automatiquement en cas de rupture.",
    "Fermer le robinet d'arrivée quand on s'absente plusieurs jours&nbsp;— et "
    "systématiquement dans un logement laissé vide plusieurs semaines.",
    "Fixer correctement la crosse de vidange dans son évacuation, à la bonne hauteur, "
    "pour qu'elle ne ressorte pas à l'essorage.",
    "Ne pas faire tourner la machine en partant de chez soi ou la nuit, en appartement.",
    "Poser un bac de rétention sous l'appareil quand la buanderie est au-dessus d'une "
    "pièce sensible."],
   ),
 ],
 "faq": [
  ("Ça ne déborde que pendant la vidange, d'où ça vient&nbsp;?",
   "De l'évacuation, qui n'absorbe pas le débit de la pompe. Soit elle est partiellement "
   "bouchée, soit son diamètre est insuffisant, soit la crosse est mal positionnée. "
   "C'est le cas le plus fréquent et il se règle en une intervention."),
  ("Mon assurance couvre-t-elle un dégât des eaux venant de l'électroménager&nbsp;?",
   "Généralement oui au titre du dégât des eaux, mais les modalités varient et la "
   "vétusté du flexible peut être discutée. Photographiez, conservez la pièce "
   "défectueuse, et déclarez rapidement."),
  ("Dois-je appeler un plombier ou un réparateur électroménager&nbsp;?",
   "Si l'eau vient des raccords ou de l'évacuation, c'est un plombier. Si elle sort du "
   "ventre de l'appareil, c'est un réparateur électroménager. Décrivez-nous la situation "
   "au téléphone&nbsp;: nous vous le dirons plutôt que de nous déplacer pour rien."),
  ("Intervenez-vous en urgence sur Rennes&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur toute l'Ille-et-Vilaine. En appartement, la priorité est "
   "d'arrêter l'écoulement et de limiter l'atteinte aux logements voisins."),
 ],
},

{
 "slug": "fuite-encastree-dans-une-dalle-ille-et-vilaine",
 "court": "Fuite encastrée (35)",
 "dept": "35", "act": "plomberie", "date": "2026-09-30",
 "titre": "Fuite encastrée dans une dalle (35) : la localiser — ETS-BZH",
 "h1": "Fuite encastrée dans une dalle ou une cloison&nbsp;: la trouver sans tout casser",
 "meta": ("Fuite encastrée dans une dalle ou une cloison en Ille-et-Vilaine : caméra "
          "thermique, gaz traceur, mise en pression. Localiser avant d'ouvrir. "
          "02 20 06 00 75."),
 "mots_cles": ("fuite encastrée, recherche de fuite non destructive, caméra thermique "
               "fuite, gaz traceur, fuite sous dalle Rennes"),
 "chapo": ("Une tache qui s'élargit au sol, une plinthe qui gondole, un mur humide sans "
           "raison apparente&nbsp;: la fuite est dans la dalle ou dans la cloison, "
           "invisible. La tentation est d'ouvrir là où c'est mouillé. C'est presque "
           "toujours le mauvais endroit, et c'est la partie la plus coûteuse du chantier."),
 "urgent": [
   "Coupez l'arrivée d'eau générale et vérifiez si la tache cesse de progresser&nbsp;: "
   "cela distingue déjà une fuite sous pression d'une infiltration extérieure.",
   "Fermez le circuit de chauffage si la tache est près d'un radiateur, et surveillez "
   "la pression de la chaudière.",
   "Relevez le compteur d'eau, attendez une heure sans consommer, relevez à "
   "nouveau&nbsp;: un index qui bouge confirme une fuite sous pression.",
   "Photographiez l'évolution de la tache en datant&nbsp;: c'est utile au diagnostic et "
   "à l'assurance.",
   "N'ouvrez rien avant la localisation.",
 ],
 "danger": ("Ne percez pas une dalle ou une cloison pour « voir »&nbsp;: vous risquez de "
            "toucher une autre canalisation, un câble électrique encastré ou un plancher "
            "chauffant, et de transformer une fuite en sinistre. En immeuble, s'y ajoute "
            "le risque de percer une canalisation qui ne dessert pas votre logement."),
 "sections": [
  ("Pourquoi la tache n'est pas au-dessus de la fuite",
   ["L'eau qui s'échappe d'une canalisation encastrée ne monte pas tout droit&nbsp;: "
    "elle suit les chemins de moindre résistance. Dans une dalle, elle circule dans la "
    "couche de ravoirage ou le lit de sable, longe les gaines et ressort là où le "
    "revêtement est le plus perméable — souvent à plusieurs mètres.",
    "Dans une cloison, elle descend le long du montant et sort au niveau de la plinthe, "
    "parfois de l'autre côté du mur. Sur un plancher intermédiaire d'immeuble, elle "
    "traverse la dalle et apparaît au plafond du logement du dessous, décalée d'une "
    "pièce entière.",
    "C'est pour cette raison que l'ouverture au jugé est rarement rentable&nbsp;: on "
    "ouvre, on ne trouve pas, on referme, et on recommence ailleurs. La remise en état de "
    "ces ouvertures inutiles dépasse très vite le coût d'une recherche."],
   None),
  ("Les trois méthodes, et ce qu'elles voient",
   ["<strong>La caméra thermique</strong> visualise les écarts de température en "
    "surface. Elle est très efficace sur une fuite d'eau chaude ou sur un circuit de "
    "chauffage, et sur les dalles avec plancher chauffant&nbsp;: le tracé apparaît, et "
    "l'anomalie avec lui. Elle voit moins bien une fuite d'eau froide dans un mur épais.",
    "<strong>Le gaz traceur</strong> consiste à vider la canalisation et à la mettre "
    "sous pression avec un mélange inoffensif, plus léger que l'air. Il s'échappe par le "
    "point de fuite et remonte à travers le revêtement, où un détecteur le repère. C'est "
    "la méthode la plus précise sur les fuites froides et les canalisations enterrées.",
    "<strong>La mise en pression avec mesure</strong> isole les circuits un par un pour "
    "déterminer lequel perd&nbsp;: eau froide, eau chaude, chauffage. Cela ne donne pas "
    "le point exact mais réduit considérablement la zone, et c'est toujours la première "
    "étape.",
    "En pratique, on combine&nbsp;: on isole le circuit fautif, puis on localise. "
    "L'objectif est d'ouvrir un carré de quarante centimètres, pas une pièce."],
   None),
  ("Le parc rennais : deux configurations récurrentes",
   [],
   ["Les immeubles des années soixante et soixante-dix, avec canalisations noyées dans "
    "la dalle sans gaine&nbsp;: à la moindre corrosion, la reprise demande de casser, "
    "d'où l'importance de localiser précisément.",
    "Les salles de bain superposées sur toute la hauteur du bâtiment&nbsp;: une fuite au "
    "quatrième peut se manifester au deuxième.",
    "Les rénovations récentes avec plancher chauffant, où toute ouverture au hasard "
    "risque de percer un circuit.",
    "Les cloisons en plaque sur ossature, où l'eau descend le long des montants et "
    "ressort loin du point d'origine.",
    "Le bâti ancien du centre et de Saint-Malo, où l'humidité de remontée capillaire "
    "imite parfaitement une fuite&nbsp;— et où la recherche sert aussi à prouver qu'il "
    "n'y en a pas."],
   ),
 ],
 "faq": [
  ("La recherche de fuite est-elle prise en charge par l'assurance&nbsp;?",
   "Souvent oui dans le cadre d'un dégât des eaux, selon les garanties du contrat. "
   "Appelez votre assureur avant d'engager l'intervention pour vérifier la couverture "
   "et la procédure&nbsp;: cela évite une avance inutile. Nous fournissons un rapport "
   "exploitable par l'expert."),
  ("Combien de temps dure une recherche&nbsp;?",
   "Comptez en général deux à quatre heures selon la configuration et la méthode "
   "employée. La réparation se programme ensuite, une fois le point exact connu et "
   "l'ouverture réduite au minimum."),
  ("Faut-il forcément casser pour réparer&nbsp;?",
   "Pas toujours. Selon la position et la longueur concernée, il est parfois plus "
   "économique d'abandonner la portion défectueuse et de créer un nouveau tracé en "
   "apparent ou en contournement. Nous vous présentons les deux options chiffrées."),
  ("Et si la fuite vient de l'appartement du dessus&nbsp;?",
   "La recherche sert précisément à l'établir. Le rapport indique l'origine réelle, ce "
   "qui permet aux assureurs de se positionner sans que l'occupant du dessous attende "
   "des mois. C'est souvent ce document qui débloque la situation."),
 ],
},

{
 "slug": "fuite-chez-le-voisin-du-dessous-ille-et-vilaine",
 "court": "Fuite vers le voisin du dessous (35)",
 "dept": "35", "act": "plomberie", "date": "2026-09-30",
 "titre": "Ma fuite coule chez le voisin (35) : que faire — ETS-BZH",
 "h1": "C'est chez vous que ça fuit et ça coule chez le voisin&nbsp;: la bonne conduite",
 "meta": "Votre fuite atteint le logement du dessous en Ille-et-Vilaine : couper, prévenir, constater, déclarer. L'ordre qui évite les litiges. 02 20 06 00 75.",
 "mots_cles": ("fuite chez le voisin du dessous, constat amiable dégât des eaux, "
               "responsabilité fuite appartement, assurance dégât des eaux Rennes"),
 "chapo": ("Il y a une abondante littérature sur ce qu'il faut faire quand l'eau vient "
           "du voisin du dessus. Beaucoup moins sur la situation inverse, qui est "
           "pourtant tout aussi fréquente et bien plus inconfortable&nbsp;: c'est chez "
           "vous que ça fuit, et le dommage est chez quelqu'un d'autre."),
 "urgent": [
   "Coupez l'arrivée d'eau de votre logement&nbsp;: la vanne générale, pas seulement "
   "le robinet suspect.",
   "Descendez prévenir le voisin immédiatement, avant qu'il ne découvre la tache. "
   "C'est le geste qui détermine le ton de tout ce qui suivra.",
   "S'il est absent, prévenez le gardien ou le syndic&nbsp;: eux seuls peuvent faire "
   "ouvrir un logement en cas d'urgence.",
   "Photographiez chez vous&nbsp;: origine de la fuite, heure, ce que vous avez coupé.",
   "Faites intervenir pour arrêter la fuite. Tant qu'elle n'est pas arrêtée, tout "
   "le reste est prématuré.",
 ],
 "danger": ("Si l'eau a traversé le plancher, elle a probablement atteint le point "
            "lumineux du plafond du dessous. Dites-le explicitement à votre voisin et "
            "conseillez-lui de couper le circuit d'éclairage de la pièce concernée avant "
            "d'allumer. Un plafond qui goutte sur un luminaire est une situation "
            "dangereuse, et c'est vous qui avez l'information."),
 "sections": [
  ("Pourquoi prévenir immédiatement change tout",
   ["Sur le plan pratique d'abord&nbsp;: un voisin averti protège ses meubles, déplace "
    "son électroménager, coupe son éclairage. Les dégâts s'arrêtent de croître.",
    "Sur le plan de la relation ensuite. Un dégât des eaux entre voisins se règle "
    "presque toujours sans difficulté quand il a été annoncé, et presque toujours mal "
    "quand il a été découvert. La différence ne tient pas au montant, elle tient au fait "
    "d'avoir été prévenu ou non.",
    "Sur le plan de l'assurance enfin. Vous n'êtes pas en train de reconnaître une "
    "faute&nbsp;: une canalisation qui cède n'est pas une faute, c'est un sinistre, et "
    "c'est exactement ce que vos contrats couvrent. Ce sont les assureurs qui règlent "
    "entre eux. Votre rôle est de faire cesser le dommage, de le documenter, et de "
    "déclarer.",
    "Sur l'agglomération rennaise, où une grande part des logements est en copropriété "
    "et où beaucoup de propriétaires ne résident pas sur place, cette étape est aussi "
    "celle qui prend le plus de temps&nbsp;: il faut souvent passer par le syndic ou "
    "l'agence pour joindre l'occupant réel. Commencez tout de suite."],
   None),
  ("Le constat amiable, et pourquoi le remplir le jour même",
   ["Le constat amiable dégât des eaux est un document contradictoire, rempli et signé "
    "par les deux parties, qui décrit l'origine, la date, les circonstances et les "
    "dommages constatés. Chacun l'envoie ensuite à son assureur.",
    "Le remplir le jour même a un avantage décisif&nbsp;: les faits sont frais, les deux "
    "parties sont d'accord sur ce qu'elles voient, et personne n'a encore eu le temps de "
    "reconstruire une version. Une semaine plus tard, les souvenirs divergent et les "
    "dégâts se sont étendus.",
    "Quelques points à soigner&nbsp;: décrire l'origine précisément — « rupture du "
    "flexible d'alimentation du lave-linge », pas « fuite d'eau » —, lister les biens "
    "touchés chez le voisin, joindre des photos des deux côtés, et mentionner l'heure de "
    "la découverte et celle de l'arrêt de la fuite. Si votre voisin refuse de signer, "
    "déclarez seul en indiquant le refus&nbsp;: cela ne bloque pas votre dossier."],
   None),
  ("Ce qui relève de vous, et ce qui n'en relève pas",
   [],
   ["<strong>De vous</strong>&nbsp;: les canalisations privatives de votre logement, vos "
    "appareils, vos raccordements, et l'entretien courant.",
    "<strong>De la copropriété</strong>&nbsp;: les colonnes verticales, les canalisations "
    "encastrées desservant plusieurs logements, et les parties communes. Une fuite sur "
    "une colonne qui traverse votre appartement n'est pas la vôtre.",
    "<strong>De votre propriétaire</strong>, si vous êtes locataire&nbsp;: la vétusté et "
    "les défauts de l'ouvrage, par opposition à l'entretien courant.",
    "<strong>Des assureurs</strong>&nbsp;: la répartition finale. Ce n'est pas à vous de "
    "la négocier avec votre voisin.",
    "Dans tous les cas, un rapport d'intervention qui identifie précisément l'origine "
    "vaut mieux qu'une discussion&nbsp;: il désigne la bonne responsabilité, et parfois "
    "elle n'est pas celle qu'on croyait."],
   ),
 ],
 "faq": [
  ("Dois-je payer les réparations chez mon voisin&nbsp;?",
   "Ce sont les assurances qui règlent, dans le cadre prévu pour les dégâts des eaux en "
   "immeuble. Ne vous engagez pas personnellement à rembourser avant que les assureurs "
   "aient instruit&nbsp;: déclarez, documentez, et laissez la procédure suivre son cours."),
  ("Mon voisin exige une réparation immédiate de son plafond&nbsp;?",
   "La remise en état vient après le passage de l'expert et après assèchement complet. "
   "Repeindre un plafond encore humide fait cloquer la peinture et complique "
   "l'indemnisation. Expliquez-le, c'est dans son intérêt aussi."),
  ("Je suis locataire, qui déclare&nbsp;?",
   "Vous déclarez à votre assurance habitation, et vous informez le propriétaire ou "
   "l'agence. Si la fuite vient d'un élément relevant du bailleur — vétusté d'une "
   "canalisation, par exemple — c'est son assurance qui prendra le relais."),
  ("Intervenez-vous en urgence pour arrêter la fuite&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur l'Ille-et-Vilaine. La première priorité est d'arrêter "
   "l'écoulement&nbsp;; la recherche fine et la réparation définitive se programment "
   "ensuite. Le rapport d'intervention vous est remis pour votre dossier."),
 ],
},

{
 "slug": "disjoncteur-puissance-insuffisante-ille-et-vilaine",
 "court": "Puissance insuffisante (35)",
 "dept": "35", "act": "electricite", "date": "2026-09-30",
 "titre": "Le compteur disjoncte souvent (35) : puissance — ETS-BZH",
 "h1": "Le compteur disjoncte dès qu'on cumule&nbsp;: puissance souscrite ou installation&nbsp;?",
 "meta": ("Disjoncteur de branchement qui saute dans un studio ou un appartement à "
          "Rennes : puissance souscrite, circuits ou défaut ? Le diagnostic. "
          "02 20 06 00 75."),
 "mots_cles": ("disjoncteur de branchement saute, puissance souscrite insuffisante, "
               "compteur qui disjoncte, studio Rennes électricité, augmenter la puissance"),
 "chapo": ("Le four et la bouilloire en même temps, et tout s'éteint. On accuse "
           "l'installation, on parle d'augmenter la puissance, et parfois c'est la bonne "
           "réponse — parfois non. Dans un petit logement, la question mérite d'être "
           "posée correctement avant de payer un abonnement plus cher pour rien."),
 "urgent": [
   "Identifiez ce qui a sauté&nbsp;: le gros disjoncteur près du compteur, ou un "
   "petit dans le tableau. Ce n'est pas le même problème.",
   "Si c'est le gros et qu'il se réarme sans difficulté après avoir éteint un "
   "appareil, il s'agit d'un dépassement de puissance, pas d'un défaut.",
   "Notez la combinaison exacte qui déclenche&nbsp;: quels appareils, dans quel "
   "ordre. C'est ce qui permet de calculer.",
   "Relevez la puissance souscrite&nbsp;: elle figure sur votre facture et sur "
   "l'écran du compteur.",
 ],
 "danger": ("Ne remplacez jamais un disjoncteur par un calibre supérieur pour « qu'il "
            "saute moins ». Le calibre est choisi en fonction de la section des câbles "
            "qu'il protège&nbsp;: un calibre plus élevé laisse passer un courant que le "
            "câble ne peut pas dissiper, et le point chaud se forme dans la cloison, là "
            "où personne ne le verra."),
 "sections": [
  ("Dépassement de puissance ou défaut : la différence",
   ["<strong>Un dépassement de puissance</strong> se reconnaît à sa régularité&nbsp;: il "
    "survient toujours quand plusieurs appareils gourmands fonctionnent ensemble, et le "
    "disjoncteur se réarme sans problème dès qu'on en éteint un. Rien n'est cassé&nbsp;: "
    "vous demandez simplement plus que ce que vous avez souscrit.",
    "<strong>Un défaut</strong> se reconnaît à son caractère aléatoire ou obstiné&nbsp;: "
    "le disjoncteur saute sans logique apparente, ou refuse de se réarmer. Là, il y a "
    "quelque chose à chercher, et augmenter la puissance ne changerait rien.",
    "Le calcul est plus simple qu'il n'y paraît. Une plaque de cuisson, un four, un "
    "sèche-linge, un chauffe-eau en chauffe, un radiateur électrique ou un chauffage "
    "d'appoint&nbsp;: chacun consomme beaucoup. Deux ou trois ensemble suffisent à "
    "dépasser une puissance souscrite modeste, très courante dans les studios et les "
    "petits appartements.",
    "Sur Rennes, le cas revient constamment dans le parc étudiant et les petites "
    "surfaces&nbsp;: des logements souscrits au minimum, équipés ensuite d'un "
    "sèche-linge, d'un chauffage d'appoint et d'une plaque. L'installation est saine, "
    "l'abonnement ne l'est plus."],
   None),
  ("Augmenter la puissance : oui, mais après vérification",
   ["Augmenter la puissance souscrite se demande à votre fournisseur d'électricité, et "
    "cela se fait à distance sur les compteurs communicants. C'est rapide, et cela "
    "augmente l'abonnement.",
    "Mais avant de le faire, il faut s'assurer que l'installation supporte cette "
    "puissance. Augmenter le seuil de déclenchement sans vérifier, c'est simplement "
    "reporter la contrainte sur les câbles et le tableau&nbsp;: ce qui protégeait ne "
    "protège plus au bon niveau.",
    "Les points que nous contrôlons sont toujours les mêmes&nbsp;: la section des "
    "conducteurs en tête d'installation, l'état et le calibre des protections, la "
    "présence de circuits dédiés pour les appareils de forte puissance, et l'état des "
    "connexions au tableau — un serrage qui a pris du jeu chauffe d'autant plus qu'on "
    "augmente le courant.",
    "Dans beaucoup de cas, la meilleure réponse n'est d'ailleurs pas d'augmenter la "
    "puissance mais de <strong>répartir</strong>&nbsp;: créer un circuit dédié pour la "
    "plaque ou le sèche-linge règle le problème sans toucher à l'abonnement."],
   None),
  ("Ce qui se vérifie dans un petit logement",
   [],
   ["La puissance souscrite comparée à l'équipement réellement présent.",
    "La présence de circuits dédiés pour plaque, four, lave-linge et chauffe-eau.",
    "Le nombre de prises par circuit&nbsp;: une multiplication de multiprises signale "
    "presque toujours un circuit sous-équipé.",
    "La protection différentielle 30&nbsp;mA, souvent absente dans les petites surfaces "
    "issues de divisions d'immeubles anciens.",
    "L'état de la prise de terre, régulièrement inexistante dans ces mêmes logements.",
    "Les chauffages d'appoint utilisés en permanence&nbsp;: ils sont la première cause "
    "de dépassement et, sur une prise ancienne, la première cause d'échauffement."],
   ),
 ],
 "faq": [
  ("Vaut-il mieux augmenter la puissance ou refaire des circuits&nbsp;?",
   "Cela dépend de l'usage réel. Si vous cumulez souvent plusieurs gros appareils, "
   "l'augmentation est justifiée. Si le problème vient d'un seul appareil branché sur un "
   "circuit inadapté, un circuit dédié coûte une fois et ne se paie pas tous les mois "
   "sur l'abonnement."),
  ("Mon logement est une location, qui décide&nbsp;?",
   "L'abonnement est au nom de l'occupant, donc l'augmentation vous appartient. En "
   "revanche, les travaux sur l'installation relèvent du propriétaire. Un rapport "
   "écrit précisant ce qui manque facilite nettement la demande."),
  ("Le compteur communicant peut-il disjoncter pour une autre raison&nbsp;?",
   "Oui&nbsp;: un dépassement bref et répété, ou un défaut en aval. Si le réarmement se "
   "fait mal, ou si la coupure survient sans cumul d'appareils, ce n'est pas une "
   "question de puissance et il faut contrôler l'installation."),
  ("Intervenez-vous rapidement sur l'agglomération rennaise&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur toute l'Ille-et-Vilaine. Le diagnostic et le devis sont "
   "gratuits, et nous vous dirons franchement si le problème relève de l'abonnement "
   "plutôt que de travaux."),
 ],
},

{
 "slug": "prise-ou-circuit-hors-service-ille-et-vilaine",
 "court": "Prise hors service (35)",
 "dept": "35", "act": "electricite", "date": "2026-09-30",
 "titre": "Prises mortes dans une pièce (35) : d'où ça vient — ETS-BZH",
 "h1": "Plus de courant dans une seule pièce&nbsp;: retrouver le circuit coupé",
 "meta": ("Prises ou éclairage hors service dans une pièce en Ille-et-Vilaine : les "
          "vérifications, les causes réelles et les signes d'alerte. 02 20 06 00 75."),
 "mots_cles": ("prise ne fonctionne plus, plus de courant dans une pièce, circuit "
               "coupé, boîte de dérivation, électricien Rennes"),
 "chapo": ("Les prises d'une pièce ne donnent plus rien, le reste du logement "
           "fonctionne, et aucun disjoncteur n'a bougé. Ce n'est ni une panne de réseau "
           "ni un hasard&nbsp;: quelque chose a lâché sur ce circuit précis, et c'est "
           "souvent un simple contact. Encore faut-il savoir lesquels vérifier — et "
           "reconnaître les cas où il ne faut surtout pas chercher soi-même."),
 "urgent": [
   "Testez plusieurs prises de la pièce avec un appareil dont vous êtes sûr, une "
   "lampe par exemple.",
   "Regardez le tableau&nbsp;: un disjoncteur légèrement abaissé passe facilement "
   "inaperçu. Abaissez-le complètement avant de le remonter.",
   "Vérifiez si l'éclairage de la pièce fonctionne encore&nbsp;: éclairage et prises "
   "sont sur des circuits distincts, et cela oriente le diagnostic.",
   "Sentez et regardez autour des prises concernées&nbsp;: odeur, trace noire, "
   "plastique déformé. Si vous en trouvez, arrêtez tout et coupez le circuit.",
 ],
 "danger": ("Une prise qui ne fonctionne plus après avoir chauffé, noirci ou senti le "
            "brûlé n'est pas « en panne »&nbsp;: elle a subi un échauffement, et le "
            "conducteur derrière elle aussi. Ne la démontez pas, ne la rebranchez pas, "
            "coupez son circuit au tableau et faites-la remplacer. C'est exactement le "
            "scénario qui précède un départ de feu dans une cloison."),
 "sections": [
  ("Les causes, de la plus banale à la plus sérieuse",
   ["<strong>Un disjoncteur mal remonté.</strong> Cela paraît trivial, et c'est "
    "pourtant fréquent&nbsp;: un disjoncteur qui a déclenché reste parfois en position "
    "intermédiaire. Il faut l'abaisser à fond avant de le relever.",
    "<strong>Une borne desserrée dans une prise.</strong> Les prises d'un même circuit "
    "sont souvent raccordées en chaîne&nbsp;: le courant passe par l'une pour aller à la "
    "suivante. Si un conducteur se desserre dans une prise, tout ce qui vient après "
    "s'éteint. C'est la cause la plus courante, et la plus révélatrice&nbsp;: un contact "
    "desserré chauffe.",
    "<strong>Une boîte de dérivation défaillante.</strong> Dans les logements anciens, "
    "les raccordements se font dans des boîtes encastrées, parfois avec de vieux dominos "
    "qui se desserrent avec le temps.",
    "<strong>Un conducteur coupé.</strong> Un percement de cloison pour fixer une "
    "étagère, un tableau ou un meuble&nbsp;: nous en trouvons régulièrement, et cela "
    "explique une panne apparue « sans raison » juste après un emménagement.",
    "Dans le parc rennais issu de divisions d'immeubles anciens, une cinquième cause "
    "revient&nbsp;: des circuits qui traversent plusieurs logements ou passent par des "
    "parties communes, héritage de découpages successifs."],
   None),
  ("Pourquoi un contact desserré est plus grave qu'une panne",
   ["Une prise qui ne donne plus rien est un inconfort. Mais si la cause est un "
    "conducteur desserré, ce qui s'est passé avant l'extinction mérite attention&nbsp;: "
    "le contact a résisté, il a chauffé, et il a fini par se dégrader complètement.",
    "Ce mécanisme s'emballe tout seul&nbsp;: la résistance de contact produit de la "
    "chaleur, la chaleur dilate le métal, le serrage se relâche encore. Selon le point "
    "où il s'arrête, on obtient soit une prise morte — le cas favorable —, soit un point "
    "chaud durable dans une boîte encastrée.",
    "Et un disjoncteur ne protège pas contre cela&nbsp;: il coupe sur une surintensité "
    "ou un défaut d'isolement, pas sur un mauvais contact. C'est pourquoi une prise qui "
    "s'éteint sans que rien ne saute mérite d'être ouverte et contrôlée, pas seulement "
    "remplacée."],
   None),
  ("Quand il faut appeler plutôt que chercher",
   [],
   ["Odeur de brûlé, trace noire, plastique déformé autour d'une prise ou d'un "
    "interrupteur.",
    "Une prise devenue tiède ou lâche, dans laquelle les fiches tiennent mal.",
    "Un disjoncteur qui ne se réarme pas, ou qui saute à nouveau dès la remise.",
    "Plusieurs pièces touchées en même temps sans qu'aucune protection n'ait bougé.",
    "Un tableau sans protection différentielle 30&nbsp;mA&nbsp;: dans ce cas, aucun "
    "défaut d'isolement ne sera détecté, quel qu'il soit.",
    "Une panne apparue juste après des travaux de perçage&nbsp;: un conducteur blessé "
    "mais pas sectionné est une situation dangereuse."],
   ),
 ],
 "faq": [
  ("Puis-je changer une prise moi-même&nbsp;?",
   "Techniquement c'est simple, à condition de couper le circuit et de vérifier "
   "l'absence de tension. Mais si la prise a chauffé, le remplacement ne suffit pas&nbsp;: "
   "il faut contrôler le conducteur et la boîte derrière, et souvent reprendre la "
   "liaison. C'est là que l'intervention se justifie."),
  ("L'éclairage fonctionne mais pas les prises, est-ce normal&nbsp;?",
   "C'est cohérent&nbsp;: éclairage et prises sont sur des circuits distincts, protégés "
   "séparément. Cela indique que le défaut est sur le circuit prises de cette pièce, ce "
   "qui restreint utilement la recherche."),
  ("Combien de temps pour retrouver une coupure de circuit&nbsp;?",
   "En général moins d'une heure&nbsp;: le circuit se remonte de proche en proche depuis "
   "le tableau, prise par prise. Une recherche plus longue signale une liaison encastrée "
   "endommagée, et nous vous le disons avant de poursuivre."),
  ("Intervenez-vous le soir sur Rennes&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur l'Ille-et-Vilaine. Une pièce sans courant peut attendre le "
   "lendemain&nbsp;; une odeur de brûlé, non — dites-le nous au téléphone, cela change "
   "la priorité."),
 ],
},

# ------------------------------------------------------ 56 — MORBIHAN (suite)
{
 "slug": "wc-bouche-location-saisonniere-morbihan",
 "court": "WC bouché en location (56)",
 "dept": "56", "act": "degorgement", "date": "2026-09-30",
 "titre": "WC bouché en location saisonnière (56) : réagir — ETS-BZH",
 "h1": "WC bouché en location saisonnière&nbsp;: réagir vite entre deux séjours",
 "meta": ("WC bouché dans une location saisonnière du Morbihan : intervenir entre deux "
          "séjours, prévenir la récidive, et qui paie. Débouchage 7j/7 au 02 20 06 00 75."),
 "mots_cles": ("WC bouché location saisonnière, débouchage Vannes, canalisation "
               "location vacances Morbihan, propriétaire meublé tourisme plomberie"),
 "chapo": ("Un WC bouché dans une location de vacances n'est pas seulement un problème "
           "technique&nbsp;: c'est un séjour gâché, un commentaire en ligne, et parfois "
           "un remboursement. En pleine saison, entre deux arrivées, la question n'est "
           "pas « comment réparer » mais « comment réparer avant samedi 16 h »."),
 "urgent": [
   "Faites cesser tout usage du WC concerné et indiquez-le clairement aux occupants.",
   "Demandez-leur le test le plus utile&nbsp;: la douche et l'évier s'évacuent-ils "
   "normalement&nbsp;? Cela distingue un bouchon local d'un problème de réseau.",
   "Demandez une photo de la cuvette et du sol&nbsp;: à distance, c'est ce qui vous "
   "évitera un déplacement inutile.",
   "Interdisez explicitement le déboucheur chimique, même s'il y en a sous l'évier.",
   "Appelez&nbsp;: en saison, le créneau se réserve, il ne s'improvise pas.",
 ],
 "danger": ("Si la maison est sur assainissement non collectif, un WC bouché peut "
            "signaler une fosse pleine et non un bouchon. Dans ce cas, ne faites jamais "
            "ouvrir le tampon par les locataires et ne leur demandez pas de regarder à "
            "l'intérieur&nbsp;: les gaz de fermentation sont dangereux, et ce n'est ni "
            "leur rôle ni leur responsabilité."),
 "sections": [
  ("Le diagnostic à distance, en trois questions",
   ["Quand vous n'êtes pas sur place — et en location saisonnière c'est souvent le cas "
    "—, trois questions posées aux occupants suffisent à orienter l'intervention.",
    "<strong>Les autres appareils fonctionnent-ils&nbsp;?</strong> Si la douche et "
    "l'évier s'évacuent bien, le bouchon est dans le WC ou juste après. Si tout est "
    "lent, il est sur l'évacuation commune, voire sur la fosse.",
    "<strong>Y a-t-il un gargouillis ailleurs quand on tire la chasse&nbsp;?</strong> "
    "Un oui déplace le problème vers l'aval&nbsp;: inutile de s'acharner sur la cuvette.",
    "<strong>Le niveau descend-il lentement ou pas du tout&nbsp;?</strong> Lentement, le "
    "passage est réduit&nbsp;; pas du tout, le bouchon est compact et proche.",
    "Ces trois réponses, transmises au téléphone, nous permettent d'arriver avec le bon "
    "matériel du premier coup. En pleine saison, cela fait la différence entre une "
    "intervention le jour même et un second passage."],
   None),
  ("Pourquoi cela arrive surtout en juillet et août",
   ["Une maison de location n'est pas soumise au même régime qu'une résidence "
    "principale, et le réseau le ressent.",
    "D'abord le <strong>volume</strong>&nbsp;: une installation dimensionnée et rodée "
    "pour deux personnes reçoit six occupants pendant trois semaines. Les mêmes "
    "canalisations, quatre fois plus de sollicitation.",
    "Ensuite les <strong>usages inconnus</strong>&nbsp;: les occupants changent chaque "
    "semaine et ne connaissent ni les habitudes de la maison, ni la présence d'une fosse "
    "septique. Les lingettes, les protections hygiéniques et le papier essuie-tout "
    "finissent dans la cuvette, sans mauvaise intention.",
    "Enfin l'<strong>alternance</strong>&nbsp;: pendant les mois creux, le réseau sèche, "
    "les dépôts durcissent et les siphons s'évaporent. La remise en service de mai "
    "réveille tout d'un coup. Sur le littoral morbihannais, du golfe à Quiberon en "
    "passant par la presqu'île de Rhuys, c'est un cycle que nous voyons chaque année.",
    "S'y ajoute une contrainte de réseau&nbsp;: dans les communes très touristiques, les "
    "collecteurs publics travaillent à leur limite en août, et un refoulement peut n'avoir "
    "aucun rapport avec votre installation."],
   None),
  ("Ce qui réduit vraiment le risque, côté propriétaire",
   [],
   ["Une consigne affichée dans les WC, en français et en anglais&nbsp;: rien d'autre "
    "que du papier hygiénique. C'est la mesure la plus efficace, et elle coûte une "
    "feuille imprimée.",
    "Une poubelle fermée dans chaque salle de bain&nbsp;: sans elle, tout part dans la "
    "cuvette.",
    "Un hydrocurage préventif avant la saison plutôt qu'un débouchage d'urgence pendant.",
    "Une vidange de fosse programmée hors saison, avec bordereau conservé.",
    "Un contact d'urgence communiqué aux occupants, avec la consigne de vous appeler au "
    "premier signe de ralentissement — pas quand tout est bouché.",
    "Une inspection caméra une fois, si la maison est ancienne&nbsp;: savoir dans quel "
    "état est le réseau évite de découvrir un affaissement un 14 août."],
   ),
 ],
 "faq": [
  ("Qui paie, le locataire de vacances ou le propriétaire&nbsp;?",
   "Dans un meublé de tourisme, l'entretien et le bon fonctionnement des équipements "
   "incombent au propriétaire, sauf dégradation manifestement imputable aux occupants — "
   "un objet dans la cuvette, par exemple. En pratique, le rapport d'intervention, qui "
   "décrit ce qui a été retiré, tranche la question mieux qu'un débat."),
  ("Intervenez-vous en urgence en pleine saison&nbsp;?",
   "Oui, 7j/7 sur l'ensemble du Morbihan, y compris en août. Nous annonçons un délai "
   "réaliste dès l'appel plutôt qu'un horaire que nous ne tiendrions pas&nbsp;: c'est ce "
   "qui vous permet d'organiser l'arrivée des occupants suivants."),
  ("Peut-on intervenir en l'absence du propriétaire&nbsp;?",
   "Oui, avec un accès et un accord. Beaucoup de nos interventions estivales sont "
   "déclenchées par un gestionnaire, une conciergerie ou un voisin. Nous transmettons le "
   "rapport et les photos au propriétaire."),
  ("Un contrat d'entretien avant saison, cela existe&nbsp;?",
   "Oui, et pour un bien loué c'est souvent le meilleur calcul&nbsp;: un hydrocurage "
   "programmé au printemps coûte moins cher qu'une urgence un samedi d'août, et il "
   "n'annule pas un séjour."),
 ],
},

{
 "slug": "bac-a-graisse-restaurant-morbihan",
 "court": "Bac à graisse (56)",
 "dept": "56", "act": "degorgement", "date": "2026-09-30",
 "titre": "Bac à graisse saturé (56) : l'urgence des pros — ETS-BZH",
 "h1": "Bac à graisse saturé en restaurant&nbsp;: l'urgence qui ferme un service",
 "meta": ("Bac à graisse saturé dans un restaurant du Morbihan : signes d'alerte, "
          "obligations, fréquence d'entretien et intervention. 02 20 06 00 75."),
 "mots_cles": ("bac à graisse restaurant, dégraissage bac à graisse, entretien "
               "séparateur de graisses, hydrocurage cuisine professionnelle Morbihan"),
 "chapo": ("Pour un restaurant, une évacuation de cuisine qui lâche un vendredi soir "
           "n'est pas un désagrément&nbsp;: c'est un service annulé. Le bac à graisse est "
           "presque toujours en cause, et presque toujours parce qu'il a été entretenu "
           "trop tard. Voici les signes qui précèdent la panne et ce que dit la "
           "réglementation."),
 "urgent": [
   "Arrêtez les rejets en cuisine&nbsp;: plonge, lave-vaisselle, siphons de sol.",
   "Vérifiez le niveau dans le bac&nbsp;: une croûte épaisse en surface ou un "
   "niveau au-dessus de la sortie confirme la saturation.",
   "N'ouvrez pas le bac plus que nécessaire et écartez-vous&nbsp;: les gaz de "
   "fermentation s'y accumulent.",
   "Ne versez aucun produit dégraissant dans le bac&nbsp;: il liquéfie la graisse, "
   "qui repart dans le réseau et se re-fige plus loin, hors d'atteinte.",
   "Appelez&nbsp;: en restauration, le délai d'intervention est le sujet.",
 ],
 "danger": ("Ne faites jamais descendre un employé dans un bac à graisse ou un regard, "
            "même peu profond, et même « juste pour racler ». La fermentation des "
            "graisses produit de l'hydrogène sulfuré, un gaz qui sature l'odorat avant "
            "d'assommer. Ces interventions se font depuis la surface, avec du matériel "
            "de pompage, et jamais à la main."),
 "sections": [
  ("Les signes qui précèdent la panne",
   ["Un bac à graisse ne sature pas du jour au lendemain. Il prévient, et les signes "
    "sont toujours les mêmes.",
    "<strong>L'évacuation de la plonge ralentit</strong> en fin de service, puis toute "
    "la journée. C'est le premier signal, et c'est celui qu'on attribue à tort au "
    "siphon.",
    "<strong>Une odeur revient en cuisine</strong>, surtout le matin à l'ouverture ou "
    "après un week-end de fermeture&nbsp;: la fermentation a travaillé sans dilution.",
    "<strong>Le siphon de sol gargouille</strong> quand le lave-vaisselle vidange.",
    "<strong>La croûte de surface dans le bac dépasse quelques centimètres</strong>, ou "
    "le niveau atteint la canalisation de sortie.",
    "À ce stade, l'intervention est programmable&nbsp;: on choisit le créneau, entre "
    "deux services. Passé ce stade, c'est une urgence, et elle tombe toujours au plus "
    "mauvais moment."],
   None),
  ("Ce que l'établissement doit pouvoir montrer",
   ["Un établissement de restauration qui rejette des graisses au réseau public est "
    "tenu de les prétraiter, et l'équipement doit être entretenu et vidangé "
    "régulièrement. Les modalités précises — dimensionnement, fréquence, justificatifs — "
    "figurent dans le règlement d'assainissement de votre commune ou de votre "
    "agglomération, et dans votre autorisation de déversement si vous en avez une.",
    "Ce qui est demandé en contrôle est simple&nbsp;: la preuve que l'entretien a eu "
    "lieu. Concrètement, les <strong>bordereaux de suivi des déchets</strong> remis à "
    "chaque vidange, qui indiquent le volume évacué, la date et la filière de "
    "traitement. Conservez-les&nbsp;; c'est la seule chose qui vaut en cas de contrôle, "
    "et c'est aussi ce qui vous protège si un bouchon survient en aval de votre "
    "branchement.",
    "Sur le littoral morbihannais, la question a un enjeu supplémentaire&nbsp;: les "
    "communes conchylicoles et les zones de baignade du golfe sont particulièrement "
    "attentives à la qualité des rejets. Les contrôles y sont plus fréquents qu'ailleurs, "
    "et les établissements saisonniers sont les premiers visités."],
   None),
  ("La fréquence qui évite l'urgence",
   [],
   ["Un dégraissage semestriel pour un établissement à l'activité régulière&nbsp;: c'est "
    "le rythme de référence.",
    "Un rythme trimestriel pour une cuisine à forte production de graisses — friture, "
    "grillades, volumes importants.",
    "Une vidange avant et après la saison pour les établissements saisonniers du "
    "littoral&nbsp;: le bac ne doit pas passer l'hiver plein.",
    "Un hydrocurage de la canalisation entre la cuisine et le bac, au moins une fois "
    "par an&nbsp;: c'est là que se forment les bouchons que le bac n'a pas retenus.",
    "Des bacs de récupération pour les huiles de friture, qui ne doivent jamais partir "
    "à l'évacuation&nbsp;: leur filière est distincte.",
    "Un pré-raclage des assiettes et des plaques avant la plonge&nbsp;: la mesure la "
    "plus efficace, et la moins coûteuse."],
   ),
 ],
 "faq": [
  ("Peut-on intervenir en dehors des heures de service&nbsp;?",
   "Oui, et c'est le cas le plus fréquent&nbsp;: nous intervenons tôt le matin, l'après-"
   "midi entre deux services ou le jour de fermeture. Le créneau se cale à l'avance pour "
   "les entretiens programmés."),
  ("Les produits enzymatiques remplacent-ils la vidange&nbsp;?",
   "Non. Ils peuvent ralentir l'encrassement des canalisations, mais ils ne retirent pas "
   "les graisses du bac&nbsp;: elles y sont toujours, et le volume utile continue de "
   "diminuer. La vidange reste obligatoire et les bordereaux aussi."),
  ("Mon bac est-il bien dimensionné&nbsp;?",
   "C'est une question qui se pose quand la saturation revient malgré un entretien "
   "régulier. Le dimensionnement dépend du nombre de couverts et du type de cuisine&nbsp;: "
   "nous vous le disons après intervention, avec les éléments constatés."),
  ("Intervenez-vous sur Vannes, Lorient et le littoral&nbsp;?",
   "Oui, sur l'ensemble du Morbihan, en urgence comme en contrat d'entretien. Les "
   "bordereaux de suivi vous sont remis à chaque passage."),
 ],
},

{
 "slug": "pompe-de-relevage-en-panne-morbihan",
 "court": "Pompe de relevage en panne (56)",
 "dept": "56", "act": "degorgement", "date": "2026-09-30",
 "titre": "Pompe de relevage en panne (56) : l'alarme sonne — ETS-BZH",
 "h1": "Pompe de relevage en panne&nbsp;: l'alarme sonne, combien de temps avez-vous&nbsp;?",
 "meta": "Pompe de relevage en panne dans le Morbihan : que faire quand l'alarme sonne et combien de temps avant le débordement. 02 20 06 00 75.",
 "mots_cles": ("pompe de relevage en panne, alarme poste de relevage, broyeur "
               "assainissement, débordement fosse Morbihan, dépannage pompe eaux usées"),
 "chapo": ("Une pompe de relevage travaille dans l'ombre&nbsp;: tant qu'elle fonctionne, "
           "personne ne sait qu'elle existe. Le jour où elle s'arrête, l'alarme sonne et "
           "le compte à rebours commence — car la cuve continue de se remplir au rythme "
           "de votre consommation, et elle a un volume fini."),
 "urgent": [
   "Réduisez immédiatement les rejets d'eau&nbsp;: c'est ce qui vous donne du temps. "
   "Pas de machine, pas de bain, usage minimal des WC.",
   "Vérifiez que la pompe est bien alimentée&nbsp;: un disjoncteur abaissé au tableau "
   "explique une bonne part des alarmes.",
   "Coupez l'alarme si elle peut l'être, mais ne coupez jamais l'alimentation de la "
   "pompe elle-même&nbsp;: elle redémarrera peut-être seule.",
   "Estimez le temps disponible&nbsp;: une cuve courante de quelques centaines de "
   "litres se remplit en quelques heures d'usage normal.",
   "Appelez sans attendre que ça déborde.",
 ],
 "danger": ("N'ouvrez pas la cuve pour « voir la pompe », et n'y descendez sous aucun "
            "prétexte. Un poste de relevage d'eaux usées accumule des gaz de "
            "fermentation dans un volume confiné, et l'hydrogène sulfuré y est "
            "présent&nbsp;: il endort l'odorat avant d'assommer. Ne tentez pas non plus "
            "de dégager une pompe à la main, même hors tension&nbsp;: le rotor peut se "
            "libérer brutalement."),
 "sections": [
  ("Ce que l'alarme signale, et ce qu'elle ne dit pas",
   ["Une alarme de poste de relevage se déclenche sur un niveau haut&nbsp;: la cuve se "
    "remplit plus vite qu'elle ne se vide. Elle ne dit pas pourquoi, et la cause change "
    "complètement l'intervention.",
    "<strong>La pompe n'est plus alimentée.</strong> Disjoncteur déclenché, "
    "différentiel qui a sauté, coupure de courant. C'est la première chose à vérifier, "
    "et c'est souvent tout.",
    "<strong>Le flotteur est bloqué.</strong> Ce petit interrupteur qui commande le "
    "démarrage se coince dans les dépôts ou s'accroche au câble. La pompe est en parfait "
    "état, elle ne reçoit simplement jamais l'ordre de partir.",
    "<strong>La pompe est bloquée.</strong> Lingettes, cheveux, textile&nbsp;: le rotor "
    "ou le broyeur est pris. C'est de loin la cause la plus fréquente sur les "
    "installations domestiques.",
    "<strong>Le refoulement est obstrué.</strong> La pompe tourne mais ne refoule "
    "plus&nbsp;: clapet anti-retour bloqué, conduite de refoulement colmatée. On "
    "l'entend fonctionner sans que le niveau ne descende.",
    "<strong>La pompe est hors service.</strong> Moteur grillé, étanchéité perdue. Là, "
    "c'est un remplacement."],
   None),
  ("Le Morbihan, terre de postes de relevage",
   ["Le département compte une densité inhabituelle d'installations de relevage, pour "
    "trois raisons qui se cumulent sur le littoral.",
    "La <strong>topographie</strong> d'abord&nbsp;: autour du golfe, sur la presqu'île "
    "de Rhuys et le long de la côte, beaucoup de maisons sont en contrebas du réseau "
    "public. L'écoulement gravitaire est impossible, il faut relever.",
    "Les <strong>nappes hautes</strong> ensuite&nbsp;: en zone littorale, on ne peut pas "
    "toujours enterrer un réseau assez profondément pour garder une pente. La pompe "
    "compense.",
    "Les <strong>extensions</strong> enfin&nbsp;: une salle de bain créée en sous-sol, "
    "une dépendance aménagée, un studio en rez-de-jardin. Chaque aménagement en contrebas "
    "ajoute un petit poste de relevage, souvent un broyeur, souvent oublié.",
    "Ces installations ont un point commun&nbsp;: elles ne tolèrent pas les lingettes. "
    "Un broyeur domestique est conçu pour du papier hygiénique et rien d'autre. En "
    "location saisonnière, où les usages sont inconnus, c'est la panne numéro un."],
   None),
  ("Ce qui évite l'appel d'urgence",
   [],
   ["Une alarme sonore <em>et</em> visuelle, vérifiée une fois par an&nbsp;: une alarme "
    "muette ne sert à rien.",
    "Un contrôle annuel du flotteur et un nettoyage de la cuve&nbsp;: c'est l'entretien "
    "qui évite la majorité des pannes.",
    "Rien d'autre que du papier hygiénique dans les WC raccordés à un broyeur, et une "
    "consigne affichée en location.",
    "Pas de lingettes, pas de protections hygiéniques, pas de graisses de cuisson dans "
    "un réseau qui passe par une pompe.",
    "Une pompe de secours ou un contrat d'intervention quand l'installation dessert un "
    "logement sans autre solution — c'est le cas de beaucoup de maisons en contrebas.",
    "Le disjoncteur de la pompe repéré et étiqueté au tableau&nbsp;: en urgence, on "
    "gagne dix minutes rien qu'avec cela."],
   ),
 ],
 "faq": [
  ("Combien de temps avant que ça déborde&nbsp;?",
   "Cela dépend du volume de la cuve et de votre consommation. Sur une installation "
   "domestique courante, quelques heures d'usage normal suffisent à atteindre le niveau "
   "critique. En réduisant fortement les rejets, on gagne souvent une demi-journée — "
   "assez pour intervenir dans de bonnes conditions."),
  ("Puis-je débloquer la pompe moi-même&nbsp;?",
   "Non, et ce n'est pas une question de compétence technique&nbsp;: c'est une question "
   "de gaz confinés et de risque mécanique. L'intervention se fait avec le matériel "
   "adapté, depuis la surface."),
  ("Faut-il remplacer la pompe ou la nettoyer&nbsp;?",
   "Dans la majorité des cas, un dégagement et un nettoyage suffisent, et l'appareil "
   "repart. Le remplacement se pose quand le moteur a chauffé à vide, quand "
   "l'étanchéité est perdue, ou sur une pompe en fin de vie. Nous vous le disons "
   "franchement, chiffres à l'appui."),
  ("Intervenez-vous la nuit sur le littoral morbihannais&nbsp;?",
   "Oui, 24h/24 et 7j/7, de Vannes à Lorient et sur les communes du golfe et de la "
   "presqu'île. Une alarme de relevage fait partie des situations que nous traitons en "
   "astreinte&nbsp;: attendre le lendemain, c'est souvent nettoyer un débordement."),
 ],
},

{
 "slug": "fuite-au-compteur-facture-anormale-morbihan",
 "court": "Facture d'eau anormale (56)",
 "dept": "56", "act": "plomberie", "date": "2026-09-30",
 "titre": "Facture d'eau anormale (56) : trouver la fuite — ETS-BZH",
 "h1": "Facture d'eau qui explose dans le Morbihan&nbsp;: la méthode pour trouver la fuite",
 "meta": ("Facture d'eau anormale dans le Morbihan : isoler la fuite étape par étape, "
          "et faire jouer l'écrêtement dans les délais. 02 20 06 00 75."),
 "mots_cles": ("facture d'eau anormale, fuite invisible, écrêtement facture d'eau, "
               "recherche de fuite Vannes, compteur qui tourne Morbihan"),
 "chapo": ("Une facture d'eau qui double n'est presque jamais une erreur de relevé. "
           "C'est une fuite, et elle coule depuis des mois. La bonne nouvelle&nbsp;: une "
           "méthode simple permet de la localiser par élimination, et un dispositif "
           "légal permet d'en limiter le coût — à condition d'agir dans les délais."),
 "urgent": [
   "Fermez tous les robinets, arrêtez les appareils, y compris le remplissage des "
   "WC, l'adoucisseur et l'arrosage automatique.",
   "Relevez le compteur, attendez une heure sans rien consommer, relevez à "
   "nouveau. Un index qui bouge confirme la fuite.",
   "Fermez la vanne d'entrée de la maison et refaites l'essai&nbsp;: si le compteur "
   "tourne toujours, la fuite est sur la portion enterrée.",
   "Photographiez chaque relevé avec l'heure&nbsp;: ce sont vos pièces.",
   "Renseignez-vous immédiatement sur le délai d'écrêtement auprès de votre service "
   "des eaux&nbsp;: il est court, et il se rate facilement.",
 ],
 "danger": ("Ne creusez pas au jugé pour chercher une fuite enterrée. La zone humide "
            "en surface n'est presque jamais à l'aplomb du percement&nbsp;: l'eau suit la "
            "tranchée de pose et ressort ailleurs. Une tranchée ouverte au mauvais "
            "endroit coûte plus cher que la localisation, et risque d'endommager "
            "d'autres réseaux enterrés."),
 "sections": [
  ("Isoler par élimination, du plus simple au plus profond",
   ["La recherche suit un ordre, et chaque étape élimine une zone.",
    "<strong>Étape 1 — les appareils sanitaires.</strong> Une chasse d'eau qui fuit en "
    "continu est la première cause de surconsommation invisible. Le test&nbsp;: posez du "
    "papier toilette contre la paroi arrière de la cuvette, au-dessus du niveau d'eau. "
    "S'il se mouille, c'est trouvé. Faites-le sur chaque WC de la maison, y compris ceux "
    "que personne n'utilise.",
    "<strong>Étape 2 — le chauffe-eau.</strong> Un groupe de sécurité qui coule en "
    "dehors des phases de chauffe évacue en continu, directement à l'égout. Personne ne "
    "le voit.",
    "<strong>Étape 3 — les points extérieurs.</strong> Robinet de jardin, arrosage "
    "automatique, remplissage de piscine, local technique. Ce sont les fuites les plus "
    "longtemps invisibles, parce que l'eau part dans le sol.",
    "<strong>Étape 4 — la portion enterrée.</strong> Si le compteur tourne alors que la "
    "vanne d'entrée de la maison est fermée, la fuite est entre le compteur et la "
    "maison. Là, il faut localiser avant d'ouvrir."],
   None),
  ("L'écrêtement : un droit, mais avec un délai",
   ["La loi prévoit, pour les logements, un dispositif d'écrêtement de la facture en cas "
    "de fuite sur une canalisation après compteur. Le principe&nbsp;: au-delà d'un "
    "certain seuil de surconsommation, la part excédentaire n'est pas facturée, sous "
    "conditions.",
    "Trois points à retenir, parce que c'est là que les dossiers échouent. "
    "<strong>Le champ est limité</strong>&nbsp;: le dispositif vise les fuites sur "
    "canalisation, pas les appareils sanitaires — une chasse d'eau ou un robinet qui "
    "fuit n'y ouvrent pas droit. <strong>Le délai est court</strong>&nbsp;: il court à "
    "compter de l'information que vous adresse le service des eaux, et il se compte en "
    "semaines. <strong>Il faut une attestation</strong>&nbsp;: une facture d'entreprise "
    "détaillant la localisation et la nature de la fuite, ainsi que la date de "
    "réparation.",
    "Concrètement&nbsp;: appelez votre service des eaux dès que vous suspectez la fuite, "
    "demandez la procédure exacte et le délai, faites réparer, et transmettez la facture "
    "détaillée. Nous rédigeons nos interventions dans ce format pour que le dossier "
    "passe sans aller-retour."],
   None),
  ("Le Morbihan ajoute deux causes particulières",
   [],
   ["<strong>Les piscines et leurs locaux techniques</strong>&nbsp;: très nombreux dans "
    "le département. Une fuite sur un circuit de filtration ou un bassin masquée par un "
    "remplissage automatique peut couler des mois sans aucun signe.",
    "<strong>Les résidences secondaires</strong>&nbsp;: une fuite qui se déclare en "
    "octobre dans une maison fermée est découverte en avril, sur la facture. C'est le "
    "scénario le plus coûteux du département.",
    "Les arrosages automatiques programmés, dont une électrovanne bloquée passe "
    "totalement inaperçue.",
    "Les conduites enterrées longues, sur des terrains où la maison est loin de la "
    "limite de propriété.",
    "Les réseaux anciens en polyéthylène de première génération, qui se fendent aux "
    "raccords.",
    "La parade universelle pour une maison peu occupée&nbsp;: fermer l'arrivée générale "
    "à chaque départ prolongé."],
   ),
 ],
 "faq": [
  ("Mon compteur tourne même vanne fermée, que faire&nbsp;?",
   "La fuite est entre le compteur et votre vanne d'entrée, donc sur la portion "
   "enterrée qui vous appartient. Il faut une recherche de fuite avant de creuser&nbsp;: "
   "corrélation acoustique, gaz traceur ou caméra thermique selon la configuration."),
  ("Combien de temps pour localiser une fuite enterrée&nbsp;?",
   "En général une demi-journée, selon la longueur du tracé et la nature du sol. "
   "L'objectif est d'ouvrir un mètre carré au bon endroit plutôt qu'une tranchée "
   "complète."),
  ("L'écrêtement est-il automatique&nbsp;?",
   "Non. Il faut en faire la demande, dans le délai indiqué par le service des eaux, en "
   "joignant l'attestation de réparation. Renseignez-vous dès le premier soupçon&nbsp;: "
   "c'est le délai qui fait échouer la plupart des dossiers, pas le fond."),
  ("Intervenez-vous sur tout le Morbihan&nbsp;?",
   "Oui, de Vannes à Lorient, Pontivy et Auray, ainsi que sur les communes du littoral "
   "et du golfe. Devis gratuit et rapport rédigé pour être exploitable par votre service "
   "des eaux."),
 ],
},

{
 "slug": "vanne-d-arret-bloquee-morbihan",
 "court": "Vanne d'arrêt bloquée (56)",
 "dept": "56", "act": "plomberie", "date": "2026-09-30",
 "titre": "Vanne d'arrêt bloquée (56) : où couper — ETS-BZH",
 "h1": "Impossible de couper l'eau&nbsp;: quand la vanne d'arrêt refuse de tourner",
 "meta": "Vanne d'arrêt bloquée dans le Morbihan : où couper l'eau quand la vanne générale ne ferme plus, et pourquoi la remplacer. 02 20 06 00 75.",
 "mots_cles": ("vanne d'arrêt bloquée, couper l'eau maison, robinet d'arrêt grippé, "
               "vanne compteur, plombier urgence Morbihan"),
 "chapo": ("Il y a un moment où l'on découvre que la vanne générale ne tourne plus&nbsp;: "
           "c'est précisément celui où l'on a besoin de couper l'eau. Cette page décrit "
           "quoi faire dans l'instant, et pourquoi une vanne qui n'a jamais été manœuvrée "
           "est un problème en attente."),
 "urgent": [
   "Ne forcez pas sur une vanne grippée&nbsp;: elle casse, et une fuite maîtrisable "
   "devient une fuite franche que plus rien n'arrête.",
   "Cherchez les vannes intermédiaires&nbsp;: sous l'évier, derrière le WC, au pied "
   "du chauffe-eau. L'une d'elles isole peut-être déjà la fuite.",
   "Sinon, allez au compteur&nbsp;: il y a presque toujours une vanne juste avant ou "
   "juste après, dans le regard ou le local technique.",
   "Si rien ne ferme, appelez le service des eaux&nbsp;: il peut couper au compteur "
   "en urgence.",
   "En attendant, limitez les dégâts&nbsp;: récipients, serpillières, coupure "
   "électrique de la zone si l'eau approche d'une prise.",
 ],
 "danger": ("Une vanne qui n'a jamais été manœuvrée depuis des années casse souvent au "
            "premier effort, en particulier les modèles à tête ronde à joint de "
            "presse-étoupe. Si vous devez essayer, faites-le doucement, sans clé ni "
            "rallonge de bras, et arrêtez au premier point dur. Une vanne cassée en "
            "position ouverte pendant une fuite est la pire situation possible."),
 "sections": [
  ("Où sont les vannes, dans l'ordre",
   ["Une maison comporte plusieurs niveaux de coupure, et il est utile de les connaître "
    "avant d'en avoir besoin.",
    "<strong>Les robinets d'arrêt d'appareil</strong>&nbsp;: sous l'évier, sous le "
    "lavabo, derrière le WC, à l'arrivée du lave-linge. Ils isolent un seul point d'eau. "
    "Ce sont les plus souvent grippés, parce que personne ne les touche jamais.",
    "<strong>La vanne d'arrivée générale du logement</strong>&nbsp;: en général près de "
    "l'entrée de la conduite, dans un placard technique, un garage, une buanderie ou "
    "sous un évier de cuisine. C'est celle qu'il faut savoir localiser les yeux fermés.",
    "<strong>La vanne au compteur</strong>&nbsp;: dans le regard extérieur ou le local "
    "de comptage. Elle coupe tout, et elle appartient en général au périmètre du service "
    "des eaux selon les cas.",
    "<strong>Les vannes de zone</strong>, sur les installations récentes&nbsp;: une par "
    "niveau ou par circuit. Elles permettent d'isoler sans priver toute la maison, et "
    "c'est un confort réel lors d'une réparation."],
   None),
  ("Pourquoi les vannes se bloquent, et surtout ici",
   ["Une vanne se grippe par immobilité. Le joint de presse-étoupe sèche, les dépôts "
    "s'accumulent sur la tige, et la pièce se soude progressivement dans sa position. "
    "Une vanne manœuvrée deux fois par an ne se bloque presque jamais&nbsp;; une vanne "
    "jamais touchée depuis la construction se bloque presque toujours.",
    "Sur le littoral morbihannais, deux facteurs accélèrent le phénomène. L'humidité "
    "permanente et l'air salin, qui attaquent les parties métalliques dans les regards "
    "extérieurs et les locaux non chauffés. Et le rythme d'occupation&nbsp;: dans une "
    "résidence secondaire, l'installation reste immobile dix mois par an.",
    "Il y a là un paradoxe qu'il vaut mieux connaître&nbsp;: ce sont les maisons les "
    "moins occupées, donc celles où une fuite ferait le plus de dégâts avant d'être "
    "découverte, qui ont les vannes les plus susceptibles de ne pas fonctionner le jour "
    "où on en a besoin."],
   None),
  ("Le quart d'heure qui change tout",
   [],
   ["Localisez votre vanne générale <em>maintenant</em>, pas le jour de la fuite. "
    "Montrez-la aux autres occupants.",
    "Manœuvrez-la une à deux fois par an, doucement, fermeture puis réouverture "
    "complète&nbsp;: c'est le seul entretien qui existe.",
    "Faites de même avec les robinets d'arrêt sous les appareils.",
    "Remplacez les vannes à tête ronde anciennes par des vannes quart de tour&nbsp;: "
    "elles se bloquent beaucoup moins et se manœuvrent d'un geste.",
    "Dégagez l'accès&nbsp;: une vanne derrière un meuble ou sous un carton n'est pas "
    "une vanne accessible en urgence.",
    "Dans une maison peu occupée&nbsp;: fermez l'arrivée générale à chaque départ "
    "prolongé. Cela règle la question avant qu'elle ne se pose."],
   ),
 ],
 "faq": [
  ("La vanne tourne mais l'eau coule encore&nbsp;?",
   "Le mécanisme interne est détruit&nbsp;: la vanne tourne à vide. C'est fréquent sur "
   "les modèles anciens. Elle doit être remplacée, et en attendant il faut couper plus "
   "en amont, au compteur."),
  ("Puis-je remplacer une vanne moi-même&nbsp;?",
   "Cela demande de couper en amont — donc d'avoir une autre vanne fonctionnelle, ce "
   "qui est précisément le problème — et de travailler sur une conduite sous pression si "
   "la coupure échoue. C'est le type d'intervention où l'on gagne à ne pas improviser."),
  ("Le service des eaux peut-il couper en urgence&nbsp;?",
   "Oui, il dispose d'une astreinte pour intervenir au compteur. Le numéro figure sur "
   "votre facture d'eau. C'est la bonne solution quand plus rien ne ferme chez vous."),
  ("Intervenez-vous en urgence pour remplacer une vanne&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur le Morbihan. Et si nous intervenons chez vous pour autre "
   "chose, nous vous signalons systématiquement les vannes grippées&nbsp;: c'est peu de "
   "chose à remplacer à froid, et beaucoup à subir en urgence."),
 ],
},

{
 "slug": "coup-de-belier-bruits-canalisations-morbihan",
 "court": "Coup de bélier (56)",
 "dept": "56", "act": "plomberie", "date": "2026-09-30",
 "titre": "Coup de bélier et bruits dans les tuyaux (56) — ETS-BZH",
 "h1": "Coup de bélier&nbsp;: le bruit sourd qui finit par casser un raccord",
 "meta": ("Coup de bélier et bruits dans les canalisations dans le Morbihan : d'où "
          "vient le choc, pourquoi il abîme, et comment le supprimer. 02 20 06 00 75."),
 "mots_cles": ("coup de bélier plomberie, bruit dans les tuyaux, canalisation qui "
               "claque, anti-bélier, pression d'eau trop forte Morbihan"),
 "chapo": ("Un claquement sourd dans les murs quand le lave-linge coupe son "
           "remplissage, un tuyau qui vibre quand on ferme un mitigeur&nbsp;: ce n'est "
           "pas seulement agaçant. Chaque coup de bélier est un choc de pression qui "
           "fatigue les raccords — et ce sont ces raccords-là qui finissent par lâcher."),
 "urgent": [
   "Repérez à quel moment le bruit se produit&nbsp;: à la fermeture d'un robinet, au "
   "démarrage ou à l'arrêt d'un appareil, ou en continu. C'est l'indice principal.",
   "Fermez les mitigeurs plus lentement&nbsp;: si le bruit disparaît, le diagnostic "
   "est confirmé.",
   "Relevez la pression si vous avez un manomètre&nbsp;: au-delà de 3 bars, elle "
   "amplifie tout.",
   "Vérifiez la fixation des tuyaux apparents&nbsp;: un collier desserré transforme "
   "un choc en vacarme.",
 ],
 "danger": ("Ne considérez pas un coup de bélier comme un simple bruit à supporter. "
            "Chaque choc envoie une surpression brutale dans le réseau, et elle "
            "s'applique à tous les raccords, y compris ceux qui sont encastrés et "
            "inaccessibles. C'est un des mécanismes classiques derrière les fuites "
            "encastrées qui apparaissent « sans raison » quelques années plus tard."),
 "sections": [
  ("Ce qui se passe réellement dans le tuyau",
   ["L'eau en mouvement a une inertie. Quand une vanne se ferme brutalement — un "
    "mitigeur à cartouche, l'électrovanne d'un lave-linge, un robinet quart de tour — la "
    "colonne d'eau s'arrête d'un coup, et son énergie se transforme en onde de pression "
    "qui remonte le réseau puis revient. C'est ce va-et-vient qui produit le claquement.",
    "Trois facteurs amplifient le phénomène. Une <strong>pression de service "
    "élevée</strong>&nbsp;: plus elle est forte, plus l'onde est violente. Des "
    "<strong>tuyaux mal fixés</strong>&nbsp;: ils bougent, frappent la structure et "
    "transforment un choc hydraulique en bruit de percussion. Et l'<strong>absence de "
    "dispositif d'amortissement</strong>, qui devrait absorber l'onde au lieu de la "
    "laisser se propager.",
    "Il faut distinguer le coup de bélier d'autres bruits qui n'ont rien à voir&nbsp;: "
    "un sifflement continu signale plutôt un passage étranglé ou une pression excessive, "
    "un ronronnement vient souvent d'un appareil ou d'une pompe, et un tuyau qui "
    "« chante » à un débit précis indique un diamètre insuffisant."],
   None),
  ("Pression et surpresseurs : la spécificité locale",
   ["Le Morbihan présente une configuration qui favorise les coups de bélier. Sur les "
    "communes littorales et les secteurs vallonnés du golfe, la pression du réseau varie "
    "fortement selon l'altitude et la distance au réservoir, et elle peut être élevée en "
    "point bas.",
    "S'y ajoute la <strong>saisonnalité</strong>&nbsp;: les variations de consommation "
    "entre l'hiver et le mois d'août modifient la pression disponible, parfois "
    "sensiblement. Une installation calme onze mois par an peut se mettre à claquer en "
    "plein été, sans que rien n'ait changé chez vous.",
    "Enfin, beaucoup de maisons du département sont équipées d'un <strong>surpresseur</strong> "
    "ou alimentées par un forage privé. Un surpresseur mal réglé, ou dont le ballon a "
    "perdu sa pression d'air, provoque des démarrages et des arrêts brutaux qui sont "
    "eux-mêmes une source de coups de bélier — et il s'use d'autant plus vite.",
    "C'est pourquoi la première chose que nous mesurons est la pression, en statique et "
    "en dynamique&nbsp;: c'est elle qui dicte la solution."],
   None),
  ("Les solutions, dans l'ordre de simplicité",
   [],
   ["<strong>Régler ou installer un réducteur de pression</strong> en entrée "
    "d'installation&nbsp;: c'est la mesure la plus efficace quand la pression est "
    "élevée, et elle protège tout le réseau.",
    "<strong>Reprendre les fixations</strong> des tuyaux apparents&nbsp;: colliers "
    "resserrés et supports intermédiaires suppriment l'essentiel du bruit perçu.",
    "<strong>Poser un anti-bélier</strong> au plus près des appareils à fermeture "
    "rapide — lave-linge, lave-vaisselle&nbsp;: il absorbe l'onde là où elle naît.",
    "<strong>Vérifier le surpresseur</strong>&nbsp;: pression du ballon, réglage du "
    "pressostat, état du clapet.",
    "<strong>Remplacer une robinetterie</strong> dont la fermeture est trop brutale, sur "
    "les points les plus sollicités.",
    "<strong>Contrôler le vase d'expansion sanitaire</strong> quand il y en a un&nbsp;: "
    "il joue aussi un rôle d'amortissement."],
   ),
 ],
 "faq": [
  ("Le bruit n'est pas très fort, dois-je m'en occuper&nbsp;?",
   "L'intensité du bruit ne dit pas grand-chose de l'intensité du choc&nbsp;: un coup de "
   "bélier discret dans une installation encastrée fatigue tout autant les raccords. Si "
   "le phénomène est régulier, il vaut la peine d'être traité."),
  ("Un anti-bélier suffit-il&nbsp;?",
   "Il traite très bien un point précis, typiquement l'arrivée d'un lave-linge. Si la "
   "pression générale est trop élevée, c'est le réducteur en tête d'installation qui "
   "règle le problème de fond&nbsp;; l'anti-bélier vient en complément."),
  ("Mes tuyaux sifflent quand j'ouvre un robinet, est-ce la même chose&nbsp;?",
   "Non. Un sifflement continu évoque plutôt une pression excessive, un mousseur "
   "colmaté ou un passage étranglé. Le diagnostic est différent, mais la mesure de "
   "pression est le point de départ dans les deux cas."),
  ("Intervenez-vous pour un simple problème de bruit&nbsp;?",
   "Oui, et c'est une intervention préventive utile&nbsp;: elle coûte bien moins qu'une "
   "fuite encastrée quelques années plus tard. Devis gratuit sur l'ensemble du Morbihan."),
 ],
},

{
 "slug": "ballon-d-eau-chaude-ne-chauffe-plus-morbihan",
 "court": "Le ballon ne chauffe plus (56)",
 "dept": "56", "act": "electricite", "date": "2026-09-30",
 "titre": "Le ballon ne chauffe plus (56) : côté électrique — ETS-BZH",
 "h1": "Le ballon ne chauffe plus&nbsp;: quand le problème est électrique, pas sanitaire",
 "meta": 'Chauffe-eau qui ne chauffe plus dans le Morbihan : contacteur, disjoncteur, thermostat. Les vérifications côté électrique. 02 20 06 00 75.',
 "mots_cles": ("ballon ne chauffe plus, contacteur jour nuit, marche forcée chauffe-eau, "
               "heures creuses chauffe-eau, électricien Vannes"),
 "chapo": ("Quand l'eau chaude disparaît, on pense au chauffe-eau. Pourtant, dans une "
           "grande part des cas, l'appareil est intact&nbsp;: c'est sa commande "
           "électrique qui ne fait plus son travail. Deux minutes devant le tableau "
           "suffisent souvent à le vérifier, et parfois à récupérer l'eau chaude le soir "
           "même."),
 "urgent": [
   "Regardez le tableau&nbsp;: le disjoncteur du chauffe-eau est-il bien relevé&nbsp;?",
   "Trouvez le contacteur jour/nuit, un petit boîtier avec un sélecteur à trois "
   "positions, et placez-le sur I ou « marche forcée ».",
   "Attendez deux heures, puis testez l'eau chaude. Si elle est revenue, le "
   "diagnostic est fait.",
   "Remettez ensuite le sélecteur sur Auto&nbsp;: s'il n'y a plus d'eau chaude le "
   "lendemain, le contacteur ou son signal est en cause.",
   "Regardez sous l'appareil&nbsp;: la moindre trace d'eau change complètement le "
   "diagnostic.",
 ],
 "danger": ("N'ouvrez pas le capot du chauffe-eau sans avoir coupé son disjoncteur au "
            "tableau&nbsp;: les bornes de la résistance et du thermostat restent sous "
            "tension même si l'appareil ne chauffe pas. Et ne remettez jamais sous "
            "tension un ballon vidangé&nbsp;: une résistance alimentée à vide grille en "
            "quelques minutes, et le remplacement devient inévitable."),
 "sections": [
  ("Le contacteur jour/nuit, pièce la plus sous-estimée du tableau",
   ["Sur une installation en heures creuses, le chauffe-eau n'est pas alimenté en "
    "permanence&nbsp;: un contacteur reçoit un signal du compteur et ferme le circuit "
    "pendant les plages autorisées. C'est une pièce mécanique, avec des contacts, et "
    "elle s'use.",
    "Trois pannes s'y rattachent. Le <strong>contacteur lui-même</strong>, dont les "
    "contacts sont piqués ou collés&nbsp;: il ne ferme plus, ou il reste fermé en "
    "permanence — ce qui coûte cher sans qu'on s'en aperçoive. Le <strong>signal</strong> "
    "en provenance du compteur, qui ne parvient plus, notamment après un changement de "
    "compteur ou de contrat. Et le <strong>sélecteur</strong>, laissé sur 0 par "
    "quelqu'un sans le savoir&nbsp;: c'est plus fréquent qu'on ne l'imagine, notamment "
    "dans une maison louée ou après le passage d'un artisan.",
    "Le test de la marche forcée tranche entre toutes ces hypothèses en deux heures. "
    "S'il y a de l'eau chaude en forcé mais plus rien en automatique, le problème est là, "
    "et il ne s'agit ni du ballon, ni de la résistance."],
   None),
  ("Le cas des maisons occupées par intermittence",
   ["Dans le Morbihan, une part importante du parc est constituée de résidences "
    "secondaires et de locations saisonnières, et le chauffe-eau y subit un régime "
    "atypique qui crée ses propres pannes électriques.",
    "Le plus courant&nbsp;: à la fermeture de saison, le propriétaire coupe le "
    "disjoncteur du ballon, ce qui est la bonne pratique. À la réouverture, il remet le "
    "courant... et remet aussi l'eau, mais parfois dans le mauvais ordre. Un ballon vidé "
    "ou partiellement vide qu'on alimente grille sa résistance immédiatement. L'ordre est "
    "toujours le même&nbsp;: <strong>remplir d'abord, alimenter ensuite</strong>, après "
    "avoir vérifié qu'un robinet d'eau chaude coule sans à-coups.",
    "Autre situation locale&nbsp;: l'air salin sur les communes du littoral. Les "
    "tableaux installés en garage, en buanderie ou en local technique ouvert voient "
    "leurs contacts se dégrader plus vite, contacteur compris. Ce n'est pas une panne "
    "brutale&nbsp;: c'est une dégradation lente, qui finit par un contact qui ne "
    "transmet plus."],
   None),
  ("La séquence complète de vérification",
   [],
   ["Le disjoncteur du chauffe-eau au tableau&nbsp;: relevé, et non en position "
    "intermédiaire.",
    "Le contacteur jour/nuit&nbsp;: position du sélecteur, puis test en marche forcée.",
    "La présence du signal heures creuses, si l'installation en dépend.",
    "Le thermostat de l'appareil, qui peut s'être mis en sécurité&nbsp;: un réarmement "
    "existe, mais un déclenchement répété signale une cause à traiter.",
    "La résistance, dont la mesure dit immédiatement si elle est coupée.",
    "L'état général du tableau&nbsp;: un contacteur qui chauffe ou qui claque "
    "anormalement doit être remplacé, pas seulement remis en service."],
   ),
 ],
 "faq": [
  ("La marche forcée fonctionne, mais rien en automatique&nbsp;?",
   "C'est le contacteur ou le signal heures creuses. La pièce se remplace rapidement et "
   "le fonctionnement normal revient. Laisser durablement l'appareil en marche forcée "
   "fonctionne, mais vous chauffez alors en heures pleines&nbsp;: la facture s'en "
   "ressentira."),
  ("Mon contacteur claque plusieurs fois par jour, est-ce normal&nbsp;?",
   "Il doit commuter au début et à la fin des plages d'heures creuses, pas en "
   "permanence. Des commutations répétées signalent un contact usé ou un signal "
   "instable, et cela finit par une panne franche."),
  ("Puis-je me passer du contacteur et alimenter le ballon en direct&nbsp;?",
   "Techniquement oui, et cela dépanne. Mais vous perdez le bénéfice des heures creuses, "
   "et sur un chauffe-eau c'est l'un des postes où l'écart de tarif compte le plus. "
   "Mieux vaut remplacer la pièce."),
  ("Intervenez-vous en urgence sur Vannes et Lorient&nbsp;?",
   "Oui, 24h/24 et 7j/7 sur l'ensemble du Morbihan. Si la pièce est courante — "
   "contacteur, thermostat, résistance — nos véhicules l'ont à bord et l'eau chaude "
   "revient dans la journée."),
 ],
},

{
 "slug": "borne-de-recharge-qui-disjoncte-morbihan",
 "court": "Forte puissance qui disjoncte (56)",
 "dept": "56", "act": "electricite", "date": "2026-09-30",
 "titre": "Borne de recharge qui disjoncte (56) : pourquoi — ETS-BZH",
 "h1": "Borne de recharge ou gros appareil qui fait disjoncter&nbsp;: la question du circuit dédié",
 "meta": ("Borne de recharge, plaque ou sèche-linge qui fait disjoncter dans le "
          "Morbihan : circuit dédié, puissance, différentiel adapté. 02 20 06 00 75."),
 "mots_cles": ("borne de recharge disjoncte, circuit dédié forte puissance, prise "
               "renforcée voiture électrique, différentiel type A, électricien Morbihan"),
 "chapo": ("Une borne de recharge, une plaque à induction ou un sèche-linge qui fait "
           "sauter le tableau n'est presque jamais un appareil défectueux&nbsp;: c'est "
           "un appareil de forte puissance branché sur un circuit qui n'a pas été prévu "
           "pour lui. Et dans ce cas, la rallonge et la multiprise ne sont pas une "
           "solution — elles sont le problème."),
 "urgent": [
   "Débranchez l'appareil avant de réarmer, et notez ce qui fonctionnait en même "
   "temps.",
   "Vérifiez lequel a sauté&nbsp;: un disjoncteur divisionnaire, le différentiel, ou "
   "le disjoncteur de branchement. Ce sont trois causes différentes.",
   "Touchez la prise et la fiche&nbsp;: si elles sont chaudes, cessez immédiatement "
   "d'utiliser cette prise pour cet appareil.",
   "N'utilisez jamais de rallonge ni de multiprise pour un appareil de forte "
   "puissance, et encore moins pour recharger un véhicule.",
 ],
 "danger": ("Recharger un véhicule électrique sur une prise domestique ordinaire, par "
            "une rallonge ou une multiprise, est la configuration la plus dangereuse de "
            "cette page. Une charge dure plusieurs heures à courant élevé, sans "
            "interruption&nbsp;: une prise standard et ses contacts ne sont pas conçus "
            "pour ce régime. L'échauffement se produit à l'intérieur de la prise, dans "
            "la cloison, là où rien ne se voit et où aucun disjoncteur ne coupera."),
 "sections": [
  ("Ce qu'est un circuit dédié, et pourquoi il change tout",
   ["Un circuit dédié, c'est une ligne qui part du tableau et va directement à un seul "
    "appareil, avec une section de câble et une protection choisies pour lui. Rien "
    "d'autre n'est branché dessus.",
    "L'intérêt est double. D'abord la <strong>section du conducteur</strong>&nbsp;: un "
    "appareil de forte puissance demande un câble plus gros, capable de dissiper la "
    "chaleur produite. Ensuite l'<strong>indépendance</strong>&nbsp;: l'appareil ne "
    "partage plus sa ligne avec d'autres, donc plus de cumul qui fait sauter la "
    "protection.",
    "Les appareils qui en relèvent sont connus&nbsp;: plaque de cuisson, four, "
    "lave-linge, lave-vaisselle, sèche-linge, chauffe-eau, et bien sûr borne de recharge. "
    "Dans une installation aux normes actuelles, chacun a sa ligne.",
    "Dans les logements plus anciens du département — et le Morbihan en compte beaucoup, "
    "notamment dans les bourgs et sur le littoral —, ces circuits n'existent pas. Tout "
    "est branché sur les lignes de prises d'origine, conçues pour de l'éclairage et "
    "quelques appareils légers."],
   None),
  ("La recharge de véhicule : un cas à part",
   ["La recharge automobile n'est pas un usage comme un autre. Elle combine un courant "
    "élevé et une durée longue&nbsp;: plusieurs heures d'affilée, souvent la nuit, "
    "souvent sans personne pour surveiller. C'est exactement le régime qui fait "
    "apparaître les défauts de contact.",
    "Trois éléments sont nécessaires, et aucun ne se remplace. Un <strong>circuit "
    "dédié</strong> de section adaptée, partant du tableau. Une <strong>protection "
    "différentielle du type approprié</strong>&nbsp;: les chargeurs embarqués peuvent "
    "générer des courants de fuite que tous les différentiels ne détectent pas — la "
    "protection doit être choisie en conséquence. Et un <strong>point de charge "
    "prévu pour cet usage</strong>&nbsp;: borne murale ou prise renforcée, pas une prise "
    "de courant ordinaire.",
    "Un mot sur l'environnement local&nbsp;: sur le littoral morbihannais, beaucoup de "
    "points de charge sont installés en garage ouvert, sous auvent ou en extérieur. "
    "L'air salin attaque les contacts, et l'indice de protection du matériel comme la "
    "qualité de la prise de terre prennent alors une importance particulière. Une terre "
    "dégradée rend la protection différentielle inopérante au moment où l'on en aurait "
    "besoin."],
   None),
  ("Ce que nous vérifions avant d'installer",
   [],
   ["La puissance souscrite et la marge réellement disponible aux heures de charge.",
    "La section des conducteurs en tête d'installation et l'état du tableau.",
    "La valeur de la prise de terre, mesurée et non estimée.",
    "Le type de protection différentielle, adapté au matériel installé.",
    "La possibilité d'un pilotage de charge, pour éviter le cumul avec les autres gros "
    "appareils aux mêmes heures.",
    "L'environnement du point de charge&nbsp;: exposition, humidité, indice de "
    "protection du matériel, cheminement du câble.",
    "L'état des connexions existantes&nbsp;: un serrage qui a pris du jeu chauffera "
    "d'autant plus qu'on augmente le courant."],
   ),
 ],
 "faq": [
  ("Une prise renforcée suffit-elle&nbsp;?",
   "Elle est conçue pour la recharge et convient à des puissances modérées, à condition "
   "d'être alimentée par un circuit dédié et correctement protégée. Elle reste plus "
   "limitée qu'une borne murale en puissance et en fonctions, mais elle est infiniment "
   "préférable à une prise ordinaire."),
  ("Ma prise chauffe pendant la charge, est-ce grave&nbsp;?",
   "Oui. Une prise tiède après quelques heures signale déjà un contact qui résiste, et "
   "une prise chaude est à quelques étapes de la carbonisation de son support. Cessez "
   "immédiatement de l'utiliser pour cet usage et faites contrôler le circuit."),
  ("Faut-il augmenter ma puissance souscrite pour une borne&nbsp;?",
   "Pas toujours. Cela dépend de la puissance de charge visée et de vos usages "
   "simultanés. Un pilotage de charge permet souvent de rester sur l'abonnement "
   "existant&nbsp;: c'est une des choses que nous évaluons avant de chiffrer."),
  ("Intervenez-vous pour l'installation d'un point de charge dans le Morbihan&nbsp;?",
   "Oui, sur l'ensemble du département, après vérification de l'installation existante. "
   "Le diagnostic et le devis sont gratuits, et nous vous dirons franchement si des "
   "travaux préalables sont nécessaires."),
 ],
},

]
