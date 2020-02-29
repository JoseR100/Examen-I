
from flask import Flask, render_template


app = Flask(__name__) #this

"""Metodos HTTP CON LOS QUE ME COMUNICO
CON LA WEB, POR MEDIO DE ATTRIBUTOS, USANDO
EL URL SIEMPRE."""

@app.route("/")
def index():
    return render_template('home.html')



@app.route("/about")
def acercade():
    return render_template('about.html')


##@app.route("/estudiante", methods = ['GET', 'POST'])
##def estudiante():
##    return render_template('estudiante.html')

if __name__ == '__main__':
    app.run()


