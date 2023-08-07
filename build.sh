#!/usr/bin/env bash
# exit on error
set -o errexit

pip install pipenv

pipenv shell

pipenv install django
pipenv install pipfile
pipenv install djangorestframework
pipenv install django-debug-toolbar
pipenv install djangorestframework-xml
pipenv install bleach
pipenv install django-filter
pipenv install djoser

# python manage.py makemigrations
# python manage.py migrate
python manage.py runserver
