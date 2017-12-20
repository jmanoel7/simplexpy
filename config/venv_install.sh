#!/bin/bash
set -e
source "${SIMPLEXPY_CONFIG:-.}/bashrc"
mkvirtualenv simplexpy
pip install -U -r "${SIMPLEXPY_CONFIG:-.}/requirements.txt"
exit 0
