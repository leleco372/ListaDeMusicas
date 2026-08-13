#não quero inportar tudo da biblioteca flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/musicas')
def listaMusicas():
    return render_template('lista_musicas.html', titulo="Aprendendo do inicio")

if __name__ == '__main__':
    app.run(debug=True, port=5001)