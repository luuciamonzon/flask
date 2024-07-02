from flask import Flask, render_template

app = Flask(__name__)
personas_list = ('Pablo', 'Juan', 'Maria')

personas_dict= [
    dict(
    nombre= 'Pablo',
    edad= 27,
    pais= 'Argentina',
    ),
    dict(
    nombre= 'Ana',
    edad= 30,
    pais= 'Chilena',
    ),
    dict(
    nombre= 'Juan',
    edad= 40,
    pais= 'Argentino',
    ),
]

@app.route('/') # app es la instancia, route el metodo, '/' es el disparador
def index():
    return render_template(
        'index.html',
    )

@app.route('/info') # app es la instancia, route el metodo, '/' es el disparador
def informacion():
    return render_template(
        'informacion.html',
    )

@app.route('/bienvenido/<nombre>')
def bienvenida(nombre):
    return render_template(
        'bienvenida.html',
    )

@app.route('/personas') # app es la instancia, route el metodo, '/' es el disparador
def personas():
    listado_de_personas = personas_list
    return render_template(
        'personas.html',
        personas = listado_de_personas,
        diccionario_personas = personas_dict,
    )