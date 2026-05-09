from database.db import db

class Pareja(db.Model):
    __tablename__ = 'parejas'
    id = db.Column(db.Integer, primary_key=True)
    jugador_1_id = db.Column(db.Integer, db.ForeignKey('jugadores.id'), nullable=False)
    jugador_2_id = db.Column(db.Integer, db.ForeignKey('jugadores.id'), nullable=False)
    alias_pareja = db.Column(db.String(100), nullable=True)
    puntos_pareja = db.Column(db.Integer, default=0)

    # Relaciones para acceder fácil a los nombres de los jugadores
    jugador_1 = db.relationship('Jugador', foreign_keys=[jugador_1_id])
    jugador_2 = db.relationship('Jugador', foreign_keys=[jugador_2_id])