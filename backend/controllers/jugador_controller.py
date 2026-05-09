from flask import Blueprint, request, jsonify
from services.jugador_service import JugadorService

# Creamos un "Blueprint" para agrupar las rutas de jugadores
jugador_bp = Blueprint('jugador_bp', __name__)

@jugador_bp.route('/jugadores', methods=['POST'])
def registrar_jugador():
    datos = request.get_json()
    try:
        nuevo = JugadorService.crear_jugador(datos)
        return jsonify({"message": "Jugador creado", "id": nuevo.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@jugador_bp.route('/jugadores', methods=['GET'])
def listar_jugadores():
    jugadores = JugadorService.obtener_todos()
    return jsonify([j.to_dict() for j in jugadores]), 200