#não quero inportar tudo da biblioteca flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/musicas')
def listarMusicas():

    lista = ["despacito", "shape of you", "bad guy", "blinding lights", "rockstar"]
    return render_template('lista_musicas.html', titulo="Leandro aprendendo do zero", musicas= lista)

if __name__ == '__main__':
    app.run(debug=True, port=5001)