# CodeAlpha - Data Visualization

Projet réalisé dans le cadre du stage virtuel **Data Analytics** chez CodeAlpha (Tâche 3 : Data Visualization).

## Objectif

Transformer des données brutes en graphiques clairs pour répondre à des questions simples :
- Comment les prix des livres sont-ils répartis ?
- Les notes sont-elles équilibrées ?
- Un livre mieux noté coûte-t-il plus cher ?

## Dataset

- **Source** : [books.toscrape.com](https://books.toscrape.com/), collecté par web scraping (Tâche 1)
- **Taille** : 1000 livres
- **Colonnes** :

| Colonne | Description |
|---|---|
| Titre | Titre du livre |
| Prix_GBP | Prix en livres sterling (£) |
| Disponibilite | Statut de disponibilité |
| Note | Note du livre, de 1 à 5 étoiles |

## Outils utilisés

- Python 3
- pandas (chargement et traitement des données)
- matplotlib (création des graphiques)
- seaborn (style et graphiques statistiques)

## Structure du projet

```
CodeAlpha_DataVisualization/
├── dataset.csv
├── visualisation.py
├── outputs/
│   └── graphs/
│       ├── 01_distribution_prix.png
│       ├── 02_livres_par_note.png
│       ├── 03_prix_moyen_par_note.png
│       └── 04_prix_vs_note.png
└── README.md
```

## Visualisations et analyse

### 1. Répartition des prix
![Répartition des prix](outputs/graphs/01_distribution_prix.png)

Les prix vont d'environ 10 £ à 60 £. Ils sont répartis sur toute cette plage, sans grande concentration à un endroit précis : la boutique propose des livres à tous les niveaux de prix.

### 2. Nombre de livres par note
![Livres par note](outputs/graphs/02_livres_par_note.png)

Chaque note (de 1 à 5 étoiles) regroupe à peu près le même nombre de livres, autour de 200. Aucune note ne domine vraiment.

### 3. Prix moyen selon la note
![Prix moyen par note](outputs/graphs/03_prix_moyen_par_note.png)

Les barres ont des hauteurs très proches : le prix moyen est environ le même quelle que soit la note.

### 4. Prix de chaque livre selon sa note
![Prix vs note](outputs/graphs/04_prix_vs_note.png)

Les points sont répartis sur toute la hauteur du graphique pour chaque note. On trouve des livres chers et bon marché à toutes les notes.

## Conclusion

L'analyse montre que **le prix d'un livre ne dépend pas de sa note**. Les livres bien notés ne sont ni plus chers ni moins chers que les autres, et les notes sont réparties de façon équilibrée dans le catalogue. Pour un client, la note seule ne permet donc pas de deviner le prix, et le prix ne garantit pas la qualité perçue.

## Lancer le projet

1. Installer les bibliothèques :
```
pip install pandas matplotlib seaborn
```
2. Lancer le script :
```
python visualisation.py
```
Les graphiques s'affichent et sont enregistrés dans `outputs/graphs/`.

## Auteur

Doou - Stagiaire Data Analytics chez CodeAlpha