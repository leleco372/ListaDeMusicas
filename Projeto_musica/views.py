from flask import render_template, request, redirect, session, flash, url_for
from models import Musica, Usuario
from musica import db, app
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
    musica_existente = Musica.query.filter_by(nome=nome).first()
    if musica_existente:
        flash(f"música escrita ( {musica_existente.nome}) já  está cadastrada")
        return redirect(url_for('cadastrarMusica'))
        

    elif nome != "":
        db.session.add(novaMusica)
        db.session.commit()
        return redirect(url_for('listarMusicas'))

    else:
        return redirect(url_for('cadastrarMusica'))
@app.route('/editar')
def editar():
    if "usuario_logado" not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    
    return render_template('editar_musica.html', titulo='Editar música')

@app.route('/atualizar')
def atualizar():
    pass




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