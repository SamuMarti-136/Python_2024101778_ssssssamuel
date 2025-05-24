clientes_registrados = {"2126550"}

def verificar_cliente(ci):
    if ci in cliente_registrados:
        return {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci
        }
    else:
        return {
            "accion": "cliente no esta en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }