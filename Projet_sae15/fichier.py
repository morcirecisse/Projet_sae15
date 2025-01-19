import pandas as pd
import folium
import os
import webbrowser
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement du fichier CSV
file_path = "experimentations_5G.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Le fichier '{file_path}' est introuvable.")

data = pd.read_csv(file_path, encoding='cp1252', sep=';')

# Partie 1 : Création de la carte avec Folium

def creer_carte(data):
    # Création d'une carte avec Folium
    location = [47, 1]  # Coordonnées centrées sur la France
    zoom = 6
    tiles = 'cartodbpositron'  
    Carte = folium.Map(location=location, zoom_start=zoom, tiles=tiles)

    # Ajout des marqueurs avec des informations détaillées
    if 'Latitude' in data.columns and 'Longitude' in data.columns:
        for idx, row in data.iterrows():
            try:
                # Conversion des coordonnées en float
                latitude = float(str(row['Latitude']).replace(',', '.'))
                longitude = float(str(row['Longitude']).replace(',', '.'))

                # Construction du contenu du popup
                popup_content = f"""
                    <b>Expérimentateur:</b> {row.get('Expérimentateur', 'Inconnu')}<br>
                    <b>Région:</b> {row.get('Région', 'Inconnue')}<br>
                    <b>Département:</b> {row.get('Département', 'Inconnu')}<br>
                    <b>Commune:</b> {row.get('Commune', 'Inconnu')}<br>
                    <b>Description:</b> {row.get('Description', 'Aucune description disponible')}<br>
                    <b>Bande de fréquences:</b> {row.get('Bande de fréquences', 'Inconnu')}<br>
                """

                # Ajout d'un marqueur avec les informations
                folium.Marker(
                    location=[latitude, longitude],
                    popup=folium.Popup(popup_content, max_width=300),
                    icon=folium.Icon(color="blue", icon="info-sign")
                ).add_to(Carte)
            except ValueError:
                print(f"Ligne {idx} ignorée : Coordonnées invalides ou données manquantes.")
    else:
        print("Colonnes 'Latitude' et 'Longitude' introuvables dans le fichier.")

    # Sauvegarde de la carte en HTML
    output_path = "map.html"
    Carte.save(output_path)

    # Ouverture automatiquement de la carte dans le navigateur
    webbrowser.open(f"file://{os.path.abspath(output_path)}")
    print(f"Carte générée et affichée. Ouvrez manuellement '{output_path}' si le navigateur ne s'ouvre pas automatiquement.")

# Partie 2 : Génération des graphiques

def generer_graphiques(data):
    try:
        # Vérification des colonnes disponibles
        colonnes = data.columns
        print(f"Colonnes disponibles : {colonnes}")

        # Projets par bande de fréquences
        if 'Bande de fréquences' in colonnes:
            plt.figure(figsize=(10, 5))
            data['Bande de fréquences'].value_counts().plot(kind='bar', color='green')
            plt.title("Projets par bande de fréquences", fontsize=14)
            plt.xlabel("Bande de fréquences", fontsize=12)
            plt.ylabel("Nombre de projets", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.tight_layout()
            plt.savefig("projets_par_bande_de_frequences.png")
            plt.show()

        # Répartition des expérimentateurs par région
        if 'Région' in colonnes:
            plt.figure(figsize=(10, 6))
            data['Région'].value_counts().plot(kind='bar', color='skyblue')
            plt.title("Répartition des expérimentateurs par région", fontsize=14)
            plt.xlabel("Régions", fontsize=12)
            plt.ylabel("Nombre d'expérimentateurs", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.tight_layout()
            plt.savefig("repartition_par_region.png")
            plt.show()

        # Répartition des expérimentateurs par commune
        if 'Commune' in colonnes:
            plt.figure(figsize=(10, 6))
            data['Commune'].value_counts().head(10).plot(kind='bar', color='purple')
            plt.title("Top 10 des communes par nombre d'expérimentations", fontsize=14)
            plt.xlabel("Communes", fontsize=12)
            plt.ylabel("Nombre d'expérimentations", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.tight_layout()
            plt.savefig("repartition_par_commune.png")
            plt.show()

        # Répartition des usages
        usage_cols = [col for col in colonnes if col.startswith('Usage -')]
        if usage_cols:
            plt.figure(figsize=(10, 6))
            data[usage_cols].sum().sort_values().plot(kind='barh', color='orange')
            plt.title("Répartition des usages", fontsize=14)
            plt.xlabel("Nombre d'expérimentations", fontsize=12)
            plt.ylabel("Type d'usage", fontsize=12)
            plt.tight_layout()
            plt.savefig("repartition_des_usages.png")
            plt.show()

        # Nombre de projets par département
        if 'Département' in colonnes:
            plt.figure(figsize=(12, 6))
            data['Département'].value_counts().head(10).plot(kind='bar', color='purple')
            plt.title("Top 10 des départements par nombre de projets", fontsize=14)
            plt.xlabel("Département", fontsize=12)
            plt.ylabel("Nombre de projets", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.tight_layout()
            plt.savefig("top_departements.png")
            plt.show()

    except Exception as e:
        print(f"Erreur lors de la génération des graphiques : {e}")

# Partie 3 : Graphique des technologies mises en œuvre

def graphique_technologies(data):
    try:
        # Extraire les colonnes liées aux technologies (commençant par 'Techno -')
        technologie_cols = [col for col in data.columns if col.startswith('Techno -')]

        if technologie_cols:
            # Compter le nombre total d'expérimentations pour chaque technologie
            technologie_counts = data[technologie_cols].sum()

            # Générer le graphique
            plt.figure(figsize=(10, 6))
            technologie_counts.sort_values().plot(kind='barh', color='teal')
            plt.title("Technologies mises en œuvre", fontsize=14)
            plt.xlabel("Nombre d'expérimentations", fontsize=12)
            plt.ylabel("Technologies", fontsize=12)
            plt.tight_layout()
            plt.savefig("technologies_mises_en_oeuvre.png")  # Sauvegarder le graphique
            plt.show()
        else:
            print("Aucune colonne relative aux technologies trouvée dans le fichier.")

    except Exception as e:
        print(f"Erreur lors de la génération du graphique des technologies : {e}")

# Appels des fonctions
creer_carte(data)
generer_graphiques(data)
graphique_technologies(data)

print("Traitement terminé avec succès.")
