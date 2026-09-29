import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset créé par le scraping
df = pd.read_csv("dataset.csv")

# Créer le dossier où seront enregistrés les graphiques
os.makedirs("outputs/graphs", exist_ok=True)

# Choisir un style propre pour tous les graphiques
sns.set_theme(style="whitegrid")

# Graphique 1 : répartition des prix
plt.figure(figsize=(9, 5))
sns.histplot(df["Prix_GBP"], bins=20, color="#4C72B0")
plt.title("Répartition des prix des livres")
plt.xlabel("Prix (£)")
plt.ylabel("Nombre de livres")
plt.tight_layout()

# Sauvegarder l'image puis l'afficher
plt.savefig("outputs/graphs/01_distribution_prix.png", dpi=150)
plt.show()
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset créé par le scraping
d
f = pd.read_csv("dataset.csv")

# Créer le dossier où seront enregistrés les graphiques
os.makedirs("outputs/graphs", exist_ok=True)


# Choisir un style propre pour tous les graphiques
sns.set_theme(style="whitegrid")

# Graphique 1 : répartition des prix
plt.figure(figsize=(9, 5))
sns.histplot(df["Prix_GBP"], bins=20, color="#4C72B0")
plt.title("Répartition des prix des livres")
plt.xlabel("Prix (£)")
plt.ylabel("Nombre de livres")
plt.tight_layout()

# Sauvegarder l'image puis l'afficher
plt.savefig("outputs/graphs/01_distribution_prix.png", dpi=150)
plt.show()


# Graphique 2 : nombre de livres pour chaque note
plt.figure(figsize=(9, 5))
sns.countplot(x="Note", data=df, color="#55A868")
plt.title("Nombre de livres par note")
plt.xlabel("Note (de 1 à 5 étoiles)")
plt.ylabel("Nombre de livres")
plt.tight_layout()
plt.savefig("outputs/graphs/02_livres_par_note.png", dpi=150)
plt.show()


# Graphique 3 : prix moyen pour chaque note
plt.figure(figsize=(9, 5))
sns.barplot(x="Note", y="Prix_GBP", data=df, color="#C44E52", errorbar=None)
plt.title("Prix moyen des livres selon la note")
plt.xlabel("Note (de 1 à 5 étoiles)")
plt.ylabel("Prix moyen (£)")
plt.tight_layout()

plt.savefig("outputs/graphs/03_prix_moyen_par_note.png", dpi=150)
plt.show()

# Graphique 4 : prix de chaque livre selon sa note
plt.figure(figsize=(9, 5))
sns.stripplot(x="Note", y="Prix_GBP", data=df, alpha=0.5, jitter=True, color="#8172B2")
plt.title("Prix de chaque livre selon sa note")
plt.xlabel("Note (de 1 à 5 étoiles)")
plt.ylabel("Prix (£)")
plt.tight_layout()

plt.savefig("outputs/graphs/04_prix_vs_note.png", dpi=150)
plt.show()