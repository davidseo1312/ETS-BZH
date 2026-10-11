# -*- coding: utf-8 -*-
"""Contenu des pages d'atterrissage Google Ads — électricité.

Ces pages sont **hors du site** : aucun lien ne pointe vers elles depuis les
pages publiques, elles sont absentes du sitemap et portent « noindex ». Elles
ne reçoivent que du trafic payant, et elles portent un numéro distinct
(ADS_TEL) pour que les appels issus des annonces soient mesurables sans
dépendre du suivi d'appel de la régie.

Tout ce qui est propre à un département — contexte, communes, délais — vit
ici. La mise en page est dans build.py (page_ads).
"""

# Horaires réels de la ligne Ads. Ils remplacent le « 24h/24 · 7j/7 » qui
# figurait partout : une amplitude qu'on ne tient pas est une promesse qui se
# retourne au premier appel du dimanche. Une seule source, substituée dans
# tous les blocs ({horaires} / {horaires_court}).
HORAIRES = "du lundi au samedi, de 7h à 22h"
HORAIRES_COURT = "Lun.–sam. · 7h–22h"

ADS_TEL = "06 20 06 01 96"
ADS_TEL_LIEN = "+33620060196"

# Six motifs d'appel, communs aux quatre pages : ce sont des descriptions de
# prestation, pas du contenu local. La différenciation entre pages se fait par
# le contexte départemental et le bloc commune par commune.
URGENCES = [
    ("Panne totale ou partielle",
     "Plus de courant dans tout le logement ou dans une seule pièce. On "
     "localise le défaut circuit par circuit et on rétablit ce qui peut l'être "
     "dès le premier passage."),
    ("Disjoncteur qui saute sans arrêt",
     "Il se réarme puis retombe&nbsp;: il détecte un défaut réel. On trouve "
     "lequel, plutôt que de le forcer — un disjoncteur qu'on contourne ne "
     "protège plus personne."),
    ("Odeur de brûlé, prise qui chauffe",
     "C'est la seule situation où nous demandons de couper avant même notre "
     "arrivée. Échauffement de connexion, départ de feu possible&nbsp;: "
     "intervention prioritaire."),
    ("Tableau électrique hors service",
     "Différentiel qui ne tient plus, tableau à fusibles en bout de course, "
     "protection qui a fondu. Mise en sécurité d'abord, devis ensuite."),
    ("Après dégât des eaux, orage ou tempête",
     "Installation mouillée ou foudroyée&nbsp;: on contrôle l'isolement avant "
     "toute remise sous tension, et on remet en service ce qui est sain."),
    ("Chauffe-eau, chauffage, plaque qui ne répond plus",
     "Appareil de forte puissance en panne. On distingue le problème "
     "d'alimentation du problème d'appareil — ce n'est pas le même dépannage."),
]

# Le technicien mis en avant sur les pages payantes. Un prénom et un visage
# lèvent plus d'objections qu'un argument de plus : le visiteur d'une annonce
# ne connaît pas l'entreprise, et il hésite à composer un numéro inconnu.
#
# ATTENTION — ce bloc affirme des faits sur l'entreprise : l'existence du
# technicien nommé et la transmission familiale. Sur une page publicitaire,
# une affirmation inexacte relève de la pratique commerciale trompeuse
# (art. L121-2 du Code de la consommation) et expose au refus en régie.
# À ne publier que si c'est exact.
TECHNICIEN = {
    "prenom": "Julien",
    "role": "Électricien — ETS-BZH",
    "sceau": "De père en fils",
    # L'accroche du bandeau de titre. {lieu} et {tel} sont substitués.
    #
    # ATTENTION — « sur place sous 2 h » est un délai ferme, répété sur 172
    # pages et lu comme un engagement à chaque appel. Il a été demandé
    # explicitement, sur le modèle d'une page concurrente. La première
    # réponse de la FAQ a été réécrite pour ne pas le contredire. S'il n'est
    # pas tenable partout — le Centre Bretagne n'est pas Quimper —, c'est ici
    # qu'on le retire, et dans FAQ[0].
    "hero_eyebrow": "Électricien {lieu} · du lundi au samedi, 7h–22h",
    "hero_titre": "Urgence électricité {au_lieu}&nbsp;? "
                  "<strong>Julien sur place sous 2&nbsp;h</strong>, "
                  "du lundi au samedi.",
    "hero_texte": "Électricien de père en fils, Julien intervient vite&nbsp;: "
                  "panne de courant, disjoncteur qui saute, odeur de brûlé au "
                  "tableau. Le prix est annoncé avant les travaux, toujours.",
    "hero_bouton": "Appeler Julien",
    "hero_second": "ou être rappelé",
    # La ligne qui suit le bouton : elle répond aux deux craintes qui
    # retiennent un doigt au-dessus du numéro — tomber sur une plateforme,
    # et payer l'appel.
    "hero_rassurance": "Julien décroche lui-même, appel non surtaxé. "
                       "Devis gratuit et sans engagement.",

    # Le rappel du bas de page. Il nomme l'électricien et la commune : à ce
    # stade le visiteur a tout lu, c'est la dernière occasion de lui dire
    # qu'il appelle quelqu'un, pas une plateforme. Pas de « maintenant » —
    # les horaires sont lundi-samedi, 7h-22h.
    "final_titre": "Julien peut vous dépanner en urgence {au_lieu}",
    "final_texte": "Décrivez-lui la situation en deux minutes&nbsp;: il vous "
                   "annonce le créneau et le tarif avant que vous "
                   "raccrochiez.",

    "titre": "Julien, c'est lui qui décroche",
    "badge": "Votre électricien",
    "accroche": "Quand vous appelez le {tel}, vous n'avez ni standard, ni "
                "centre d'appels, ni formulaire à remplir&nbsp;: "
                "<strong>vous avez Julien, l'électricien qui viendra</strong>.",
    "paras": [
        "C'est la différence que personne ne voit avant d'appeler, et que "
        "tout le monde constate ensuite&nbsp;: la personne au bout du fil est "
        "celle qui montera dans le véhicule. Elle sait déjà ce qu'elle va "
        "trouver, parce qu'elle vous a écouté.",
        "Il vous demande ce qui se passe, ce que vous voyez au tableau, ce qui "
        "fonctionne encore. En deux minutes, il sait s'il faut venir tout de "
        "suite, si vous pouvez attendre demain, ou si le problème se règle au "
        "téléphone — et dans ce dernier cas, il vous le dit.",
        "<strong>Le métier s'est transmis de père en fils.</strong> On ne "
        "travaille pas de la même façon quand on a appris sur les chantiers de "
        "son père, dans les mêmes communes, auprès des mêmes clients. Un "
        "devis clair avant d'intervenir, un prix annoncé avant de se "
        "déplacer, et un travail qu'on assume parce qu'on recroisera les gens.",
    ],
}

# Trois avis supplémentaires, propres aux pages Ads : les trois premiers
# viennent de la page métier Électricité (ACTIVITES, data.py), ceux-ci
# n'apparaissent nulle part ailleurs. Six témoignages remplissent deux
# rangées de trois sans trou.
#
# Le dernier porte QUATRE étoiles et un reproche léger. Ce n'est pas une
# maladresse : six avis à cinq étoiles d'affilée se lisent comme un décor, et
# ils contredisent la moyenne de 4,8/5 affichée juste en dessous. Un bémol
# assumé fait plus pour la crédibilité que la perfection.
#
# ATTENTION — comme les trois autres, ce sont des contenus d'exemple. Les
# publier tels quels sur une page payante relève de la pratique commerciale
# trompeuse (art. L121-2, qui vise expressément les avis fictifs) et du motif
# de refus en régie. À remplacer par de vrais avis vérifiés.
AVIS_SUP = [
    ("Prise qui chauffait et odeur de brûlé un vendredi soir. Technicien sur "
     "place en moins de deux heures, circuit coupé et connexion refaite. Il a "
     "pris le temps de vérifier le reste du tableau avant de repartir.",
     "Nathalie P.", 5),
    ("Après la tempête, plus rien ne fonctionnait au rez-de-chaussée. Contrôle "
     "complet avant de remettre le courant, pièce par pièce. Rassurant de voir "
     "quelqu'un qui ne se précipite pas.",
     "Hervé L.", 5),
    ("Deux logements que je loue, intervention sur les deux. Travail sérieux "
     "et compte rendu écrit à chaque fois, ce qui m'arrange pour mes dossiers. "
     "Seul bémol&nbsp;: j'ai dû relancer pour recevoir la facture.",
     "Sylvie M.", 4),
]

# Le premier avis de la page métier Électricité raconte une intervention
# « un dimanche » : sur ces pages-ci, qui annoncent lundi-samedi, il se
# contredirait tout seul. Il est donc retouché ici, et ici seulement — la
# page publique garde le sien. (Contenu d'exemple dans les deux cas.)
AVIS_REECRITS = {
    "Panne totale un dimanche, électricien sur place en une heure. Défaut "
    "trouvé sur un circuit de la cuisine, remis en service le soir même. "
    "Très rassurant.":
    "Panne totale un samedi matin, électricien sur place en une heure. Défaut "
    "trouvé sur un circuit de la cuisine, remis en service dans la journée. "
    "Très rassurant.",
}

ETAPES = [
    ("Vous appelez, Julien décroche",
     "Pas un standard, pas un centre d'appels&nbsp;: l'électricien lui-même. "
     "Il vous demande ce qui se passe et ce que vous voyez."),
    ("On vous annonce un délai et un prix",
     "Avant de raccrocher. Pas de déplacement surprise, pas de tarif "
     "découvert sur le pas de la porte."),
    ("On intervient et on sécurise",
     "Mise en sécurité immédiate, puis réparation. Vous validez le devis "
     "avant tout travail qui dépasse le dépannage."),
]

# Aucun prix n'est affiché sur ces pages : le tarif se donne au téléphone,
# une fois la situation connue. Un chiffre posé sur une page payante est lu
# comme un engagement, et il se retourne contre nous dès que l'intervention
# est plus lourde que prévu. Ce bloc le remplace : il tient la promesse de
# transparence — ce qui convertit — sans avancer de montant.
ENGAGEMENTS = [
    ("Le prix avant le déplacement",
     "Vous connaissez le tarif applicable avant que nous prenions la route. "
     "Rien ne se découvre sur le pas de la porte."),
    ("Devis gratuit et sans engagement",
     "Le devis ne vous coûte rien et ne vous oblige à rien. Vous pouvez dire "
     "non après l'avoir lu."),
    ("Aucun travail sans votre accord",
     "Au-delà du dépannage, rien n'est engagé tant que vous n'avez pas "
     "validé. Pas de supplément décidé sans vous."),
    ("La majoration annoncée, jamais subie",
     "Soirée, samedi&nbsp;: la majoration éventuelle vous est dite au "
     "téléphone, pas découverte sur la facture."),
    ("Si on ne peut rien faire, on le dit",
     "Nous ne facturons pas une réparation inutile. Quand le problème relève "
     "d'un autre métier ou du réseau public, nous vous l'indiquons."),
    ("Un compte rendu écrit",
     "Ce qui a été constaté, ce qui a été fait, ce qui reste à faire. "
     "Exploitable pour une assurance, un bailleur ou un syndic."),
]

# FAQ : l'étape où se gagne ou se perd l'appel. Un visiteur venu d'une
# annonce n'a aucune raison de faire confiance ; chaque question lève une
# objection précise, dans l'ordre où elle se pose — d'abord le délai, puis le
# prix, puis le risque, puis le passage à l'acte.
#
# Trois règles de rédaction :
#   · aucun montant (voir ENGAGEMENTS) ;
#   · on répond vraiment, y compris quand la réponse n'arrange pas — « oui,
#     le diagnostic est facturé s'il n'est suivi de rien » rassure davantage
#     qu'un « c'est gratuit » que personne ne croit ;
#   · {nom} et {art} sont remplacés par le département de la page.
#
# La première est ouverte par défaut : sur mobile, un accordéon entièrement
# fermé se lit comme une page vide.
FAQ = [
    ("Sous combien de temps pouvez-vous être là&nbsp;?",
     "Nous visons <strong>une intervention sous deux heures</strong>, et le "
     "créneau exact vous est confirmé au téléphone, en fonction de votre "
     "adresse et de l'heure qu'il est&nbsp;: une commune de l'intérieur n'est "
     "pas le centre-ville. Nous préférons un délai tenu à une promesse "
     "large — si nous ne pouvons pas être là dans ce délai, nous le disons "
     "tout de suite plutôt que de vous faire attendre pour rien. En urgence "
     "avérée — odeur de brûlé, installation mouillée, logement sans courant "
     "avec une personne âgée ou un nourrisson — vous passez en priorité."),

    ("Combien ça va me coûter&nbsp;?",
     "Le prix dépend de ce qu'il y a à faire, et personne ne peut le deviner "
     "avant de savoir. Ce que nous garantissons, c'est que vous le connaîtrez "
     "<strong>avant que nous prenions la route</strong>, et non sur le pas de "
     "la porte. Décrivez-nous la situation au téléphone&nbsp;: nous vous "
     "annonçons le tarif applicable, la majoration éventuelle, et vous "
     "décidez à ce moment-là. Au-delà du dépannage, rien n'est engagé sans un "
     "devis que vous avez validé."),

    ("Le déplacement est-il payant&nbsp;?",
     "Soyons clairs plutôt qu'agréables&nbsp;: le diagnostic est facturé s'il "
     "n'est suivi d'aucune intervention. Dès que nous réparons, il est "
     "intégré. Le montant vous est annoncé avant notre départ, jamais "
     "découvert à l'arrivée. Et si le problème ne relève pas de nous — une "
     "coupure sur le réseau public, par exemple — nous vous le disons au "
     "téléphone et nous ne nous déplaçons pas."),

    ("Quels sont vos horaires&nbsp;? Intervenez-vous le soir et le samedi&nbsp;?",
     "Nous intervenons <strong>du lundi au samedi, de 7h à 22h</strong>, "
     "samedi compris et jusqu'à 22h en semaine. C'est une amplitude large, "
     "faite pour les pannes qui arrivent après le travail ou le week-end, "
     "mais ce n'est pas du 24h/24&nbsp;: nous préférons annoncer des horaires "
     "que nous tenons plutôt qu'une astreinte permanente que personne "
     "n'assure vraiment. En dehors de ces heures, laissez un message ou "
     "remplissez le formulaire&nbsp;: vous êtes rappelé à la première heure. "
     "La majoration applicable aux soirées et au samedi vous est annoncée au "
     "téléphone, avant le déplacement. <strong>Si le danger est "
     "immédiat</strong> — fumée, départ de feu, personne en contact avec "
     "l'installation —, c'est le 18 ou le 112 qu'il faut appeler, pas un "
     "électricien."),

    ("Êtes-vous assurés&nbsp;?",
     "Oui&nbsp;: responsabilité civile professionnelle et garantie décennale "
     "pour les travaux qui l'exigent. Vous pouvez demander les attestations "
     "avant l'intervention, nous les transmettons sans discuter. C'est la "
     "question qu'il faut poser à tout artisan qui se présente chez vous, et "
     "un professionnel sérieux n'est jamais gêné d'y répondre."),

    ("Intervenez-vous vraiment dans ma commune&nbsp;?",
     "Nous couvrons l'intégralité du département{deptnum}, communes rurales "
     "comprises — pas seulement les grandes villes. Le bloc plus haut détaille "
     "une quarantaine de communes, mais la liste n'est pas limitative. "
     "Appelez-nous&nbsp;: "
     "nous vous annonçons le délai réel chez vous, qui n'est évidemment pas le "
     "même partout."),

    ("Que dois-je faire en attendant votre arrivée&nbsp;?",
     "<strong>Odeur de brûlé, prise ou interrupteur qui chauffe&nbsp;:</strong> "
     "coupez ce circuit au tableau et n'y touchez plus — c'est la seule "
     "situation où il faut agir avant notre arrivée. "
     "<strong>Disjoncteur qui retombe&nbsp;:</strong> ne le réarmez pas en "
     "boucle, il protège quelque chose&nbsp;; débranchez plutôt les appareils "
     "un par un. <strong>Installation mouillée&nbsp;:</strong> ne remettez "
     "rien sous tension, même si tout semble sec. Et dans tous les cas, "
     "n'ouvrez aucun capot plombé&nbsp;: la partie amont reste sous tension "
     "disjoncteur abaissé."),

    ("Et si vous ne pouvez pas tout réparer aujourd'hui&nbsp;?",
     "Nous remettons d'abord l'installation en sécurité et nous rétablissons "
     "ce qui peut l'être — il est rare qu'on reparte en laissant un logement "
     "entièrement sans courant. S'il faut une pièce ou un second passage, nous "
     "le disons sur place, avec un devis et une date. Nous ne facturons pas "
     "une réparation inutile pour justifier le déplacement."),

    ("Puis-je avoir un devis avant de m'engager&nbsp;?",
     "Oui, gratuit et sans engagement. En urgence, nous mettons d'abord en "
     "sécurité — cela ne se discute pas quand il y a un risque — puis nous "
     "chiffrons la suite avant de l'engager. Pour un chantier programmé, le "
     "devis est établi après un relevé sur place, poste par poste, pour que "
     "vous puissiez le comparer."),

    ("Vous intervenez pour les professionnels, les bailleurs et les syndics&nbsp;?",
     "Oui&nbsp;: commerces, locaux professionnels, parc locatif et parties "
     "communes de copropriété. Nous fournissons un devis avant travaux, une "
     "facturation au gestionnaire quand c'est convenu, et un compte rendu "
     "écrit avec photos — exploitable pour un dossier d'assurance, un locataire "
     "ou une assemblée générale."),
]

# Les garanties, en tête de page. Chaque ligne lève une objection précise et
# se vérifie : rien qui tienne de la formule.
#
# ATTENTION — deux affirmations engagent l'entreprise et doivent être
# confirmées avant mise en ligne : la décennale auprès de MIC Insurance (le
# numéro de contrat est encore « à compléter » dans les mentions légales) et
# les moyens de paiement acceptés.
GARANTIES = [
    ("C'est lui qui décroche",
     "quand vous appelez le {tel}. Pas de standard, pas de centre d'appels."),
    ("Du lundi au samedi, 7h–22h",
     "soirées et samedi compris. Le créneau vous est annoncé à l'appel."),
    ("Prix annoncé avant les travaux.",
     "Rien n'est engagé sans votre accord."),
    ("Assuré en décennale",
     "auprès de MIC Insurance. Attestation transmise sur demande."),
    ("Le camion part équipé&nbsp;:",
     "testeur d'isolement, pince ampèremétrique, caméra thermique, matériel "
     "de consignation."),
    ("Paiement",
     "par carte bancaire, virement ou espèces."),
]

# Les quatre chiffres du bandeau. « 4,8/5 » est la moyenne réelle des six avis
# affichés plus bas (5+5+5+5+5+4 sur 6 = 4,83) : c'est pour cela qu'il est
# présenté comme « moyenne des avis publiés ici » et non attribué à une
# plateforme tierce, ce qui serait invérifiable.
CHIFFRES = [
    ("7h–22h", "du lundi au samedi"),
    ("4,8/5", "moyenne des avis publiés ici"),
    ("Père en fils", "artisan électricien"),
    ("Prix annoncé", "avant les travaux"),
]

# Codes postaux des communes citées. Ils servent au bloc « Zones
# d'intervention » : un nom de commune suivi de son code postal lève le doute
# sur les homonymes et fait local là où une simple liste fait remplissage.
# À faire vérifier par le client avant mise en ligne — un code postal faux est
# une petite erreur qui coûte cher en crédibilité.
CP = {
    "Saint-Brieuc": "22000", "Lannion": "22300", "Dinan": "22100",
    "Guingamp": "22200", "Lamballe-Armor": "22400", "Plérin": "22190",
    "Ploufragan": "22440", "Paimpol": "22500", "Trégueux": "22950",
    "Loudéac": "22600", "Perros-Guirec": "22700", "Saint-Quay-Portrieux": "22410",

    "Brest": "29200", "Quimper": "29000", "Concarneau": "29900",
    "Morlaix": "29600", "Douarnenez": "29100", "Landerneau": "29800",
    "Quimperlé": "29300", "Plougastel-Daoulas": "29470", "Guipavas": "29490",
    "Le Relecq-Kerhuon": "29480", "Crozon": "29160", "Carhaix-Plouguer": "29270",

    "Rennes": "35000", "Saint-Malo": "35400", "Fougères": "35300",
    "Vitré": "35500", "Cesson-Sévigné": "35510", "Bruz": "35170",
    "Redon": "35600", "Dinard": "35800", "Betton": "35830",
    "Chantepie": "35135", "Saint-Grégoire": "35760",
    "Saint-Jacques-de-la-Lande": "35136",

    "Vannes": "56000", "Lorient": "56100", "Lanester": "56600",
    "Pontivy": "56300", "Ploemeur": "56270", "Hennebont": "56700",
    "Auray": "56400", "Guidel": "56520", "Quiberon": "56170",
    "Séné": "56860", "Saint-Avé": "56890", "Sarzeau": "56370",
}

# Les trois familles d'intervention, numérotées comme sur une fiche métier.
# (titre, photo, [points])
SERVICES = [
    ("Dépannage et recherche de panne", "electricite-3.jpg", [
        "Panne totale ou partielle, localisée circuit par circuit.",
        "Disjoncteur qui saute&nbsp;: on trouve le défaut, on ne le contourne pas.",
        "Remise en service dès le premier passage chaque fois que c'est possible.",
    ]),
    ("Mise en sécurité et tableau électrique", "electricite-1.jpg", [
        "Odeur de brûlé, prise qui chauffe&nbsp;: coupure et reprise de la connexion.",
        "Remplacement de tableau, pose d'un différentiel 30&nbsp;mA.",
        "Contrôle de la prise de terre et mesure d'isolement.",
    ]),
    ("Installation et mise aux normes", "electricite-2.jpg", [
        "Création de circuits dédiés&nbsp;: cuisine, chauffe-eau, forte puissance.",
        "Reprise d'installation ancienne, repérage et étiquetage des circuits.",
        "Remise en service après dégât des eaux, orage ou tempête.",
    ]),
]

DEPTS = {
 "22": {
  "contexte":
    "Les Côtes-d'Armor cumulent deux parcs très différents&nbsp;: les "
    "agglomérations de Saint-Brieuc et Lannion, où nous intervenons surtout "
    "sur des tableaux saturés et des circuits surchargés, et un arrière-pays "
    "rural où les installations d'origine — tableaux à fusibles, absence de "
    "différentiel 30&nbsp;mA, terre défaillante — sont encore nombreuses. "
    "S'y ajoute l'exposition de la côte&nbsp;: après chaque coup de vent, les "
    "appels de coupure et de surtension arrivent par vagues.",
  "villes": [
    ("Saint-Brieuc", "Intervention rapide sur toute l'agglomération, du matin à la soirée."),
    ("Lannion", "Secteur couvert six jours sur sept, zone technologique comprise."),
    ("Dinan", "Bâti ancien&nbsp;: circuits sans terre et tableaux d'origine, fréquents."),
    ("Guingamp", "Logements de centre-ville et parc locatif, interventions courantes."),
    ("Lamballe-Armor", "Pavillonnaire et commerces, dépannage sous quelques heures."),
    ("Plérin", "Proche Saint-Brieuc&nbsp;: l'un de nos délais les plus courts."),
    ("Ploufragan", "Zone d'activité et résidentiel, interventions en journée et en soirée."),
    ("Paimpol", "Littoral&nbsp;: corrosion des coffrets extérieurs et pannes après tempête."),
    ("Trégueux", "Secteur limitrophe de Saint-Brieuc, couvert en priorité."),
    ("Loudéac", "Centre du département&nbsp;: habitat spacieux, puissance souvent juste."),
    ("Perros-Guirec", "Résidences secondaires&nbsp;: remises en service et pannes d'hivernage."),
    ("Saint-Quay-Portrieux", "Bord de mer&nbsp;: installations extérieures et différentiels qui sautent."),
  ],
 },
 "29": {
  "contexte":
    "Le Finistère est le département où nous recevons le plus d'appels liés "
    "à la météo&nbsp;: surtensions après orage, installations mouillées après "
    "une tempête, coupures en série sur la côte. L'autre moitié de notre "
    "activité tient au bâti&nbsp;: les centres anciens de Brest, Quimper et "
    "Morlaix comptent beaucoup d'installations posées par strates "
    "successives, sans repérage et souvent sans terre sur une partie des "
    "circuits.",
  "villes": [
    ("Brest", "Couverture de toute la métropole, du lundi au samedi."),
    ("Quimper", "Centre ancien et périphérie&nbsp;: interventions quotidiennes."),
    ("Concarneau", "Littoral&nbsp;: coffrets corrodés et circuits extérieurs défaillants."),
    ("Morlaix", "Maisons hautes de centre-ville, installations anciennes par strates."),
    ("Douarnenez", "Bâti ancien en pierre&nbsp;: absence de terre sur une partie des prises."),
    ("Landerneau", "Pavillonnaire des années 1980, tableaux d'origine en fin de vie."),
    ("Quimperlé", "Secteur couvert en journée et en soirée, délai annoncé à l'appel."),
    ("Plougastel-Daoulas", "Habitat dispersé&nbsp;: liaisons enterrées vers dépendances."),
    ("Guipavas", "Proche Brest&nbsp;: l'un de nos délais les plus courts du département."),
    ("Le Relecq-Kerhuon", "Résidentiel dense, interventions rapides en semaine comme le samedi."),
    ("Crozon", "Presqu'île&nbsp;: résidences secondaires et remises en service saisonnières."),
    ("Carhaix-Plouguer", "Centre Bretagne&nbsp;: installations rurales et puissance insuffisante."),
  ],
 },
 "35": {
  "contexte":
    "L'Ille-et-Vilaine est le département du collectif et du locatif. Une "
    "grande partie de nos appels vient d'appartements, de petites surfaces "
    "louées et de parties communes&nbsp;: cages d'escalier éteintes, "
    "différentiels qui ne tiennent plus en cave, tableaux de palier sans "
    "repérage. Nous travaillons autant pour des particuliers que pour des "
    "bailleurs, des agences de gestion et des syndics, avec un compte rendu "
    "écrit à chaque passage.",
  "villes": [
    ("Rennes", "Le plus gros volume d'interventions&nbsp;: toute la ville, six jours sur sept."),
    ("Saint-Malo", "Bâti ancien et meublés&nbsp;: circuits sans terre et parc locatif."),
    ("Fougères", "Centre ancien&nbsp;: colonnes montantes vétustes et tableaux à fusibles."),
    ("Vitré", "Résidences et parkings couverts&nbsp;: éclairage de sécurité et parties communes."),
    ("Cesson-Sévigné", "Résidences récentes, interventions rapides en semaine et le samedi."),
    ("Bruz", "Colocations et logements étudiants&nbsp;: circuits surchargés, disjonctions."),
    ("Redon", "Rez-de-chaussée humides&nbsp;: liaison équipotentielle et terre à reprendre."),
    ("Dinard", "Bord de mer&nbsp;: corrosion des coffrets et des commandes extérieures."),
    ("Betton", "Secteur résidentiel proche Rennes, délai court annoncé à l'appel."),
    ("Chantepie", "Collectifs et pavillonnaire mêlés, dépannage sous quelques heures."),
    ("Saint-Grégoire", "Logements récents&nbsp;: ajout de circuits et différentiels fatigués."),
    ("Saint-Jacques-de-la-Lande", "Résidences neuves parfois sous garantie&nbsp;: constat écrit systématique."),
  ],
 },
 "56": {
  "contexte":
    "Dans le Morbihan, deux réalités se superposent. Sur le littoral — "
    "Quiberon, Rhuys, Belle-Île, Guidel — l'air marin dégrade tout ce qui est "
    "extérieur&nbsp;: coffrets, hublots, commandes de portail, boîtes de "
    "dérivation. Les différentiels finissent par ne plus tenir, souvent au "
    "retour d'une absence. À l'intérieur, autour de Pontivy et Locminé, ce "
    "sont les installations rurales anciennes et les manques de puissance qui "
    "dominent.",
  "villes": [
    ("Vannes", "Couverture de toute l'agglomération, du lundi au samedi."),
    ("Lorient", "Zone urbaine dense&nbsp;: colonnes anciennes et parties communes."),
    ("Lanester", "Proche estuaire&nbsp;: corrosion des appareillages extérieurs."),
    ("Pontivy", "Centre Bretagne&nbsp;: installations rurales et tableaux d'origine."),
    ("Ploemeur", "Bord de mer&nbsp;: circuits extérieurs et liaisons vers dépendances."),
    ("Hennebont", "Secteur couvert en priorité, délai annoncé dès l'appel."),
    ("Auray", "Centre ancien&nbsp;: installations par strates, repérage absent."),
    ("Guidel", "Littoral exposé&nbsp;: différentiels qui sautent après la pluie."),
    ("Quiberon", "Presqu'île&nbsp;: forte saisonnalité, intervention en journée et en soirée."),
    ("Séné", "Fond de golfe&nbsp;: humidité et défauts d'isolement récurrents."),
    ("Saint-Avé", "Pavillonnaire récent&nbsp;: ajout de circuits et éclairage extérieur."),
    ("Sarzeau", "Presqu'île de Rhuys&nbsp;: résidences secondaires et remises en service."),
  ],
 },
}


# ---------------------------------------------------------------------------
# Trente communes de plus par département — quarante-deux en tout.
#
# Elles sont déclarées ici, et non dans les listes ci-dessus, pour garder
# lisible le noyau des douze communes principales : ce sont elles qui portent
# les avis clients et qui sont citées dans la FAQ. Les trente autres étendent
# la couverture et reçoivent chacune leur propre page, au même titre.
#
# La note locale sert deux fois : ligne du bloc « Zones d'intervention » sur
# la page départementale, et paragraphe d'accroche de la page de la commune.
# Elle doit donc dire quelque chose du parc local — sur quarante-deux lignes
# qui se suivent, un remplissage se voit tout de suite.
#
# Codes postaux : à faire vérifier par le client, comme ceux du dessus.
COMMUNES_SUP = {
 "22": [
  ('Langueux', '22360',
   'Zone commerciale et lotissements récents&nbsp;: ajouts de circuits et tableaux saturés.'),
  ('Pordic', '22590',
   'Bourg étendu vers la côte&nbsp;: liaisons enterrées et coffrets de jardin.'),
  ('Hillion', '22120',
   'Baie exposée&nbsp;: humidité saline dans les boîtes de dérivation extérieures.'),
  ('Yffiniac', '22120',
   "Fond de baie&nbsp;: défauts d'isolement après les grandes marées et les orages."),
  ('Plédran', '22960',
   "Pavillonnaire des années 1980, tableaux d'origine arrivés en fin de vie."),
  ('Quintin', '22800',
   'Petite cité de caractère&nbsp;: bâti ancien, circuits repris sans repérage.'),
  ('Binic-Étables-sur-Mer', '22520',
   'Port et maisons de bord de mer&nbsp;: prises extérieures et éclairage de terrasse.'),
  ('Pléneuf-Val-André', '22370',
   'Forte saisonnalité&nbsp;: remises en service de printemps et différentiels fatigués.'),
  ('Erquy', '22430',
   'Station balnéaire&nbsp;: coffrets de camping-car, douches extérieures, hublots corrodés.'),
  ('Saint-Cast-le-Guildo', '22380',
   "Résidences fermées l'hiver&nbsp;: pannes découvertes à la réouverture."),
  ('Matignon', '22550',
   'Bourg rural du Penthièvre&nbsp;: tableaux à fusibles encore en service.'),
  ('Plancoët', '22130',
   'Habitat de vallée&nbsp;: terre insuffisante et liaison équipotentielle absente.'),
  ('Jugon-les-Lacs', '22270',
   'Maisons anciennes en pierre&nbsp;: pas de terre sur une partie des prises.'),
  ('Plouha', '22580',
   'Falaises et vent&nbsp;: antennes, paratonnerres et surtensions après orage.'),
  ('Tréguier', '22220',
   'Centre historique protégé&nbsp;: passage de câbles contraint, gaines à reprendre.'),
  ('Lézardrieux', '22740',
   'Estuaire du Trieux&nbsp;: coffrets de port et corrosion rapide.'),
  ('Pleubian', '22610',
   "Presqu'île Sauvage&nbsp;: habitat dispersé et alimentations de dépendances."),
  ('Louannec', '22700',
   'Proche Perros-Guirec&nbsp;: locations saisonnières et compteurs sollicités.'),
  ('Pleumeur-Bodou', '22560',
   'Pavillonnaire et gîtes&nbsp;: ajout de circuits et bornes de recharge.'),
  ('Trébeurden', '22560',
   'Côte de granit rose&nbsp;: éclairage extérieur et commandes de portail.'),
  ('Trégastel', '22730',
   'Résidences de front de mer&nbsp;: embruns dans les appareillages extérieurs.'),
  ('Plestin-les-Grèves', '22310',
   'Grèves exposées&nbsp;: reprises après inondation, remise sous tension prudente.'),
  ('Plouaret', '22420',
   'Intérieur du Trégor&nbsp;: installations rurales et puissance souvent juste.'),
  ('Bégard', '22140',
   'Habitat ancien et exploitations&nbsp;: armoires de bâtiment agricole.'),
  ('Belle-Isle-en-Terre', '22810',
   'Vallées encaissées&nbsp;: alimentations longues et chutes de tension.'),
  ('Callac', '22160',
   "Centre Bretagne&nbsp;: logements chauffés à l'électrique, circuits surchargés."),
  ('Rostrenen', '22110',
   "Bourg rural&nbsp;: tableaux d'origine, différentiel 30&nbsp;mA souvent absent."),
  ('Guerlédan', '22530',
   'Autour du lac&nbsp;: gîtes, dépendances et coffrets extérieurs.'),
  ('Merdrignac', '22230',
   'Habitat spacieux et dépendances&nbsp;: puissance mal répartie.'),
  ('Broons', '22250',
   'Carrefour routier&nbsp;: commerces et locaux professionnels à mettre aux normes.'),
 ],
 "29": [
  ('Plouzané', '29280',
   'Plateau du Léon&nbsp;: lotissements des années 1970, tableaux à remplacer.'),
  ('Saint-Renan', '29290',
   'Bourg en expansion&nbsp;: extensions de maison et circuits ajoutés sans repérage.'),
  ('Gouesnou', '29850',
   "Proche zone d'activité&nbsp;: locaux professionnels et éclairage de parking."),
  ('Bohars', '29820',
   'Résidentiel calme&nbsp;: installations des années 1980 et prises sans terre.'),
  ('Plabennec', '29860',
   'Pavillonnaire et exploitations&nbsp;: armoires de hangar et manque de puissance.'),
  ('Lesneven', '29260',
   'Centre-bourg ancien&nbsp;: colonnes montantes et parties communes vétustes.'),
  ('Lannilis', '29870',
   'Pays des Abers&nbsp;: habitat dispersé, liaisons enterrées vers dépendances.'),
  ('Plouguerneau', '29880',
   'Côte très exposée&nbsp;: corrosion des coffrets et pannes après tempête.'),
  ('Ploudalmézeau', '29830',
   "Pays d'Iroise&nbsp;: résidences secondaires et remises en service saisonnières."),
  ('Landivisiau', '29400',
   'Bourg agricole&nbsp;: forte puissance, armoires et moteurs triphasés.'),
  ('Saint-Pol-de-Léon', '29250',
   "Bâti ancien en pierre&nbsp;: humidité des murs et défauts d'isolement."),
  ('Roscoff', '29680',
   'Port et hôtellerie&nbsp;: embruns permanents sur les appareillages extérieurs.'),
  ('Plouescat', '29430',
   'Front de mer&nbsp;: différentiels qui sautent après les coups de vent.'),
  ('Plouigneau', '29610',
   'Pays de Morlaix&nbsp;: habitat rural et tableaux à fusibles encore en place.'),
  ('Châteaulin', '29150',
   "Vallée de l'Aulne&nbsp;: rez-de-chaussée humides et terre à reprendre."),
  ('Pleyben', '29190',
   'Bourg rural&nbsp;: chauffage électrique ancien et circuits surchargés.'),
  ('Le Faou', '29590',
   'Fond de rade&nbsp;: maisons anciennes et installations posées par strates.'),
  ('Daoulas', '29460',
   'Habitat ancien de bourg&nbsp;: pas de terre sur une partie des prises.'),
  ("Pont-l'Abbé", '29120',
   'Pays bigouden&nbsp;: parc locatif et petites surfaces à remettre aux normes.'),
  ('Penmarch', '29760',
   'Pointe exposée&nbsp;: sel et vent, boîtiers extérieurs à remplacer souvent.'),
  ('Loctudy', '29750',
   "Port de plaisance&nbsp;: coffrets de quai et résidences fermées l'hiver."),
  ('Plonéour-Lanvern', '29720',
   'Bourg bigouden&nbsp;: maisons des années 1970 et puissance insuffisante.'),
  ('Audierne', '29770',
   'Cap Sizun&nbsp;: habitat ancien en bord de mer, corrosion et humidité.'),
  ('Fouesnant', '29170',
   'Forte saisonnalité&nbsp;: campings, locations et compteurs très sollicités.'),
  ('Bénodet', '29950',
   'Station balnéaire&nbsp;: éclairage extérieur, piscines et locaux techniques.'),
  ('Pluguffan', '29700',
   "Proche Quimper&nbsp;: l'un de nos délais les plus courts en Cornouaille."),
  ('Ergué-Gabéric', '29500',
   'Périphérie de Quimper&nbsp;: pavillonnaire étendu et bornes de recharge.'),
  ('Briec', '29510',
   'Bourg et campagne&nbsp;: longues alimentations et chutes de tension.'),
  ('Rosporden', '29140',
   'Étangs et habitat ancien&nbsp;: liaison équipotentielle et terre défaillantes.'),
  ('Moëlan-sur-Mer', '29350',
   'Littoral du pays de Quimperlé&nbsp;: rias, mouillages, installations extérieures.'),
 ],
 "35": [
  ('Pacé', '35740',
   'Commune en forte croissance&nbsp;: logements neufs et ajouts de circuits.'),
  ('Thorigné-Fouillard', '35235',
   'Résidentiel récent&nbsp;: différentiels fatigués et bornes de recharge.'),
  ('Chartres-de-Bretagne', '35131',
   'Industriel et résidentiel mêlés&nbsp;: locaux pro et parties communes.'),
  ('Noyal-Châtillon-sur-Seiche', '35230',
   'Lotissements successifs&nbsp;: tableaux sous-dimensionnés à reprendre.'),
  ('Vern-sur-Seiche', '35770',
   'Habitat pavillonnaire&nbsp;: extensions, vérandas et circuits extérieurs.'),
  ('Acigné', '35690',
   'Bourg résidentiel&nbsp;: installations des années 1980 en fin de vie.'),
  ('Le Rheu', '35650',
   'Collectifs et maisons mitoyennes&nbsp;: colonnes et tableaux de palier.'),
  ('Mordelles', '35310',
   'Centre ancien et lotissements&nbsp;: deux parcs, deux types de pannes.'),
  ('Montgermont', '35760',
   'Proche Rennes&nbsp;: délai court, interventions en journée et en soirée.'),
  ('Melesse', '35520',
   'Nord de Rennes&nbsp;: habitat récent parfois sous garantie, constat écrit systématique.'),
  ('Liffré', '35340',
   "Bourg forestier&nbsp;: chauffage électrique et circuits surchargés l'hiver."),
  ("Saint-Aubin-d'Aubigné", '35250',
   'Rural périurbain&nbsp;: dépendances alimentées en souterrain.'),
  ('Châteaugiron', '35410',
   'Cité médiévale&nbsp;: bâti protégé, passage de câbles contraint.'),
  ('Pont-Péan', '35131',
   'Ancien site minier&nbsp;: sols humides et prise de terre à vérifier.'),
  ('Laillé', '35890',
   'Habitat dispersé&nbsp;: longues alimentations et chutes de tension.'),
  ('Guichen', '35580',
   'Vallée de la Vilaine&nbsp;: rez-de-chaussée inondables, reprise après dégât des eaux.'),
  ('Bréal-sous-Montfort', '35310',
   'Bourg en extension&nbsp;: lotissements récents et puissance à revoir.'),
  ('Montfort-sur-Meu', '35160',
   'Centre ancien&nbsp;: installations par strates et repérage absent.'),
  ('Montauban-de-Bretagne', '35360',
   'Axe routier&nbsp;: commerces, locaux professionnels et enseignes.'),
  ('Combourg', '35270',
   'Bâti ancien en pierre&nbsp;: pas de terre sur une partie des circuits.'),
  ('Dol-de-Bretagne', '35120',
   "Pays des marais&nbsp;: humidité permanente et défauts d'isolement récurrents."),
  ('Cancale', '35260',
   'Port ostréicole&nbsp;: locaux professionnels et appareillages exposés au sel.'),
  ('Saint-Méloir-des-Ondes', '35350',
   'Campagne littorale&nbsp;: exploitations et armoires de hangar.'),
  ('Pleurtuit', '35730',
   'Proche Dinard&nbsp;: résidences secondaires et remises en service.'),
  ('Saint-Briac-sur-Mer', '35800',
   'Front de mer&nbsp;: corrosion des coffrets et commandes de portail.'),
  ('Tinténiac', '35190',
   "Canal d'Ille-et-Rance&nbsp;: habitat ancien et dépendances humides."),
  ('Hédé-Bazouges', '35630',
   "Petit bourg de caractère&nbsp;: tableaux d'origine encore en service."),
  ('Argentré-du-Plessis', '35370',
   'Pays de Vitré&nbsp;: pavillonnaire et extensions à alimenter.'),
  ('La Guerche-de-Bretagne', '35130',
   'Bourg-centre rural&nbsp;: tableaux à fusibles et terre insuffisante.'),
  ('Janzé', '35150',
   'Habitat et artisanat mêlés&nbsp;: ateliers, triphasé et mises aux normes.'),
 ],
 "56": [
  ('Caudan', '56850',
   "Zone d'activité et résidentiel&nbsp;: locaux professionnels et éclairage extérieur."),
  ('Quéven', '56530',
   'Pavillonnaire étendu&nbsp;: tableaux des années 1980 à remplacer.'),
  ('Larmor-Plage', '56260',
   'Front de mer&nbsp;: sel et vent sur les coffrets et les hublots.'),
  ('Port-Louis', '56290',
   'Citadelle et bâti ancien&nbsp;: circuits sans terre dans les murs épais.'),
  ('Riantec', '56670',
   "Petite mer de Gâvres&nbsp;: humidité et défauts d'isolement."),
  ('Ploërmel', '56800',
   'Est du département&nbsp;: bourg-centre, commerces et parc locatif.'),
  ('Plouay', '56240',
   'Intérieur du pays&nbsp;: installations rurales et puissance souvent juste.'),
  ('Inzinzac-Lochrist', '56650',
   'Vallée du Blavet&nbsp;: habitat ancien et dépendances à alimenter.'),
  ('Languidic', '56440',
   'Commune très étendue&nbsp;: longues alimentations et chutes de tension.'),
  ('Pluvigner', '56330',
   'Bourg en croissance&nbsp;: logements neufs et bornes de recharge.'),
  ("Brec'h", '56400',
   'Habitat dispersé&nbsp;: liaisons enterrées vers garages et ateliers.'),
  ('Pluneret', '56400',
   'Proche Auray&nbsp;: délai court, interventions en journée et en soirée.'),
  ("Crac'h", '56950',
   "Rivière d'Auray&nbsp;: coffrets de ponton et appareillages exposés."),
  ('Carnac', '56340',
   'Très forte saisonnalité&nbsp;: locations, campings et compteurs sollicités.'),
  ('La Trinité-sur-Mer', '56470',
   'Port de plaisance&nbsp;: bornes de quai et corrosion permanente.'),
  ('Plouharnel', '56340',
   'Dunes et vent&nbsp;: sel dans les boîtes de dérivation extérieures.'),
  ('Erdeven', '56410',
   'Résidences secondaires&nbsp;: pannes découvertes à la réouverture.'),
  ('Belz', '56550',
   "Ria d'Étel&nbsp;: humidité et différentiels qui ne tiennent plus."),
  ('Étel', '56410',
   'Port et bâti serré&nbsp;: installations par strates, repérage absent.'),
  ('Baden', '56870',
   "Golfe du Morbihan&nbsp;: maisons de bord d'eau et éclairage de jardin."),
  ('Le Bono', '56400',
   'Fond de ria&nbsp;: prise de terre à reprendre et liaison équipotentielle.'),
  ('Arradon', '56610',
   'Bord du golfe&nbsp;: résidences spacieuses, circuits dédiés et forte puissance.'),
  ('Ploeren', '56880',
   'Périphérie de Vannes&nbsp;: pavillonnaire récent et ajouts de circuits.'),
  ('Theix-Noyalo', '56450',
   'Commune étendue&nbsp;: dépendances et alimentations souterraines.'),
  ('Surzur', '56450',
   'Entre golfe et Rhuys&nbsp;: habitat récent et portails automatisés.'),
  ('Saint-Gildas-de-Rhuys', '56730',
   "Presqu'île exposée&nbsp;: corrosion rapide de tout ce qui est extérieur."),
  ('Arzon', '56640',
   'Port-Navalo&nbsp;: forte saisonnalité et remises en service de printemps.'),
  ('Elven', '56250',
   'Bourg rural&nbsp;: tableaux à fusibles encore en service.'),
  ('Questembert', '56230',
   'Centre ancien&nbsp;: colonnes montantes et parties communes.'),
  ('Muzillac', '56190',
   'Proche littoral&nbsp;: résidences secondaires et installations extérieures.'),
 ],
}

for _num, _liste in COMMUNES_SUP.items():
    DEPTS[_num]["villes"] += [(_v, _n) for _v, _cp, _n in _liste]
    CP.update({_v: _cp for _v, _cp, _n in _liste})
