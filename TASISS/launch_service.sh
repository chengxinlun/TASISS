#!/bin/sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 45.33.62.211:443
