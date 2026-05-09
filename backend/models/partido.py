from database.db import db
from datetime import datetime

class Partido(db.Model):
    __tablename__ = 'partidos'
    id = db.Column(db.Integer, primary_key=True)
    liga_id = db.Column(db.Integer, db.ForeignKey('ligas.id'), nullable=False)
    pareja_1_id = db.Column(db.Integer, db.ForeignKey('parejas.id'), nullable=False)
    pareja_2_id = db.Column(db.Integer, db.ForeignKey('parejas.id'), nullable=False)
    fecha_hora = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.Enum('Programado', 'Finalizado'), default='Programado')
    ganador_id = db.Column(db.Integer, db.ForeignKey('parejas.id'), nullable=True)

    # Relación con los resultados de los sets
    resultados = db.relationship('ResultadoSet', backref='partido', lazy=True)