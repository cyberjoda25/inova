#Define los modelos (estructuras de las tablas) en este archivo. 
# Aquí mantendremos los modelos en este caso PerfilCargo.

from . import db

class PerfilCargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    departamento = db.Column(db.String(50), nullable=False)
    reporta_a = db.Column(db.String(50), nullable=False)
    supervisa = db.Column(db.String(50), nullable=True)
    ciudad = db.Column(db.String(50), nullable=False)
    teletrabajo = db.Column(db.Boolean, default=False)
    direccion = db.Column(db.String(100), nullable=False)