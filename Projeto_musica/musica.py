from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)

# Carrega as configurações do arquivo config.py
app.config.from_object(Config)

# Só depois cria o SQLAlchemy
db = SQLAlchemy(app)

with app.app_context():
    db.engine.connect()
    
class Musica(db.Model):
    __tablename__ = 'musica'
    id  = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    artista = db.Column('cantor_banda', db.String(50), nullable=False)
    genero = db.Column(db.String(50), nullable=False)

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_usuario = db.Column(db.String(50), nullable=False)
    login_usuario = db.Column(db.String(20), nullable=False)
    senha_usuario = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome_usuario


@app.route('/')
def listarMusicas():
    if  "usuario_logado" not in session or session["usuario_logado"] == None:
        return redirect(url_for('login'))
    musicas = Musica.query.all()

    return render_template('lista_musicas.html', musicas=musicas, titulo="Lista de Músicas")

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
    novaMusica = Musica(
    nome=nome,
    artista=artista,
    genero=genero
)
    if nome !="":
        db.session.add(novaMusica)
        db.session.commit()
        return redirect(url_for('listarMusicas'))
    else:
        return redirect(url_for('cadastrarMusica'))

@app.route("/login")
def login():
    return render_template('login.html', titulo="Login")

@app.route("/autenticar", methods=["POST",])
def autenticar():

    usuario= Usuario.query.filter_by(login_usuario=request.form['txtLogin']).first()
    if usuario:
        if request.form["txtSenha"] == usuario.senha_usuario:
    #session é basicamende um divisor de águas, ele vai criar uma sessão para o usuário que está logando, e vai armazenar o nome do usuário na sessão. )
            session["usuario_logado"] = usuario.login_usuario
            flash(f"usuário: {usuario.login_usuario} logado com sucesso!")
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