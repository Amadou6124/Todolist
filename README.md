ToDoList Project
Une application web de gestion de tâches (ToDoList) développée avec Django pour le back-end, HTML et Bootstrap pour le front-end, et PostgreSQL comme base de données.


Fonctionnalités
Authentification utilisateur : Se connecter ou s’inscrire pour accéder à l’application.
Gestion des tâches :
Ajouter une tâche
Modifier une tâche
Supprimer une tâche
Interface responsive grâce à Bootstrap.
Base de données PostgreSQL pour un stockage fiable et évolutif.



Clonage du depot 
git clone https://github.com/Amadou6124/Todolist/
cd src

python -m venv .env

sous windows
.env\Scripts\activate

sous macOS ou linux
source .env/bin/activate


pip install -r requirements.txt

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todolist_db',
        "USER": 'sy',
        'PASSWORD': 'Alhamdoulilah100%',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

python manage.py migrate
python manage.py runserver

