#Este archivo contiene las funciones que implementan la lógica de negocio. 
# Aquí es donde se realizan las operaciones CRUD relacionadas con los perfiles de cargo.

from .models import PerfilCargo
from . import db

def agregar_perfil(data):
    nuevo_perfil = PerfilCargo(
        nombre=data['nombre'],
        departamento=data['departamento'],
        reporta_a=data['reporta_a'],
        supervisa=data.get('supervisa', 'No aplica'),
        ciudad=data['ciudad'],
        teletrabajo=data.get('teletrabajo', False),
        direccion=data['direccion']
    )
    db.session.add(nuevo_perfil)
    db.session.commit()

def obtener_perfiles():
    perfiles = PerfilCargo.query.all()
    return perfiles

def obtener_perfil_por_id(id):
    return PerfilCargo.query.get(id)

def eliminar_perfil(id):
    perfil = PerfilCargo.query.get(id)
    if perfil:
        db.session.delete(perfil)
        db.session.commit()
        return True
    return False