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

def editar_producto():
    nombre_buscar = input("Ingrese el nombre del cafe a editar: ")

    try:
        with open("data/productos.json", "r") as archivo:
            datos = json.load(archivo)
    except:
        print("No hay datos.")
        return

    for cafe in datos:
        if cafe["nombre"] == nombre_buscar:
            cafe["descripcion"] = input("Nueva descripcion: ")
            cafe["precio"] = float(input("Nuevo precio: "))
            cafe["tostado"] = input("Nuevo tostado: ")
            cafe["cantidad"] = int(input("Nueva cantidad: "))

            with open("data/productos.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)

            print("Producto actualizado.")
            return

    print("Producto no encontrado.")

editar_producto()
