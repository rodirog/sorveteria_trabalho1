

class PesoInvalidoException(Exception):
    def __init__(self):
        super().__init__("Peso invalido")
