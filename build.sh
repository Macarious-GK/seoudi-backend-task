#!/usr/bin/env bash
# exit on error
set -o errexit

pip install django
pip install pipfile
pip install djangorestframework
pip install django-debug-toolbar
pip install djangorestframework-xml
pip install bleach
pip install django-filter
pip install djoser

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
