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
from  views import *

if __name__ == '__main__':
    app.run(debug=True, port=5001)