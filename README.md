
1. Cloner le projet
```
git clone https://github.com/erraguibiabdelilah/api_challeng.git
cd api_challeng
```
2. Créer et activer un environnement virtuel
```
python3 -m venv env
source env/bin/activate
```
3. Installer les dépendances
```
pip install django
pip install djangorestframework
pip install psycopg2-binary
pip install drf-yasg
```
4. Configuration de la base de données PostgreSQL dans settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nom_de_la_base',
        'USER': 'mon_user',
        'PASSWORD': 'mon_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
5. Appliquer les migrations
```
python manage.py makemigrations
python manage.py migrate
```
6. Lancer le serveur Django
```
python manage.py runserver
```

Accéder au projet via :
=> http://127.0.0.1:8000/


Swagger UI :
=> http://127.0.0.1:8000/swagger/

redoc UI :
=> http://127.0.0.1:8000/redoc/