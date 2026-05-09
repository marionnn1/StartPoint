from database.db import db

class Liga(db.Model):
    __tablename__ = 'ligas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    puntos_victoria = db.Column(db.Integer, default=3)
    puntos_participacion = db.Column(db.Integer, default=1)
    esta_activa = db.Column(db.Boolean, default=True)