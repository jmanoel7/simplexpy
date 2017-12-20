# -*- coding: utf-8 -*-


from flask import abort, Response, Flask, render_template, redirect, url_for
from os import path, getenv


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home') #GET/POST
def home():
    return '''
    '''


@app.route('/vars/decisao') #GET/POST
    return render_template()
