from models.liga import Liga
from database.db import db

class LigaService:
    @staticmethod
    def crear_liga(datos):
        nueva_liga = Liga(
            nombre=datos['nombre'],
            puntos_victoria=datos.get('puntos_victoria', 3),
            puntos_participacion=datos.get('puntos_participacion', 1)
        )
        db.session.add(nueva_liga)
        db.session.commit()
        return nueva_liga

    @staticmethod
    def obtener_ligas():
        return Liga.query.all()