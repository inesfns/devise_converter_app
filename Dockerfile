# Utilisez une image de base Python officielle.
FROM python:3.9-slim

# Définissez le répertoire de travail dans le conteneur.
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . .

# Commande pour installer les dépendances (s'il y en a)
RUN pip install -r requirements.txt

# Définissez la commande pour démarrer l'application.
CMD ["python", "app.py"]

