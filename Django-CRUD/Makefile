.PHONY: all clean build up makemigrations migrate

all: clean build up migrate

clean:
	@echo "Cleaning up..."
	docker-compose down -v --remove-orphans

build:
	@echo "Building services..."
	docker-compose build

up:
	@echo "Starting services..."
	docker-compose up -d

migrate:
	@echo "Creating migrations..."
	docker-compose exec web python manage.py makemigrations
	@echo "Migrating database..."
	docker-compose exec web python manage.py migrate
createsuperuser:
	@echo "Creating superuser..."
	docker-compose exec web python manage.py createsuperuser
exec_postgres:
	@echo "Adding entry to the database..."
	docker exec -it djangodockerized_db_1 psql -U projectName -d projectName_dev