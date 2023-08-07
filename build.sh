#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv install

python manage.py runserver
python manage.py makemigrations
python manage.py migrate
