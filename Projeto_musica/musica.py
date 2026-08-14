#não quero inportar tudo da biblioteca flask
from flask import Flask, render_template, request, redirect
#self é como o this do java, ele referencia o objeto que está chamando o método

class Musica:
    def __init__(self, nome, artista, genero):
        self.nome=nome
        self.artista=artista
        self.genero=genero

musica01=Musica("despacito", "Luis Fonsi", "pop")
musica02=Musica("shape of you", "Ed Sheeran", "pop")
musica03=Musica("bad guy", "Billie Eilish", "pop")
musica04=Musica("blinding lights", "The Weeknd", "pop")
musica05=Musica("rockstar", "Post Malone", "hip-hop")

lista = [musica01, musica02, musica03, musica04, musica05]

app = Flask(__name__)


@app.route('/')
def listarMusicas():
    return render_template('lista_musicas.html', musicas=lista, titulo="Lista de Músicas")

@app.route("/cadastrar_musicas")
def cadastrarMusica():
    return render_template('cadastrar_musicas.html')

@app.route("/adicionar", methods=["POST",])
def adicionarMusica():
    #recebendo os dados do formulário
    nome=request.form['txtNome']
    artista=request.form['txtArtista']
    genero=request.form['txtGenero']
    #inserindo os dados na nova música e adicionando na lista
    novaMusica=Musica(nome, artista, genero)
    lista.append(novaMusica)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=5001)