from models.jugador import Jugador
from database.db import db
from werkzeug.security import generate_password_hash

class JugadorService:
    @staticmethod
    def crear_jugador(datos):
        # Encriptamos la contraseña antes de guardarla
        password_encriptada = generate_password_hash(datos['password'])
        
        nuevo_jugador = Jugador(
            alias=datos['alias'],
            nombre_completo=datos['nombre_completo'],
            email=datos['email'],
            password=password_encriptada,
            posicion_en_pista=datos.get('posicion_en_pista', 'Ambos')
        )
        
        db.session.add(nuevo_jugador)
        db.session.commit()
        return nuevo_jugador

    @staticmethod
    def obtener_todos():
        return Jugador.query.all()