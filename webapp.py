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
        sp.otimizar = request.form['otimizacao']
        return redirect(url_for('vars_decisao'))
    return render_template('otimizacao.html')


@app.route('/vars_decisao', methods=['GET', 'POST'])
def vars_decisao():
    if request.method == 'POST':
        if (int(request.form['vars_decisao']) <= 0):
            return render_template('vars_decisao.html')
        sp.vars_decisao = int(request.form['vars_decisao'])
        return redirect(url_for('funcao_z'))
    return render_template('vars_decisao.html')

@app.route('/funcao_z', methods=['GET', 'POST'])
def funcao_z():
    if request.method == 'POST':
        sp.tabela = [[]]
        sp.tabela[0].append(1.0)
        for i in range(sp.vars_decisao):
            try:
                sp.tabela[0].append(-1.0 * float(request.form['funcao_z_'+str(i)]))
            except ValueError:
                return render_template('funcao_z.html', vars_decisao=range(sp.vars_decisao))
        # print (sp)
        return redirect(url_for('qtde_restricoes'))
    return render_template('funcao_z.html', vars_decisao=range(sp.vars_decisao))

@app.route('/qtde_restricoes', methods=['GET', 'POST'])
def qtde_restricoes():
    if request.method == 'POST':
        if (int(request.form['qtde_restricoes']) <= 0):
            return render_template('qtde_restricoes.html')
        for i in range(int(request.form['qtde_restricoes'])):
            sp.tabela.append(list())
        # print (sp)
        return redirect(url_for('restricoes'))
    return render_template('qtde_restricoes.html')

@app.route('/restricoes', methods=['GET', 'POST'])
def restricoes():
    if request.method == 'POST':
        try:
            for i in range(len(sp.tabela) - 1):
                for j in range(sp.vars_decisao + 1):
                    sp.tabela[i+1].append(float(request.form['restricao_'+str(i)+str(j)]))
        except ValueError:
            return render_template('restricoes.html', vars=range(sp.vars_decisao + 1), restricoes=range(len(sp.tabela) - 1))
        for i in range(len(sp.tabela) - 1):
            # Maior ou Igual
            if request.form['equacao_'+str(i)] == '1':
                for j in range(len(sp.tabela)):
                    if j == 0:
                        sp.tabela[j].append(0.0)
                    elif j == i + 1:
                        sp.tabela[j].insert(-1, -1.0)
                    else:
                        sp.tabela[j].insert(-1, 0.0)
            # Menor ou Igual
            elif request.form['equacao_'+str(i)] == '2':
                for j in range(len(sp.tabela)):
                    if j == 0:
                        sp.tabela[j].append(0.0)
                    elif j == i + 1:
                        sp.tabela[j].insert(-1, +1.0)
                    else:
                        sp.tabela[j].insert(-1, 0.0)
        sp.tabela[0].append(0.0)
        for i in range(len(sp.tabela) - 1):
            sp.tabela[i+1].insert(0, 0.0)
        print (sp)
        return redirect(url_for('solucao'))
    return render_template('restricoes.html', vars=range(sp.vars_decisao + 1), restricoes=range(len(sp.tabela) - 1))

@app.route('/solucao')
def solucao():
    return render_template('solucao.html', vars=sp.solucao())


