#não quero inportar tudo da biblioteca flask
from flask import Flask, render_template, request, redirect, session, flash, url_for

from flask_sqlalchemy import SQLAlchemy

#self é como o this do java, ele referencia o objeto que está chamando o método
class Usuario:
    def __init__(self, nome, senha, gmail):
        self.nome=nome
        self.senha=senha
        self.gmail=gmail

usuario01=Usuario("Leandro", "admin", "leandro@exemplo.com")
usuario02=Usuario("João", "1234", "joao@exemplo.com")
usuario03=Usuario("Maria", "abcd", "maria@exemplo.com")

#criando um dicionário de usuários, onde a chave é o gmail e o valor é o objeto usuário
usuarios = {
    usuario01.gmail: usuario01,
    usuario02.gmail: usuario02,
    usuario03.gmail: usuario03
}


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

app.secret_key = "senhasupersecreta"


@app.route('/')
def listarMusicas():
    if  "usuario_logado" not in session or session["usuario_logado"] == None:
        return redirect(url_for('login'))
    return render_template('lista_musicas.html', musicas=lista, titulo="Lista de Músicas")

@app.route("/cadastrar_musicas")
def cadastrarMusica():
    if  "usuario_logado" not in session or session["usuario_logado"] == None:
        return redirect(url_for('login'))
    
    return render_template('cadastrar_musicas.html', titulo="Cadastrar Música")

@app.route("/adicionar", methods=["POST",])
def adicionarMusica():
    #recebendo os dados do formulário
    nome=request.form['txtNome']
    artista=request.form['txtArtista']
    genero=request.form['txtGenero']
    #inserindo os dados na nova música e adicionando na lista
    novaMusica=Musica(nome, artista, genero)
    if nome !="":
        lista.append(novaMusica)
        return redirect(url_for('listarMusicas'))
    else:
        return redirect(url_for('cadastrarMusica'))

@app.route("/login")
def login():
    return render_template('login.html', titulo="Login")

@app.route("/autenticar", methods=["POST",])
def autenticar():
    if request.form["txtUsuario"] in usuarios:
        usuarioEncontrado = usuarios[request.form["txtUsuario"]]
        if request.form["txtSenha"] == usuarioEncontrado.senha:
    #session é basicamende um divisor de águas, ele vai criar uma sessão para o usuário que está logando, e vai armazenar o nome do usuário na sessão. )
            session["usuario_logado"] = request.form["txtUsuario"]
            flash(f"usuário: {usuarioEncontrado.nome} logado com sucesso!")
            return redirect(url_for('listarMusicas'))
        else:
            flash("senha incorreta!")
            return redirect(url_for('login'))
    else: 
        flash("usuário ou senha incorretos!")
        return redirect(url_for('login'))

@app.route("/sair")
def sair():
    session["usuario_logado"] = None
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)