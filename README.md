Description

Ce projet vise à analyser les expérimentations 5G en France, menées par l'ARCEP, pour en extraire des informations pertinentes. À partir d'un jeu de données contenant des informations détaillées sur ces expérimentations, l'objectif est de générer une carte interactive des sites d'expérimentation et de produire des graphiques pour visualiser la répartition des expérimentations par région, technologie, bande de fréquence, et d'autres critères.

Les résultats sont présentés sous forme de graphiques et de rapports interactifs. Ce projet est destiné à fournir une compréhension plus approfondie des expérimentations en cours et de leur déploiement sur le territoire français.



|-- README.md                  # Ce fichier
|-- analyse_5g.py               # Script principal pour traiter les données et générer les résultats
|-- experimentations_5G.csv     # Fichier des données des expérimentations 5G (doit être ajouté manuellement)
|-- cartes/                     # Dossier contenant la carte HTML générée
|-- graphiques/                 # Dossier contenant les graphiques générés
    |-- projets_par_bande_de_frequences.png
    |-- repartition_par_region.png
    |-- top_departements.png
    |-- technologies_mises_en_oeuvre.png
|-- rapport/                    # Dossier contenant le bilan de l'étude
    |-- bilan_etude.pdf

