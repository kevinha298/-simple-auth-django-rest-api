# django-postgres-docker
A shell of docker with django and postgresql containers for building other apps on.


1) Open git bash from local repository directory

2) Clone project from remote git to local repositorydirectory:
git clone https://github.com/kevinha298/django-postgres-docker.git

3) Open project in vs code:
code .

4) Open first terminal session in vs code to build container image:
docker-compose up

5) Once the image is built from the session above, open second terminal session in vs code to migrate Django models to Postgresql database:
docker-compose run app python manage.py migrate

6) On the second terminal session in vs code, stop the containers and rebuild image containers:
docker-compose down
docker-compose build

7) On the second terminal session in vs code, start the containers:
docker-compose up

8) Test django default site:
http://127.0.0.1:8000/


9) Open another terminal session for the following instructions (get into the app service of the django_app container to create a super user).
docker-compose exec app sh

10) Once inside the app service of the django_app container, create a super user and enter username, email address, and password
python manage.py createsuperuser


11) Go to admin site to test:
http://127.0.0.1:8000/admin

12) Enter username and password for admin to test

13) To rebuild image created above after making any change to the containers in the docker-compose.yml file:
docker-compose build


