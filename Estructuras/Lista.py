from .Nodo import Nodo

class Lista:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato) # Creamos un nuevo nodo

        if self.primero == None: #Si la lista está vacía
            self.primero = nuevo

        else: # Si la lista no está vacía
            actual = self.primero # Obtenemos el primero de la lista
            while actual.siguiente != None: # Mientras el nodo actual tenga un nodo siguiente
                actual = actual.siguiente  # El nodo actual se mueve al siguiente
            actual.siguiente = nuevo # Se agrega el nodo
        self.size += 1

    def imprimir(self):
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato)
            actual = actual.siguiente

        print(actual.dato)

    def imprimirPersona(self):
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato.nombre, actual.dato.edad)
            actual = actual.siguiente

        print(actual.dato.nombre, actual.dato.edad)

    def buscar(self, codigoIngresado):
        actual = self.primero
        while actual != None:
            if actual.dato.codigo == codigoIngresado:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def buscarAlumno(self, carnetIngresado):
        actual = self.primero
        while actual != None:
            if actual.dato.carnet == carnetIngresado:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def existepiso(self, nompiso):
        actual = self.primero
        while actual != None:
            if actual.dato.nombre == nompiso:
                return True
            actual = actual.siguiente
        return False

    def buscarcodigos(self, nompiso):
        actual = self.primero
        while actual != None:
            if actual.dato.nombre == nompiso:
                for e in actual.dato.patrones:
                    print(e.codigo)
            actual = actual.siguiente

    def devolverFyC(self, nompiso):
        actual = self.primero
        while actual != None:
            if actual.dato.nombre == nompiso:
                return actual.dato.filas,actual.dato.columnas
            actual = actual.siguiente

    def devolverprecios(self, nompiso):
        actual = self.primero
        while actual != None:
            if actual.dato.nombre == nompiso:
                return actual.dato.precioV,actual.dato.precioC
            actual = actual.siguiente

    def buscarpatron(self, nompiso, codigopatron):
        actual = self.primero
        while actual != None:
            if actual.dato.nombre == nompiso:
                for e in actual.dato.patrones:
                    if e.codigo == codigopatron:
                        return e.azulejos
            else:
                print("no se encontro el piso :(")
            actual = actual.siguiente

    # Bubblesort
    def BubbleSort(self):
        if self.primero is None or self.primero.siguiente is None:
            return 

        last = None
        while last != self.primero:
            actual = self.primero
            while actual.siguiente != last:
                if actual.dato.nota > actual.siguiente.dato.nota:
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                actual = actual.siguiente
            last = actual

        print("Lista ordenada: ")
        self.imprimir()
                
    # InsertionSort
    
    def insertionSort(self):
        if self.primero is None or self.primero.siguiente is None:
            return
        
        actual = self.primero.siguiente
        while actual != None:
            actual2 = self.primero
            while actual2 != actual:
                if actual.dato.nota < actual2.dato.nota:
                    actual.dato, actual2.dato = actual2.dato, actual.dato
                actual2 = actual2.siguiente
            actual = actual.siguiente

        print("Lista ordenada:")
        self.imprimir()

        print("Lista ordenada: ")
        self.imprimir()

    def BubbleDescendente(self):
        if self.primero is None or self.primero.siguiente is None:
            return 

        last = None
        while last != self.primero:
            actual = self.primero
            while actual.siguiente != last:
                if actual.dato.nombre > actual.siguiente.dato.nombre:
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                actual = actual.siguiente
            last = actual

        print("Lista: ")
        self.imprimir()

    def ordenarcodigos(self, nompiso):
        actual = self.primero
        while actual != None:
            if actual.dato.nombre == nompiso:
                for e in actual.dato.patrones:
                    print(e.codigo) 
            actual = actual.siguiente

    def ordenarcodigos1(self,nombrepiso):
        actual = self.primero
        codigos = []  # Lista para almacenar los códigos de los patrones
        
        while actual is not None:
            if actual.dato.nombre == nombrepiso:
                for patron in actual.dato.patrones:
                    codigos.append(patron.codigo)  # Agrega el código a la lista
                break  # Salir del bucle una vez que hayas encontrado el piso
            actual = actual.siguiente
        
        if codigos:  # Verifica si hay códigos en la lista
            codigos.sort()  # Ordena la lista alfabéticamente
            for codigo in codigos:
                print(codigo)
        else:
            print("No se encontró el piso con el nombre:", nombrepiso)
