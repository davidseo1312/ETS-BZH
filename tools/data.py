# -*- coding: utf-8 -*-
"""Données éditoriales du site ETS-BZH (activités, départements, contenus SEO)."""

SITE = {
    "nom": "ETS-BZH",
    "baseline": "Plomberie · Dégorgement · Électricité · Canalisations",
    # version courte : l'en-tête sticky ne doit jamais repousser le bouton d'appel
    "baseline_courte": "Plomberie · Dégorgement · Électricité",
    "tel": "02 20 06 00 75",
    "tel_lien": "+33220060075",
    "email": "contact@ets-bzh.fr",
    "url": "https://www.ets-bzh.fr",
    "siret": "000 000 000 00000",
    "adresse": "Bretagne — interventions sur les départements 22, 29, 35 et 56",
}

# --------------------------------------------------------------------------
# Départements
# --------------------------------------------------------------------------
DEPARTEMENTS = [
    {
        "num": "22",
        "nom": "Côtes-d'Armor",
        "nom_court": "Côtes-d'Armor",
        "slug": "cotes-d-armor",
        "article": "dans les",           # « … dans les Côtes-d'Armor »
        "article_maj": "Dans les",
        "prefecture": "Saint-Brieuc",
        "gentile": "costarmoricains",
        "villes": ["Saint-Brieuc", "Lannion", "Dinan", "Guingamp", "Lamballe-Armor",
                   "Plérin", "Ploufragan", "Paimpol", "Trégueux", "Loudéac",
                   "Perros-Guirec", "Pordic", "Saint-Quay-Portrieux", "Quintin",
                   "Bégard", "Plestin-les-Grèves", "Callac", "Rostrenen"],
        "contexte": ("un habitat côtier très exposé au sel et à l'humidité, "
                     "de nombreuses longères rénovées et des réseaux d'assainissement "
                     "individuels fréquents dans l'arrière-pays"),
        "axes": "la RN12 entre Saint-Brieuc, Lamballe et Guingamp",
    },
    {
        "num": "29",
        "nom": "Finistère",
        "nom_court": "Finistère",
        "slug": "finistere",
        "article": "dans le",
        "article_maj": "Dans le",
        "prefecture": "Quimper",
        "gentile": "finistériens",
        "villes": ["Brest", "Quimper", "Concarneau", "Morlaix", "Douarnenez",
                   "Landerneau", "Quimperlé", "Plougastel-Daoulas", "Guipavas",
                   "Pont-l'Abbé", "Crozon", "Le Relecq-Kerhuon", "Plouzané",
                   "Saint-Renan", "Châteaulin", "Fouesnant", "Carhaix-Plouguer", "Bénodet"],
        "contexte": ("un parc immobilier ancien à Brest et Quimper, des résidences "
                     "secondaires nombreuses sur la côte et des canalisations "
                     "régulièrement mises à l'épreuve par les fortes pluies"),
        "axes": "la RN165 reliant Brest, Châteaulin et Quimper",
    },
    {
        "num": "35",
        "nom": "Ille-et-Vilaine",
        "nom_court": "Ille-et-Vilaine",
        "slug": "ille-et-vilaine",
        "article": "en",
        "article_maj": "En",
        "prefecture": "Rennes",
        "gentile": "bretilliens",
        "villes": ["Rennes", "Saint-Malo", "Fougères", "Vitré", "Cesson-Sévigné",
                   "Bruz", "Redon", "Dinard", "Betton", "Chantepie", "Saint-Grégoire",
                   "Combourg", "Pacé", "Châteaubourg", "Le Rheu", "Saint-Jacques-de-la-Lande",
                   "Montfort-sur-Meu", "Janzé"],
        "contexte": ("une forte densité d'appartements et de copropriétés sur Rennes "
                     "métropole, des immeubles anciens intra-rocade et un bassin "
                     "locatif qui impose des interventions rapides"),
        "axes": "la rocade rennaise et la N137 vers Saint-Malo",
    },
    {
        "num": "56",
        "nom": "Morbihan",
        "nom_court": "Morbihan",
        "slug": "morbihan",
        "article": "dans le",
        "article_maj": "Dans le",
        "prefecture": "Vannes",
        "gentile": "morbihannais",
        "villes": ["Vannes", "Lorient", "Lanester", "Pontivy", "Ploemeur",
                   "Hennebont", "Auray", "Guidel", "Quiberon", "Séné", "Saint-Avé",
                   "Sarzeau", "Pluvigner", "Caudan", "Questembert", "Baud",
                   "Le Palais", "Locminé"],
        "contexte": ("un littoral très touristique du golfe du Morbihan à Quiberon, "
                     "de nombreuses locations saisonnières et des installations "
                     "sollicitées par pics en haute saison"),
        "axes": "la RN165 entre Lorient, Auray et Vannes",
    },
]

# --------------------------------------------------------------------------
# Activités
# --------------------------------------------------------------------------
ACTIVITES = [
    {
        "key": "degorgement",
        "slug": "degorgement-canalisation",
        "nom": "Dégorgement & Canalisations",
        "nom_court": "Dégorgement",
        "metier": "Dégorgement et curage de canalisations",
        "pro": "technicien assainissement",
        "pro_pluriel": "techniciens assainissement",
        "h1": "Dégorgement & Débouchage de Canalisations",
        "accroche": ("Canalisation bouchée, WC qui refoule, évacuation qui déborde&nbsp;? "
                     "Nos camions hydrocureurs interviennent en urgence, 7j/7."),
        "mots_cles": "dégorgement, débouchage canalisation, curage, hydrocurage, WC bouché, fosse septique",
        "hero_points": [
            "Camion hydrocureur et furet électrique haute performance",
            "Inspection par caméra avant et après intervention",
            "Débouchage garanti ou nous revenons sans frais",
        ],
        "prestations": [
            ("Débouchage WC, éviers et douches",
             "Furet électrique ou pompe haute pression selon le type de bouchon et la nature du réseau."),
            ("Hydrocurage haute pression",
             "Curage complet des canalisations jusqu'à 200 bars pour éliminer graisses, tartre et racines."),
            ("Inspection vidéo par caméra",
             "Diagnostic précis de l'état du réseau, localisation exacte du bouchon ou de la casse, rapport remis."),
            ("Débouchage de colonnes d'immeuble",
             "Intervention sur chutes d'eaux usées et colonnes collectives pour syndics et copropriétés."),
            ("Vidange de fosse septique et micro-station",
             "Pompage, nettoyage et contrôle du bon fonctionnement, avec bordereau d'élimination des déchets."),
            ("Dégraissage de bacs à graisse",
             "Entretien périodique pour restaurants, cantines et collectivités, avec contrat possible."),
            ("Pompage de cave et de regard inondés",
             "Évacuation des eaux après un refoulement ou de fortes pluies, remise en état du regard."),
            ("Détection et mise à jour de réseaux",
             "Localisation de canalisation enterrée, regard introuvable, plan de réseau et préconisations."),
        ],
        "urgences": [
            "WC bouché dans un logement sans autre sanitaire",
            "Refoulement d'eaux usées dans une douche ou une cave",
            "Colonne d'immeuble engorgée impactant plusieurs logements",
            "Débordement de regard ou de fosse septique",
        ],
        "tarifs": [
            ("Débouchage simple (WC, évier, douche)", "à partir de 129 € TTC"),
            ("Débouchage avec camion hydrocureur", "à partir de 249 € TTC"),
            ("Hydrocurage préventif de réseau", "à partir de 290 € TTC"),
            ("Inspection vidéo par caméra", "à partir de 179 € TTC"),
            ("Vidange de fosse septique (3 m³)", "à partir de 280 € TTC"),
            ("Majoration nuit, dimanche et jours fériés", "sur devis validé avant intervention"),
        ],
        "faq": [
            ("Combien de temps pour un dégorgement d'urgence {art} {dept}&nbsp;?",
             "Nos équipes sont positionnées sur {prefecture} et les principales villes {du_dept}. "
             "En urgence, nous visons une intervention dans l'heure sur les secteurs proches et "
             "sous 2 à 3 heures sur les zones rurales. Le délai vous est annoncé au téléphone, "
             "avant tout déplacement."),
            ("Le devis est-il vraiment gratuit&nbsp;?",
             "Oui. Le diagnostic et le devis sont gratuits et sans engagement. Le tarif est "
             "annoncé et validé avec vous avant le démarrage des travaux&nbsp;: aucune surprise "
             "ne s'ajoute sur la facture finale."),
            ("Quelle différence entre un débouchage et un hydrocurage&nbsp;?",
             "Le débouchage lève le bouchon pour rétablir l'écoulement immédiatement. "
             "L'hydrocurage nettoie la paroi complète de la canalisation à haute pression&nbsp;: "
             "il retire les dépôts de graisse et de tartre qui provoquent les bouchons à répétition. "
             "C'est la solution durable quand le problème revient."),
            ("Qui paie le dégorgement en location&nbsp;: locataire ou propriétaire&nbsp;?",
             "L'entretien courant des évacuations relève du locataire. En revanche, un défaut "
             "structurel (canalisation affaissée, racines, vétusté) est à la charge du "
             "propriétaire. Notre rapport d'inspection vidéo permet de trancher objectivement et "
             "sert de justificatif auprès de l'assurance ou du bailleur."),
            ("Intervenez-vous pour les copropriétés et les professionnels&nbsp;?",
             "Oui. Nous travaillons avec des syndics, bailleurs, restaurants et collectivités "
             "{du_dept}, en dépannage ponctuel comme en contrat d'entretien annuel "
             "(colonnes, bacs à graisse, réseaux extérieurs)."),
            ("Que faire en attendant votre arrivée&nbsp;?",
             "N'utilisez plus les évacuations concernées, coupez l'arrivée d'eau si l'eau monte, "
             "et évitez les déboucheurs chimiques&nbsp;: ils abîment les joints et rendent "
             "l'intervention plus dangereuse pour le technicien."),
        ],
        "avis": [
            ("WC bouché un dimanche matin, technicien sur place en 50 minutes. Débouché et "
             "nettoyé proprement, prix exactement celui annoncé au téléphone. Rien à redire.",
             "Sébastien L.", 5),
            ("Colonne d'immeuble engorgée sur nos 6 logements. Hydrocurage complet et passage "
             "caméra avec rapport pour le syndic. Travail sérieux et parfaitement documenté.",
             "Marie-Hélène T.", 5),
            ("Fosse septique à vider dans une maison familiale. Rendez-vous tenu, bordereau "
             "fourni, équipe agréable et soigneuse. Je les rappellerai pour l'entretien.",
             "Gwenaël P.", 5),
        ],
        "prose_titre": "Dégorgement {art} {dept} ({num})&nbsp;: nos interventions au quotidien",
        "prose": [
            "Une canalisation ne se bouche jamais du jour au lendemain. Les dépôts de graisse, "
            "de calcaire, de cheveux et de lingettes s'accumulent pendant des mois, réduisent le "
            "diamètre utile du tuyau, puis l'obstruent totalement au plus mauvais moment. "
            "{Art} {dept}, nos {pro_pluriel} traitent chaque semaine des évacuations "
            "d'éviers saturées, des WC qui refoulent et des regards extérieurs débordants.",
            "Le territoire a ses particularités&nbsp;: {contexte}. "
            "Ces contraintes locales, nous les connaissons parce que nous intervenons sur le "
            "terrain tous les jours, de {ville1} à {ville2} en passant par {ville3}.",
            "Notre méthode est toujours la même&nbsp;: identifier la cause avant d'agir. Un "
            "bouchon ponctuel se traite au furet en moins d'une heure. Un réseau encrassé "
            "demande un hydrocurage haute pression. Une canalisation affaissée ou percée "
            "nécessite une inspection caméra et un chiffrage de réparation. Vous repartez "
            "toujours avec un diagnostic clair, pas seulement avec un écoulement rétabli.",
        ],
        "photos": [
            ("degorgement-1.jpg", "Camion hydrocureur ETS-BZH en intervention",
             "Camion hydrocureur en intervention"),
            ("degorgement-2.jpg", "Inspection vidéo d'une canalisation par caméra",
             "Inspection vidéo du réseau"),
            ("degorgement-3.jpg", "Débouchage d'une colonne d'eaux usées en immeuble",
             "Débouchage de colonne d'immeuble"),
            ("degorgement-4.jpg", "Curage haute pression d'un réseau extérieur",
             "Curage haute pression"),
        ],
        "photo_equipe": ("degorgement-equipe.jpg",
                         "Technicien assainissement ETS-BZH et son matériel"),
        "prose_h3": [
            ("Les bouchons les plus fréquents {art} {dept}",
             ["Lingettes et produits d'hygiène dans les WC — première cause d'urgence",
              "Graisses figées dans les évacuations de cuisine, aggravées par l'eau froide",
              "Cheveux et savon dans les bondes de douche et de baignoire",
              "Racines d'arbustes infiltrées dans les réseaux enterrés anciens",
              "Calcaire et tartre sur les canalisations en fonte des bâtiments anciens"]),
            ("Prévenir plutôt que déboucher",
             ["Un hydrocurage préventif tous les 2 à 3 ans sur une maison individuelle",
              "Un dégraissage semestriel pour les cuisines professionnelles",
              "Une vidange de fosse septique tous les 4 ans environ selon l'occupation",
              "Des grilles anti-cheveux sur les douches et un bac à graisse entretenu"]),
        ],
    },

    {
        "key": "plomberie",
        "slug": "plomberie-depannage",
        "nom": "Plomberie & Dépannage",
        "nom_court": "Plomberie",
        "metier": "Plomberie et dépannage sanitaire",
        "pro": "plombier",
        "pro_pluriel": "plombiers",
        "h1": "Plomberie & Dépannage d'Urgence",
        "accroche": ("Fuite d'eau, chauffe-eau en panne, dégât des eaux&nbsp;? "
                     "Un plombier qualifié se déplace chez vous en urgence, 7j/7."),
        "mots_cles": "plombier, dépannage plomberie, recherche de fuite, chauffe-eau, dégât des eaux",
        "hero_points": [
            "Recherche de fuite non destructive (caméra thermique, gaz traceur)",
            "Véhicules équipés&nbsp;: réparation immédiate dans la majorité des cas",
            "Tarifs annoncés avant intervention, garantie décennale",
        ],
        "prestations": [
            ("Recherche de fuite non destructive",
             "Caméra thermique, gaz traceur et détection acoustique pour localiser la fuite sans casser."),
            ("Réparation de fuite d'eau",
             "Fuite sur canalisation encastrée, raccord, colonne ou compteur&nbsp;: réparation ou remplacement."),
            ("Dépannage et remplacement de chauffe-eau",
             "Ballon électrique, thermodynamique ou chauffe-eau gaz&nbsp;: diagnostic, résistance, groupe de sécurité."),
            ("Robinetterie et sanitaires",
             "Mitigeur qui goutte, chasse d'eau défectueuse, WC, lavabo, douche&nbsp;: remplacement soigné."),
            ("Dégât des eaux et assèchement",
             "Coupure, mise en sécurité, réparation et rapport détaillé pour votre déclaration d'assurance."),
            ("Remplacement de canalisations",
             "Reprise de réseaux plomb, cuivre ou PER vétustes, avec mise en conformité sanitaire."),
            ("Installation de salle de bain",
             "Création ou rénovation complète&nbsp;: alimentation, évacuation, pose des sanitaires."),
            ("Détartrage et entretien",
             "Traitement du calcaire, adoucisseur, entretien préventif des installations sanitaires."),
        ],
        "urgences": [
            "Fuite d'eau active ou canalisation percée",
            "Absence totale d'eau chaude dans le logement",
            "Dégât des eaux en cours chez vous ou chez le voisin",
            "Canalisation gelée ou éclatée en période de froid",
        ],
        "tarifs": [
            ("Déplacement + diagnostic plomberie", "à partir de 79 € TTC"),
            ("Réparation de fuite simple", "à partir de 149 € TTC"),
            ("Recherche de fuite non destructive", "à partir de 250 € TTC"),
            ("Remplacement de chauffe-eau 200 L", "à partir de 690 € TTC pose comprise"),
            ("Remplacement de mitigeur ou robinet", "à partir de 110 € TTC"),
            ("Majoration nuit, dimanche et jours fériés", "sur devis validé avant intervention"),
        ],
        "faq": [
            ("Sous quel délai un plombier peut-il intervenir {art} {dept}&nbsp;?",
             "Pour une fuite active, nous visons une intervention dans l'heure autour de "
             "{prefecture} et des principales villes {du_dept}. Sur les communes plus "
             "éloignées, comptez 2 à 3 heures. Le créneau exact vous est confirmé lors de "
             "l'appel, avec le nom du technicien."),
            ("Combien coûte une recherche de fuite&nbsp;?",
             "Une recherche de fuite non destructive démarre à 250 € TTC selon la surface et "
             "la technologie nécessaire (caméra thermique, gaz traceur, corrélation acoustique). "
             "Elle est très souvent prise en charge par votre assurance habitation dans le cadre "
             "d'un dégât des eaux&nbsp;: nous fournissons le rapport nécessaire."),
            ("Que faire immédiatement en cas de fuite importante&nbsp;?",
             "Fermez le robinet d'arrêt général (souvent sous l'évier, dans le garage ou au "
             "compteur), coupez l'électricité de la zone si l'eau approche d'une prise, puis "
             "appelez-nous au {tel}. Nous vous guidons par téléphone en attendant l'arrivée du "
             "technicien."),
            ("Intervenez-vous sur les chauffe-eau de toutes marques&nbsp;?",
             "Oui&nbsp;: Atlantic, Thermor, Ariston, De Dietrich, Chaffoteaux, Saunier Duval et "
             "les autres marques courantes. Nous dépannons en priorité (résistance, thermostat, "
             "groupe de sécurité) et ne proposons un remplacement que lorsque la réparation "
             "n'est plus rentable."),
            ("Vos travaux sont-ils garantis&nbsp;?",
             "Oui. Nos artisans sont assurés en responsabilité civile professionnelle et "
             "couverts par la garantie décennale pour les travaux qui l'exigent. Les pièces "
             "posées bénéficient de la garantie constructeur, et la main-d'œuvre est garantie."),
            ("Puis-je obtenir un devis avant de m'engager&nbsp;?",
             "Toujours. Le devis est gratuit, détaillé et sans engagement. Rien ne commence "
             "avant votre accord écrit ou signé sur tablette, et le montant validé est celui qui "
             "figure sur la facture."),
        ],
        "avis": [
            ("Fuite sous l'évier un samedi soir, plombier arrivé en 45 minutes. Réparation "
             "propre, explications claires, facture conforme au devis annoncé. Impeccable.",
             "Nathalie R.", 5),
            ("Chauffe-eau HS avec trois enfants à la maison. Diagnostic fait le jour même et "
             "remplacement dès le lendemain matin. Efficaces, ponctuels et très corrects.",
             "Yann K.", 5),
            ("Recherche de fuite sur une dalle sans rien casser. Rapport complet transmis à "
             "l'assurance qui a tout pris en charge. Vrai professionnalisme.",
             "Christophe M.", 5),
        ],
        "prose_titre": "Plombier {art} {dept} ({num})&nbsp;: dépannage, réparation et rénovation",
        "prose": [
            "Une fuite d'eau non traitée, c'est en moyenne plusieurs centaines de litres perdus "
            "par jour, une facture qui grimpe et, très vite, des dégâts sur les cloisons et les "
            "sols. C'est pourquoi nos {pro_pluriel} {art} {dept} interviennent en priorité "
            "sur les fuites actives et les coupures d'eau chaude, tous les jours de l'année.",
            "Le parc immobilier local a ses réalités&nbsp;: {contexte}. "
            "Nos véhicules sont donc équipés des pièces les plus courantes pour traiter la "
            "majorité des pannes dès le premier passage, de {ville1} à {ville2} jusqu'à {ville3}.",
            "Nous travaillons dans les deux sens&nbsp;: l'urgence, avec une intervention rapide et "
            "un tarif annoncé avant de commencer&nbsp;; et le travail de fond, avec la rénovation "
            "de salle de bain, le remplacement de réseaux vétustes et la mise en conformité "
            "sanitaire. Dans les deux cas, même exigence de propreté du chantier et de clarté "
            "sur le prix.",
        ],
        "photos": [
            ("plomberie-1.jpg", "Recherche de fuite par caméra thermique",
             "Recherche de fuite non destructive"),
            ("plomberie-2.jpg", "Remplacement d'un chauffe-eau électrique",
             "Remplacement de chauffe-eau"),
            ("plomberie-3.jpg", "Réfection d'un réseau d'alimentation en cuivre",
             "Réfection de réseau d'alimentation"),
            ("plomberie-4.jpg", "Installation complète d'une salle de bain",
             "Installation de salle de bain"),
        ],
        "photo_equipe": ("plomberie-equipe.jpg",
                         "Plombier ETS-BZH équipé sur une intervention"),
        "prose_h3": [
            ("Les dépannages les plus demandés {art} {dept}",
             ["Fuite sur flexible, siphon ou raccord sous évier",
              "Panne de chauffe-eau&nbsp;: plus d'eau chaude ou eau tiède",
              "Fuite encastrée détectée par une facture d'eau anormale",
              "Chasse d'eau qui fuit en continu et gonfle la consommation",
              "Canalisation gelée ou éclatée après un épisode de grand froid"]),
            ("Nos engagements sur chaque chantier",
             ["Devis gratuit et détaillé, validé avant toute intervention",
              "Techniciens qualifiés, assurés et couverts par la garantie décennale",
              "Chantier protégé et nettoyé avant notre départ",
              "Facture conforme au devis, sans frais ajoutés à la fin"]),
        ],
    },

    {
        "key": "electricite",
        "slug": "electricite-urgence",
        "nom": "Électricité Générale & Urgence",
        "nom_court": "Électricité",
        "metier": "Électricité générale et dépannage",
        "pro": "électricien",
        "pro_pluriel": "électriciens",
        "h1": "Électricité Générale & Dépannage d'Urgence",
        "accroche": ("Panne de courant, tableau qui disjoncte, odeur de brûlé&nbsp;? "
                     "Un électricien qualifié sécurise votre installation en urgence, 7j/7."),
        "mots_cles": "électricien, dépannage électrique, panne de courant, tableau électrique, mise aux normes NF C 15-100",
        "hero_points": [
            "Recherche de panne et mise en sécurité immédiate",
            "Mise aux normes NF C 15-100 et remplacement de tableau",
            "Électriciens qualifiés, travaux garantis décennale",
        ],
        "prestations": [
            ("Recherche de panne électrique",
             "Diagnostic complet du circuit, identification du défaut et remise en service sécurisée."),
            ("Dépannage de tableau électrique",
             "Disjoncteur qui saute, différentiel défectueux, fusible&nbsp;: réparation ou remplacement."),
            ("Mise aux normes NF C 15-100",
             "Mise en conformité de l'installation, protection différentielle 30 mA et mise à la terre."),
            ("Remplacement de tableau électrique",
             "Tableau vétuste ou saturé&nbsp;: remplacement complet, repérage des circuits et attestation."),
            ("Court-circuit et surchauffe",
             "Intervention d'urgence sur odeur de brûlé, prise noircie ou point chaud dans le tableau."),
            ("Installation de prises et éclairage",
             "Ajout de points lumineux, prises, interrupteurs, va-et-vient et circuits dédiés."),
            ("Borne de recharge véhicule électrique",
             "Étude, pose et raccordement de borne IRVE avec protection dédiée conforme."),
            ("Diagnostic électrique avant vente ou location",
             "Contrôle de l'installation, rapport des points à reprendre et chiffrage des travaux."),
        ],
        "urgences": [
            "Panne de courant totale sur le logement",
            "Odeur de brûlé, prise noircie ou étincelles",
            "Tableau électrique qui disjoncte en boucle",
            "Installation mouillée après une fuite ou une inondation",
        ],
        "tarifs": [
            ("Déplacement + diagnostic électrique", "à partir de 89 € TTC"),
            ("Recherche de panne et remise en service", "à partir de 150 € TTC"),
            ("Remplacement de disjoncteur ou différentiel", "à partir de 130 € TTC"),
            ("Remplacement de tableau électrique complet", "à partir de 890 € TTC"),
            ("Pose de borne de recharge 7,4 kW", "à partir de 1 190 € TTC"),
            ("Majoration nuit, dimanche et jours fériés", "sur devis validé avant intervention"),
        ],
        "faq": [
            ("Intervenez-vous en urgence la nuit {art} {dept}&nbsp;?",
             "Oui, 24h/24 et 7j/7 pour les situations à risque&nbsp;: odeur de brûlé, "
             "étincelles, panne totale, installation mouillée. Nos électriciens couvrent "
             "{prefecture} et l'ensemble {du_dept}, avec une priorité donnée aux "
             "interventions de mise en sécurité."),
            ("Mon tableau disjoncte en permanence, est-ce grave&nbsp;?",
             "C'est un signal à ne pas ignorer. Un différentiel qui saute protège les personnes "
             "contre un défaut d'isolement — il y a donc bien une anomalie sur un circuit ou un "
             "appareil. Ne forcez pas le réarmement à répétition&nbsp;: nous identifions le "
             "circuit fautif et traitons la cause réelle."),
            ("Qu'impose la norme NF C 15-100&nbsp;?",
             "Elle définit les règles de sécurité des installations basse tension&nbsp;: "
             "protection différentielle 30 mA, mise à la terre, nombre de prises par pièce, "
             "protection des circuits spécialisés et liaison équipotentielle dans les pièces "
             "d'eau. Nous établissons un état des lieux et chiffrons les reprises nécessaires."),
            ("Faut-il tout refaire pour mettre aux normes une maison ancienne&nbsp;?",
             "Rarement. Dans la plupart des logements anciens {du_dept}, une mise en sécurité "
             "ciblée suffit&nbsp;: remplacement du tableau, ajout de différentiels 30 mA, "
             "création d'une terre correcte et reprise des points dangereux. La réfection "
             "complète ne se justifie que sur des installations très dégradées."),
            ("Posez-vous des bornes de recharge pour voiture électrique&nbsp;?",
             "Oui, en maison individuelle comme en copropriété&nbsp;: étude de puissance, "
             "circuit dédié protégé, pose et mise en service de la borne, avec les documents "
             "nécessaires aux aides éventuelles."),
            ("Vos interventions sont-elles garanties&nbsp;?",
             "Oui. Nos électriciens sont qualifiés, assurés en responsabilité civile "
             "professionnelle et couverts par la garantie décennale sur les travaux concernés. "
             "Chaque intervention fait l'objet d'une facture détaillée."),
        ],
        "avis": [
            ("Panne totale un dimanche, électricien sur place en une heure. Défaut trouvé sur "
             "un circuit de la cuisine, remis en service le soir même. Très rassurant.",
             "Isabelle G.", 5),
            ("Tableau électrique d'origine à remplacer dans une maison de 1975. Travail "
             "impeccable, circuits repérés et étiquetés, explications claires. Rien à redire.",
             "Pierre-Yves C.", 5),
            ("Borne de recharge installée à la maison. Devis clair, délai tenu, finition "
             "soignée. Une équipe sérieuse que je recommande sans hésiter.",
             "Laurent D.", 5),
        ],
        "prose_titre": "Électricien {art} {dept} ({num})&nbsp;: dépannage, sécurité et mise aux normes",
        "prose": [
            "Une installation électrique vieillissante est la première cause d'incendie "
            "domestique d'origine électrique. Tableau sans différentiel 30 mA, absence de mise à "
            "la terre, fils sous gaine dégradée&nbsp;: ces défauts restent invisibles jusqu'à "
            "l'incident. Nos {pro_pluriel} {art} {dept} interviennent aussi bien "
            "en urgence qu'en prévention pour remettre les installations en sécurité.",
            "Sur le territoire, nous rencontrons {contexte}. "
            "Autant de situations où l'humidité, l'ancienneté du bâti et des extensions "
            "successives fragilisent les circuits. Nous intervenons de {ville1} à {ville2}, "
            "en passant par {ville3}.",
            "Notre priorité en dépannage est toujours la mise en sécurité&nbsp;: isoler le "
            "circuit en défaut, rétablir le courant sur le reste du logement, puis vous proposer "
            "la réparation durable. Vous savez exactement ce qui a été fait, ce qui reste à "
            "faire, et à quel prix.",
        ],
        "photos": [
            ("electricite-1.jpg", "Remplacement d'un tableau électrique",
             "Remplacement de tableau électrique"),
            ("electricite-2.jpg", "Mise aux normes d'une installation NF C 15-100",
             "Mise aux normes NF C 15-100"),
            ("electricite-3.jpg", "Recherche de panne sur un circuit électrique",
             "Recherche de panne"),
            ("electricite-4.jpg", "Pose d'une borne de recharge pour véhicule électrique",
             "Pose de borne de recharge"),
        ],
        "photo_equipe": ("electricite-equipe.jpg",
                         "Électricien ETS-BZH en intervention"),
        "prose_h3": [
            ("Les signaux qui doivent vous alerter",
             ["Une odeur de brûlé ou une prise qui noircit — coupez et appelez immédiatement",
              "Un disjoncteur différentiel qui saute plusieurs fois par semaine",
              "Des fusibles à broche ou un tableau sans protection différentielle 30 mA",
              "Des prises sans terre, notamment dans la cuisine et la salle de bain",
              "Un compteur qui chauffe ou des lumières qui faiblissent à l'allumage d'un appareil"]),
            ("Nos travaux de mise en conformité",
             ["Remplacement du tableau avec repérage et étiquetage des circuits",
              "Création ou reprise de la prise de terre et de la liaison équipotentielle",
              "Ajout de circuits spécialisés pour les appareils de forte puissance",
              "Sécurisation des pièces d'eau selon les volumes définis par la norme"]),
        ],
    },
]

# --------------------------------------------------------------------------
# Éléments transverses
# --------------------------------------------------------------------------
REASSURANCE = [
    ("Intervention 24/7 en urgence",
     "Astreinte réelle nuits, week-ends et jours fériés. Un interlocuteur au bout du fil, "
     "pas un répondeur, et un délai annoncé dès l'appel."),
    ("Devis gratuit sans engagement",
     "Diagnostic et chiffrage offerts. Le prix est validé avec vous avant de commencer&nbsp;: "
     "la facture ne dépasse jamais le devis accepté."),
    ("Artisans qualifiés & expérimentés",
     "Des professionnels du métier, formés et équipés, qui interviennent en Bretagne toute "
     "l'année. Pas de sous-traitance improvisée."),
    ("Garantie décennale",
     "Responsabilité civile professionnelle et garantie décennale sur les travaux concernés. "
     "Vous êtes couvert, et nous assumons nos interventions."),
]

ETAPES = [
    ("Vous appelez", "Un technicien vous répond directement, qualifie la panne au téléphone et "
     "vous annonce un créneau réaliste ainsi qu'un ordre de prix."),
    ("Nous diagnostiquons", "Sur place, l'intervenant identifie la cause exacte du problème avec "
     "le matériel adapté, et vous l'explique simplement."),
    ("Vous validez le devis", "Le montant est présenté avant les travaux. Rien ne démarre sans "
     "votre accord&nbsp;: c'est vous qui décidez, sans pression."),
    ("Nous intervenons", "Réparation réalisée, chantier nettoyé, fonctionnement vérifié devant "
     "vous, facture détaillée remise avec la garantie."),
]

PHOTOS_ACCUEIL = [
    ("realisation-1.jpg", "Intervention de dégorgement par ETS-BZH",
     "Dégorgement de canalisation"),
    ("realisation-2.jpg", "Recherche et réparation de fuite d'eau",
     "Réparation de fuite"),
    ("realisation-3.jpg", "Remplacement d'un tableau électrique",
     "Mise aux normes électrique"),
    ("realisation-4.jpg", "Curage d'un réseau d'assainissement",
     "Curage de réseau"),
    ("realisation-5.jpg", "Installation d'un chauffe-eau",
     "Pose de chauffe-eau"),
    ("realisation-6.jpg", "Véhicule d'intervention ETS-BZH en Bretagne",
     "Nos véhicules en Bretagne"),
]

PHOTO_EQUIPE = ("equipe.jpg", "L'équipe ETS-BZH et ses véhicules d'intervention")
PHOTO_CONTACT = ("atelier.jpg", "Atelier et matériel professionnel ETS-BZH")

STATS = [
    ("24/7", "Astreinte urgence"),
    ("4", "Départements couverts"),
    ("&lt; 1 h", "Délai visé en urgence"),
    ("100 %", "Devis gratuits"),
]
