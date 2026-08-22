from musica import db
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