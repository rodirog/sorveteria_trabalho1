

class QuantidadeInvalidoException(Exception):
    def __init__(self):
        super().__init__("Quantidade invalida")
