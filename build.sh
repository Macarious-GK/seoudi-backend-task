#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv install

python manage.py  --no-input