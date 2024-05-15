
# Django on Docker (Development Environment)

This repository demonstrates how to Dockerize a Django project along with configuring it to use PostgreSQL as the database.

## Dependencies
- Django v4.2.3
- Docker v24.0.2
- Python v3.11.4

## Django on Docker Series

### Dockerizing Django with Postgres
#### Project Setup
1. Create a new project directory along with a new Django project:
    ```
    $ mkdir django-on-docker && cd django-on-docker
    $ mkdir app && cd app
    $ python3.11 -m venv env
    $ source env/bin/activate
    (env)$ pip install django==4.2.3
    (env)$ django-admin startproject projectName .
    (env)$ python manage.py migrate
    (env)$ python manage.py runserver
    ```
2. Navigate to http://localhost:8000/ to view the Django welcome screen. Kill the server once done.

3. Create a `requirements.txt` file in the "app" directory and add Django as a dependency:
    ```
    Django==4.2.3
    ```

4. Remove the `db.sqlite3` file from the "app" directory.

### Docker
1. Install Docker if not already installed, then add a `Dockerfile` to the "app" directory.

2. Add a `docker-compose.yml` file to the project root.

### Postgres
1. Add a new service called `db` to `docker-compose.yml`.

2. Update the Django settings and install Psycopg2.

3. Add an `entrypoint.sh` file to the "app" directory.

## Usage

1. Build the Docker image:
    ```
    $ docker-compose build
    ```

2. Run the container:
    ```
    $ docker-compose up -d
    ```

3. Navigate to http://localhost:8000/ to view the Django welcome screen.

4. For any errors, check the logs using:
    ```
    $ docker-compose logs -f
    ```

5. To access PostgreSQL, use:
    ```
    $ docker-compose exec db psql --username=projectName --dbname=projectName_dev
    ```
6. Run the migrations:
   
    ```
    $ docker-compose exec web python manage.py migrate --noinput
    ```
## Environment Variables
Ensure to set the following environment variables in `.env.dev`:
- `DEBUG=1`
- `SECRET_KEY=foo`
- `DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]`
- `SQL_ENGINE=django.db.backends.postgresql`
- `SQL_DATABASE=projectName_dev`
- `SQL_USER=projectName`
- `SQL_PASSWORD=projectName`
- `SQL_HOST=db`
- `SQL_PORT=5432`
- `DATABASE=postgres`


### Makefile Commands:

- **`make all`**: Cleans up, builds the services, and starts them.
- **`make clean`**: Stops and removes containers, networks, volumes, and images.
- **`make build`**: Builds the Docker services defined in the docker-compose.yml file.
- **`make up`**: Starts the Docker services in detached mode.
