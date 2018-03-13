#!/bin/sh
sudo apt install \
	python2.7 \
	python2.7-dbg \
	python2.7-dev \
	python2.7-doc \
	python2.7-examples \
	python2.7-minimal \
	python3.5 \
	python3.5-dbg \
	python3.5-dev \
	python3.5-doc \
	python3.5-examples \
	python3.5-minimal \
	python3.5-venv \
	virtualenv \
	virtualenv-clone \
	virtualenvwrapper
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv -p /usr/bin/python3.5 simplexpy
workon simplexpy
pip3.5 install -U -r requirements.txt
