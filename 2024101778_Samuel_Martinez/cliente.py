from flask import Blueprint, request, jsonify # type: ignore

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamaServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')

    codRes, menRes, accion = inicializarVariables(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': user,
        'accion': accion
    }
    return jsonify(salida)

def inicializarVariables(ci):
    clientesRegistrados = ["6522920"]
    codRes = 'SIN_ERROR'
    menRes = 'OK'

    try:
        print("Verificando cliente...")
        if ci in clientesRegistrados:
            print("Cliente encontrado")
            accion = "Success"
        else:
            print("Cliente no encontrado")
            accion = "Cliente no esta en el sistema"
            codRes = 'ERROR'
            menRes = 'Credenciales incorrectas'


    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, accion
