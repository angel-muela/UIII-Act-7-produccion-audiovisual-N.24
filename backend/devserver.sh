#!/bin/sh
source .venv/bin/activate
python backend_produccionaudiovisual24/manage.py runserver --noreload $PORT
