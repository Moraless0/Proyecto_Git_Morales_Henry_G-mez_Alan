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

def listar_productos():



    try:
        with open("data/productos.json", "r") as archivo:
            datos = json.load(archivo) 
    except:
        datos = []

    if len(datos) == 0:
        print("ERROR: No hay productos")
        regresar = input("Presione ENTER regresar...")
        if regresar != "":
            print("ERROR: Presione ENTER")
        else:
            return

    contador = 1

    for producto in datos:
        nombre = producto["nombre"]
        descripcion = producto["descripcion"]
        precio = producto["precio"]
        tostado = producto["tostado"]
        cantidad = producto["cantidad"]

        print("-"*30)
        print(f"-> PRODUCTO {contador}:")
        print(f"NOMBRE: {nombre}")
        print(f"DESCRIPCIÓN: {descripcion}")
        print(f"PRECIO: {precio}")
        print(f"NIVEL DE TOSTADO: {tostado}")
        print(f"CANTIDAD: {cantidad}")
        contador += 1