from flask import Flask
from flask_cors import CORS  # Importar CORS
from controllers.controller import Controller

app = Flask(__name__)
CORS(app)  # Habilitar CORS para toda la aplicación

controller = Controller()

@app.route('/', methods=['GET', 'POST'])
def index():
    return controller.index()

@app.route('/nota/<codigo>', methods=['GET'])
def nota(codigo):
    return controller.nota(codigo)

@app.route('/notas', methods=['GET'])
def lista_notas():
    return controller.lista_notas()

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return controller.pagina_no_encontrada(error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

