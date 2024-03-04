from Lista import Lista
Listan = Lista()

def mostrar_menu():
    print("1. Mostrar la lista")
    print("2. Agregar un nodo a la lista")
    print("3. Salir")
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    return opcion

def main():

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            print("Lista actual:")
            Lista.imprimir()
        elif opcion == "2":
            valor = input("Ingrese el valor del nodo a agregar: ")
            Listan.agregar(valor)
            print("Nodo agregado exitosamente.")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")