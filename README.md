[django_postgres_docker_instructions.txt](https://github.com/kevinha298/django-postgres-docker/files/7073074/django_postgres_docker_instructions.txt)
# django-postgres-docker
A shell of docker with django and postgresql containers for building other apps on.


# Open git bash from local repository directory

# Clone project from git to local repositorydirectory:
git clone https://github.com/kevinha298/django-postgres-docker.git

# Open open project in vs code:
code .

# Create djangoapp folder at the root of the project to store Django files

# Create pgdb folder at the root of the project to store Postgresql data

# Build an image for the first time:
docker-compose run --rm app sh -c "django-admin startproject MainApp ."

# Start up docker-compose:
docker-compose up

# Test django default site:
http://127.0.0.1:8000/

# Stop docker-compose:
docker-compose down


# Delete db.sqlite3 file in the djangoapp folder

# Replace "DATABASES" section in the ./djangoapp/MainApp/settings.py file with the following.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

# Add "'rest_framework'," in the "INSTALLED_APPS" section of the ./djangoapp/MainApp/settings.py file.

# In the ./djangoapp/MainApp/settings.py file do the followings:
-- Add "import os" on the top
-- Update "SECRET_KEY" variable as:
    SECRET_KEY = os.environ.get('SECRET_KEY')
-- Update "DEBUG" variable as:
    DEBUG = bool(int(os.environ.get('DEBUG', 0)))
-- Add "ALLOWED_HOSTS" variable as:
    ALLOWED_HOSTS.extend(
        filter(
            None,
            os.environ.get('ALLOWED_HOSTS', '').split(','),
        )
    )

# Migrate django objects and connect to postgresql database
docker-compose run app python manage.py migrate

# Start up docker-compose:
docker-compose up

# Open another terminal session for the following instructions (get into the app service of the django_app container to create a super user).
docker-compose exec app sh

python manage.py createsuperuser

# Enter username

# Enter user email address

# Enter user password

# Go to admin site
http://127.0.0.1:8000/admin

# Enter username and password for admin to test

# To rebuild image created above after making some changes:
docker-compose build


