from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    termino = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(200), nullable=False)
    term_es = db.Column(db.Text, nullable=False)
    term_en = db.Column(db.Text, nullable=False)
    term_fr = db.Column(db.Text, nullable=False)
    ejemplo1_es = db.Column(db.Text, nullable=True)
    ejemplo1_en = db.Column(db.Text, nullable=True)
    ejemplo1_fr = db.Column(db.Text, nullable=True)
    ejemplo2_es = db.Column(db.Text, nullable=True)
    ejemplo2_en = db.Column(db.Text, nullable=True)
    ejemplo2_fr = db.Column(db.Text, nullable=True)
    fuente = db.Column(db.String(400), nullable=True)
    observacion = db.Column(db.Text, nullable=True)