from flask import Flask, request, jsonify
from cliente import verificar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def verificar_cliente_route():
    ci = request.json.get('ci')

    codRes, menRes, accion = procesar_verificacion(ci)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'ci': ci,
        'accion': accion
    }
    return jsonify(salida)

def procesar_verificacion(ci):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    accion = ''

    try:
        if not ci:
            accion = "Datos incorrectos"
            codRes = "ERROR"
            menRes = "No se recibió la cédula"
        else:
            resultado = verificar_cliente(ci)
            accion = resultado.get('accion', 'Sin acción')
            codRes = resultado.get('codRes', codRes)
            menRes = resultado.get('menRes', menRes)
    except Exception as e:
        print("ERROR:", str(e))
        accion = "Error interno"
        codRes = "ERROR"
        menRes = f"Msg: {str(e)}"

    return codRes, menRes, accion

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5004)
