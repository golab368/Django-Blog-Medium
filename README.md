# Django-Blog-Medium

Django blog CRUD app with features of blog platform.


# General info

An Open-Source Django blog app based on a Medium blog platform.

# Project is available also on HEROKU 

https://django-medium.herokuapp.com/

# Features

- User Login
- Common Tag List
- Comments
- Acount Followers
- Responsive on all devices
- Pagination
- Clean Code
- 77% test coverage

# Technologies

- Python 3.9.10
- Django 3
- Bootstrap
- SQLite for tests 
- PostgreSQL for Heroku 

# Setup

1. Requirements


  - Text Editor or IDE (eg. vscode, PyCharm)

  - Python 3.9 +

  - Django

2. Install Python and Pipenv

  - Python3

  - Pipenv

3. Local Setup and Running on Windows, Linux and Mac OS

4. 
  - Install package with pip or pipenv
  
  ```
      $ pip install Django-Blog-Medium
   
  ```
  
               or 
  ```
      $ pipenv install Django-Blog-Medium
   
  ```             
  - Add crispy_forms, taggit to your INSTALLED_APPS in settings.py:

   ```
    INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'crispy_forms',
      'blog',
      'taggit',

  ]
 ```



  - Add configuration to urls.py of project:
   ```
   urlpatterns = [
      path('admin/', admin.site.urls),
      path("", include("blog.urls")),
  ]
```
        
  - Create blog database tables

  - python3 manage.py makemigrations blog
  - python3 manage.py migrate
  - Optional python3 manage.py createsuperuser
  
# Screenshots

<picture>
  <img alt="" src="https://i.ibb.co/XyzTgdM/rsz-1.jpg">
</picture>
<picture>
  <img alt="" src="https://i.ibb.co/QMRCGNh/rsz-2.jpg">
</picture>
