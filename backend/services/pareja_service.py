from models.pareja import Pareja
from database.db import db

class ParejaService:
    @staticmethod
    def crear_pareja(datos):
        nueva_pareja = Pareja(
            jugador_1_id=datos['jugador_1_id'],
            jugador_2_id=datos['jugador_2_id'],
            alias_pareja=datos.get('alias_pareja', None)
        )
        db.session.add(nueva_pareja)
        db.session.commit()
        return nueva_pareja