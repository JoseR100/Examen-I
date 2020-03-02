
from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import manipuladatos


app = Flask(__name__)

#df = pd.read_csv('./Data/PADRON.csv',encoding='ISO-8859-1')


@app.route("/")
def index():
    return render_template('home.html')

@app.route('/disxprovincia', methods=("POST", "GET"))
def html_disxprovincia():
    df1 = pd.read_csv('./Data/Distelec.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnaDistrito(df1)
    df1 = manipuladatos.DistritoPorProvincia(df1)
    return render_template('disxprovincia.html',  tables=[df1.to_html(classes='data')], titles=df1.columns.values)


@app.route('/disxcanton', methods=("POST", "GET"))
def html_disxcanton():
    df1 = pd.read_csv('./Data/Distelec.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnaDistrito(df1)
    df1 = manipuladatos.DistritoPorCanton(df1)
    return render_template('disxcanton.html',  tables=[df1.to_html(classes='data')], titles=df1.columns.values)    

@app.route('/xSexo', methods=("POST", "GET"))
def html_xSexo():
    df1 = pd.read_csv('./Data/padron.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnas(df1)
    df1 = manipuladatos.votantesPorSexo(df1)
    return render_template('xSexo.html',  tables=[df1.to_html(classes='data')], titles=df1.columns.values) 

@app.route('/xProvincia', methods=("POST", "GET"))
def html_xProvinca():
    df1 = pd.read_csv('./Data/padron.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnas(df1)
    df1 = manipuladatos.votantesPorProvincia(df1)
    return render_template('xProvincia.html',  tables=[df1.to_html(classes='data')], titles=df1.columns.values) 

if __name__ == '__main__':
    app.run()

