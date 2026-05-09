from models.partido import Partido
from models.resultado_set import ResultadoSet
from models.pareja import Pareja
from models.jugador import Jugador
from models.liga import Liga
from database.db import db

class PartidoService:
    @staticmethod
    def registrar_resultado(datos):
        # 1. Crear el registro del partido
        nuevo_partido = Partido(
            liga_id=datos['liga_id'],
            pareja_1_id=datos['pareja_1_id'],
            pareja_2_id=datos['pareja_2_id'],
            estado='Finalizado'
        )
        db.session.add(nuevo_partido)
        db.session.flush() 

        # 2. Guardar los sets y calcular ganador
        sets_p1 = 0
        sets_p2 = 0
        
        for i, s in enumerate(datos['sets']):
            nuevo_set = ResultadoSet(
                partido_id=nuevo_partido.id,
                numero_set=i + 1,
                juegos_p1=s['juegos_p1'],
                juegos_p2=s['juegos_p2']
            )
            db.session.add(nuevo_set)
            
            if s['juegos_p1'] > s['juegos_p2']:
                sets_p1 += 1
            else:
                sets_p2 += 1

        # 3. Determinar pareja ganadora
        id_ganadora = datos['pareja_1_id'] if sets_p1 > sets_p2 else datos['pareja_2_id']
        id_perdedora = datos['pareja_2_id'] if sets_p1 > sets_p2 else datos['pareja_1_id']
        nuevo_partido.ganador_id = id_ganadora

        # 4. Repartir puntos
        liga = Liga.query.get(datos['liga_id'])
        
        p_ganadora = Pareja.query.get(id_ganadora)
        p_perdedora = Pareja.query.get(id_perdedora)
        
        # Puntos a la tabla de Parejas
        p_ganadora.puntos_pareja += liga.puntos_victoria
        p_perdedora.puntos_pareja += liga.puntos_participacion

        # Puntos a los jugadores (AQUÍ ESTABA EL ERROR, cambiado 'en' por 'in')
        for j in [p_ganadora.jugador_1, p_ganadora.jugador_2]:
            j.puntos_individuales += liga.puntos_victoria
            
        for j in [p_perdedora.jugador_1, p_perdedora.jugador_2]:
            j.puntos_individuales += liga.puntos_participacion

        db.session.commit()
        return nuevo_partido