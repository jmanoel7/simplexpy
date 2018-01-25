#!/bin/sh
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
workon simplexpy
export FLASK_APP=webapp.py
exec flask run --host 127.0.0.1 --port 5000
