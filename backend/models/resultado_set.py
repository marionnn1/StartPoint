from database.db import db

class ResultadoSet(db.Model):
    __tablename__ = 'resultados_sets'
    id = db.Column(db.Integer, primary_key=True)
    partido_id = db.Column(db.Integer, db.ForeignKey('partidos.id'), nullable=False)
    numero_set = db.Column(db.Integer, nullable=False) # 1, 2 o 3
    juegos_p1 = db.Column(db.Integer, nullable=False)
    juegos_p2 = db.Column(db.Integer, nullable=False)