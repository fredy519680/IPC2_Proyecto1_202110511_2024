class Patron:
    def __init__(self, codigo, azulejos):
        self.codigo = codigo
        self.azulejos = azulejos
      
    def __str__(self):
        return f"Código: {self.codigo}, Patrón: {self.azulejos}"