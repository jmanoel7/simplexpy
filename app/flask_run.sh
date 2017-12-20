#!/bin/bash
set -e
source "${SIMPLEXPY_CONFIG:-../config}/bashrc"
workon simplexpy
cd "${SIMPLEXPY_APP:-.}"
FLASK_APP=simplex.py \
    flask run --host 0.0.0.0 --port 80
exit 0
