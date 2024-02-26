from Lista import LinkedList

class MainMenu:
    def _init_(self):
        self.linked_list = LinkedList()

    def display_menu(self):
        print("Menu:")
        print("1. Agregar dato a la lista")
        print("2. Otra opción")
        print("3. Otra opción")
        print("4. Otra opción")
        print("5. Salir")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Selecciona una opción: ")
            if choice == "1":
                data = input("Ingresa el dato que deseas agregar a la lista: ")
                self.linked_list.append(data)
                print("Dato agregado correctamente a la lista.")
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

if _name_ == "_main_":
    main_menu = MainMenu()
    main_menu.run()