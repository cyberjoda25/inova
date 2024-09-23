#Este archivo contiene la configuración de la base de datos y cualquier otra configuración que sea necesaria.

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False