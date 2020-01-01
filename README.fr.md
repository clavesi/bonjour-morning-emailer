# Bonjour - Bulletin du Matin
Un bulletin qui vous envoie automatiquement par e-mail une liste de faits intéressants, une vidéo éducative de SciShow, une photo de la NASA et la nouvelle de Reuters.

*Lire ceci en: [English](README.md)*

## Comment Ça Marche
Le programme gratte le web pour:
- Un mot du jour
- La dernière vidéo de SciShow
- Un fait amusant
- Une personne née ce jour-là
- Une photo de la NASA
- Quelque chose qui s'est passé ce jour-là
- La nouvelle de Reuters

puis il met à jour une feuille de calcul et renvoie un e-mail avec toutes les informations

## Guide de Répertoire
- main.py (fichier principal pour tout exécuter)
- scraper.py (gratte le web pour toutes les infos)
- spreadsheet.py (remplit une feuille de calcul avec les informations de scraper.py)
- html_changer.py (modifier le fichier html pour l'envoyer par e-mail)
- email_server.py (envoie l'e-mail)
- settings.py (placez l'information d'e-mail et la fiche pour accéder)
- client_secret.json (vérifie et permet l'accès à la feuille de calcul)

### Mode d'emploi
1. Installer les [pilotes](https://selenium-python.readthedocs.io/installation.html) de selenium's
2. Débarrassez-vous de _sample dans les noms client_secret.json et settings.py
3. Activer l'API Google Drive and Sheets à partir de leur [console API](https://console.developers.google.com/apis/dashboard)
4. Créez des identifiants pour l'API Feuilles et collez-les dans client_secret.json
5. Remplir le fichier settings.py
6. Exécuter main.py

### Les progiciels
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [selenium](https://pypi.org/project/selenium/)
- [gspread](https://pypi.org/project/gspread/)
- [oauth2client](https://pypi.org/project/oauth2client/)
