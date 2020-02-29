import pandas as pd
from flask import Flask, render_template
import manipuladatos



#Carga el padron nacional en una varialble llamada miPadronm se utiliza el ISO para poder utilizar los difentes unicodes.
Padron = pd.read_csv('./Data/PADRON_COMPLETO.csv',encoding='ISO-8859-1')
Distrito = pd.read_csv('./Data/Distelec.csv',encoding='ISO-8859-1')

manipuladatos.agregaColumnas(Padron,Distrito)


app = Flask(__name__) #this

"""Metodos HTTP CON LOS QUE ME COMUNICO
CON LA WEB, POR MEDIO DE ATTRIBUTOS, USANDO
EL URL SIEMPRE."""

@app.route("/")
def index():
    manipuladatos.agregaColumnas(Padron,Distrito)
    return render_template('home.html')



@app.route("/about")
def acercade():
    return render_template('about.html')

@app.route('/xSexo', methods=("POST", "GET"))
def ListadoxSexo():
    votaxSexo = manipuladatos.votantesPorSexo(Padron)
    return render_template('xSexo.html',  table=[votaxSexo])  


if __name__ == '__main__':
    app.run()


