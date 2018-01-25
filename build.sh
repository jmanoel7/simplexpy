#!/bin/sh
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv -p /usr/bin/python3.5 simplexpy
workon simplexpy
pip3.5 install -U -r requirements.txt
#transcrypt -b 
