#!/bin/bash
set -e
source "${SIMPLEXPY_CONFIG:-.}/bashrc"
pip install -U pip
pip install -U setuptools
pip install -U virtualenvwrapper
exit 0
