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
    "titre": "Demandez Julien",
    "paras": [
        "Quand vous composez le {tel}, vous ne tombez pas sur une plateforme "
        "qui prend votre adresse et vous rappelle plus tard. <strong>C'est un "
        "électricien qui décroche</strong>, et c'est souvent Julien.",
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

ETAPES = [
    ("Vous appelez",
     "Un électricien décroche, pas un standard. Il vous demande ce qui se "
     "passe et ce que vous voyez."),
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
     "Nuit, dimanche, jour férié&nbsp;: la majoration éventuelle vous est dite "
     "au téléphone, pas découverte sur la facture."),
    ("Si on ne peut rien faire, on le dit",
     "Nous ne facturons pas une réparation inutile. Quand le problème relève "
     "d'un autre métier ou du réseau public, nous vous l'indiquons."),
    ("Un compte rendu écrit",
     "Ce qui a été constaté, ce qui a été fait, ce qui reste à faire. "
     "Exploitable pour une assurance, un bailleur ou un syndic."),
]

FAQ = [
    ("Combien de temps avant votre arrivée&nbsp;?",
     "Nous annonçons un créneau réaliste au téléphone, en fonction de votre "
     "commune et de l'heure. Nous préférons un délai tenu à une promesse "
     "large&nbsp;: si nous ne pouvons pas venir vite, nous le disons tout de "
     "suite."),
    ("Le déplacement est-il payant&nbsp;?",
     "Le diagnostic est facturé s'il n'est suivi d'aucune intervention. Dès "
     "que nous réparons, il est intégré. Le montant vous est annoncé avant "
     "notre départ, pas à l'arrivée."),
    ("Intervenez-vous la nuit et le week-end&nbsp;?",
     "Oui, 24h/24 et 7j/7, y compris les jours fériés. La majoration "
     "applicable vous est annoncée au téléphone avant que nous nous "
     "déplacions."),
    ("Vous intervenez pour les professionnels et les syndics&nbsp;?",
     "Oui&nbsp;: commerces, bailleurs, agences de gestion et copropriétés. "
     "Devis avant travaux et compte rendu écrit exploitable pour un dossier "
     "d'assurance ou une assemblée générale."),
    ("Que dois-je faire en attendant&nbsp;?",
     "En cas d'odeur de brûlé ou de prise qui chauffe&nbsp;: coupez le "
     "circuit concerné au tableau et n'y touchez plus. Sinon, ne réarmez pas "
     "en boucle un disjoncteur qui retombe — il protège quelque chose."),
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
    ("Saint-Brieuc", "Intervention rapide sur toute l'agglomération, de nuit comme de jour."),
    ("Lannion", "Secteur couvert en continu, y compris la zone technologique."),
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
    ("Brest", "Couverture continue sur toute la métropole, de jour comme de nuit."),
    ("Quimper", "Centre ancien et périphérie&nbsp;: interventions quotidiennes."),
    ("Concarneau", "Littoral&nbsp;: coffrets corrodés et circuits extérieurs défaillants."),
    ("Morlaix", "Maisons hautes de centre-ville, installations anciennes par strates."),
    ("Douarnenez", "Bâti ancien en pierre&nbsp;: absence de terre sur une partie des prises."),
    ("Landerneau", "Pavillonnaire des années 1980, tableaux d'origine en fin de vie."),
    ("Quimperlé", "Secteur couvert en journée et en soirée, délai annoncé à l'appel."),
    ("Plougastel-Daoulas", "Habitat dispersé&nbsp;: liaisons enterrées vers dépendances."),
    ("Guipavas", "Proche Brest&nbsp;: l'un de nos délais les plus courts du département."),
    ("Le Relecq-Kerhuon", "Résidentiel dense, interventions rapides en semaine comme le week-end."),
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
    ("Rennes", "Le plus gros volume d'interventions&nbsp;: couverture 24h/24 sur toute la ville."),
    ("Saint-Malo", "Bâti ancien et meublés&nbsp;: circuits sans terre et parc locatif."),
    ("Fougères", "Centre ancien&nbsp;: colonnes montantes vétustes et tableaux à fusibles."),
    ("Vitré", "Résidences et parkings couverts&nbsp;: éclairage de sécurité et parties communes."),
    ("Cesson-Sévigné", "Résidences récentes, interventions rapides en semaine et le week-end."),
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
    ("Vannes", "Couverture continue sur l'agglomération, de jour comme de nuit."),
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
