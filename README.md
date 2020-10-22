# blog_app
Simple blog backend

## Installation Guide
1\. Clone the repo:
> $ git clone https://github.com/Ineshin-exe/blog_app.git

2\. Set your parameters in follow files:
- "docker-compose.yml"
- "./blog_app/.env"

3\. Build and up with docker-compose:
> $ docker-compose up -d --build

4\. Database's migrations:
> $ docker-compose exec web python manage.py makemigrations 

> $ docker-compose exec web python manage.py migrate

5\. Create superuser:
App requires login to access to all pages. Create superuser and register new users.

> $ docker-compose exec web python manage.py createsuperuser
