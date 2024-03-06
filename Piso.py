class Piso:
    def __init__(self, nombre, filas, columnas, precioF, precioS, patrones):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.precioV = precioF
        self.precioC = precioS
        self.patrones = patrones

    def __str__(self):
        return f"Código: {self.nombre}, Filas: {self.filas}, Columnas: {self.columnas}, PrecioV: {self.precioV}, PrecioC: {self.precioC}, Patrones: {self.patrones}"
    

