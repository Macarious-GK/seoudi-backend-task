#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv shell
pipenv install

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
