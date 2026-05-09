from flask import Flask
from config import Config
from database.db import db
from models import *
from controllers.jugador_controller import jugador_bp
from controllers.liga_controller import liga_bp
from controllers.pareja_controller import pareja_bp
from controllers.partido_controller import partido_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        # Verifica y crea las tablas en StartPoint
        db.create_all()
        print("--- Base de Datos StartPoint: Lista y actualizada ---")

    # Registro de todas las rutas de la API
    app.register_blueprint(jugador_bp, url_prefix='/api')
    app.register_blueprint(liga_bp, url_prefix='/api')
    app.register_blueprint(pareja_bp, url_prefix='/api')
    app.register_blueprint(partido_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)