# -*- coding: utf-8 -*-


from flask import abort, Response, Flask, render_template, \
    redirect, url_for, request
from os import path, getenv
from simplex import Simplex

app = Flask(__name__)
sp = Simplex()

@app.route('/')
def index():
    return redirect(url_for('otimizacao'))

@app.route('/otimizacao', methods=['GET', 'POST'])
def otimizacao():
    if request.method == 'POST':
        sp.otimizar(request.form['otimizacao'])
        return redirect(url_for('vars_decisao'))
    return render_template('otimizacao.html')


@app.route('/vars/decisao', methods=['GET', 'POST'])
def vars_decisao():
    if request.method == 'POST':
        sp.vars_decisao(request.form['vars_decisao'])
        return redirect(url_for('funcao_z'))
    return render_template('vars_decisao.html')
