# -*- coding: utf-8 -*-


from flask import abort, Response, Flask, render_template, \
    redirect, url_for, request
from os import path, getenv


app = Flask(__name__)
#sp = SimplexPy()

@app.route('/')
def index():
    return redirect(url_for('otimizacao'))

@app.route('/otimizacao', methods=['GET', 'POST'])
def otimizacao():
    if request.method == 'POST':
        # sp.init=(request.form['otimizar'])
        return redirect(url_for('index'))
    return render_template('otimizacao.html')


#@app.route('/vars/decisao', methods=['GET', 'POST'])
#    return render_template()
