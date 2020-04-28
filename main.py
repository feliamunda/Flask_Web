from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    print('Carga el index')
    name = 'Voldi'
    is_premium = False
    courses = ['Python', 'HTML', 'CSS', 'Java']
    return render_template('index.html',username=name,
                                        is_premium=is_premium,
                                        courses=courses
                                        )

@app.before_request
def before_index():
    print('Antes de cargar el index')

@app.after_request
def after_index(response):
    print('Despues de cargar el index')
    return response

@app.route('/about')
def about():
    return 'About'

@app.route('/saludo/<name>')
def saludo(name):
    return '<h1>Hola! ' + name + '</h1>'

if __name__ == '__main__':
    app.run(debug=True)
