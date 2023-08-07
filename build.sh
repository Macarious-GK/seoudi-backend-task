#!/usr/bin/env bash
# exit on error
set -o errexit

pip install Pipfile

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
