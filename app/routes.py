#Las rutas actúan como controladores y se comunican con los servicios. Define todas las rutas en este archivo.

from flask import Blueprint, jsonify, request
from .services import agregar_perfil, obtener_perfiles, obtener_perfil_por_id, eliminar_perfil

perfil_bp = Blueprint('perfil_bp', __name__)

@perfil_bp.route('/perfil', methods=['POST'])
def crear_perfil():
    data = request.json
    agregar_perfil(data)
    return jsonify({'mensaje': 'Perfil de cargo creado con éxito'}), 201

@perfil_bp.route('/perfiles', methods=['GET'])
def listar_perfiles():
    perfiles = obtener_perfiles()
    resultado = [
        {
            'id': perfil.id,
            'nombre': perfil.nombre,
            'departamento': perfil.departamento,
            'reporta_a': perfil.reporta_a,
            'supervisa': perfil.supervisa,
            'ciudad': perfil.ciudad,
            'teletrabajo': perfil.teletrabajo,
            'direccion': perfil.direccion
        }
        for perfil in perfiles
    ]
    return jsonify(resultado)

@perfil_bp.route('/perfil/<int:id>', methods=['GET'])
def obtener_perfil(id):
    perfil = obtener_perfil_por_id(id)
    if not perfil:
        return jsonify({'mensaje': 'Perfil no encontrado'}), 404

    resultado = {
        'id': perfil.id,
        'nombre': perfil.nombre,
        'departamento': perfil.departamento,
        'reporta_a': perfil.reporta_a,
        'supervisa': perfil.supervisa,
        'ciudad': perfil.ciudad,
        'teletrabajo': perfil.teletrabajo,
        'direccion': perfil.direccion
    }
    return jsonify(resultado)

@perfil_bp.route('/perfil/<int:id>', methods=['DELETE'])
def eliminar_perfil_por_id(id):
    if eliminar_perfil(id):
        return jsonify({'mensaje': 'Perfil eliminado con éxito'}), 200
    return jsonify({'mensaje': 'Perfil no encontrado'}), 404