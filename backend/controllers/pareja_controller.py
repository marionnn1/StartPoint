from flask import Blueprint, request, jsonify
from services.pareja_service import ParejaService

pareja_bp = Blueprint('pareja_bp', __name__)

@pareja_bp.route('/parejas', methods=['POST'])
def crear_pareja():
    datos = request.get_json()
    try:
        nueva = ParejaService.crear_pareja(datos)
        return jsonify({"message": "Pareja formada correctamente", "id": nueva.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400