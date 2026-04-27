import os

def mostrar_separadores():
    separador = "="*40
    if os.name == "nt":
        os.system("cls")
        print(separador)
    else:
        os.system("clear")
        print(separador)

def menu():
    while True:
        mostrar_separadores()
        print("     --- Cafetería AromaCampus ---")
        print("   1. Agregar Café")
        print("   2. Listar tipos de café")
        print("   3. Actualizar datos de un café")
        print("   4. Eliminar un tipo de café")
        print("   5. Salir...")
        opci = int(input("   Ingrese una opción: "))