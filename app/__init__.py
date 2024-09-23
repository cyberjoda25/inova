#Este archivo inicializa la aplicación Flask, cargando la configuración y registrando las rutas.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    # Cargar las variables de entorno
    load_dotenv()

    # Crear la aplicación Flask
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config.from_object('app.config.Config')

    # Inicializar las extensiones
    db.init_app(app)

    # Registrar las rutas
    from .routes import perfil_bp
    app.register_blueprint(perfil_bp)

    # Crear las tablas si no existen
    with app.app_context():
        db.create_all()

    return app
