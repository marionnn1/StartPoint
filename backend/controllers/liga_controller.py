from flask import Blueprint, request, jsonify
from services.liga_service import LigaService

liga_bp = Blueprint('liga_bp', __name__)

@liga_bp.route('/ligas', methods=['POST'])
def crear_liga():
    datos = request.get_json()
    nueva = LigaService.crear_liga(datos)
    return jsonify({"message": "Liga creada", "id": nueva.id}), 201

@liga_bp.route('/ligas', methods=['GET'])
def listar_ligas():
    ligas = LigaService.obtener_ligas()
    return jsonify([{"id": l.id, "nombre": l.nombre} for l in ligas]), 200