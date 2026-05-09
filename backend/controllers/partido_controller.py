from flask import Blueprint, request, jsonify
from database.db import db
from services.partido_service import PartidoService

partido_bp = Blueprint('partido_bp', __name__)

@partido_bp.route('/partidos', methods=['POST'])
def registrar_partido():
    datos = request.get_json()
    try:
        partido = PartidoService.registrar_resultado(datos)
        return jsonify({
            "message": "Resultado guardado y puntos repartidos con éxito", 
            "partido_id": partido.id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400