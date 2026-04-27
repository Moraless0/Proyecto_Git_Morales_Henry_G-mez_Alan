import json

def agregar_producto():

    nombre = input("Ingrese el nombre del cafe :")
    descripcion = input("Ingrese una breve descripcion del cafe :")
    precio = float(input("Ingrese el precio :"))
    tostado = input("Ingrese el nivel de tostado (ligero, medio, oscuro) :")
    cantidad = int(input("Ingrese la cantidad del producto :"))

    cafe = {
        "nombre" : nombre,
        "descripcion" : descripcion,
        "precio" : precio,
        "tostado" : tostado,
        "cantidad" : cantidad
    }

    try:
        with open("data/productos.json", "r") as archivo:
            datos = json.load(archivo)

    except:
        datos = []

    datos.append(cafe)

    with open("data/productos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Cafe registrado correctamente ")