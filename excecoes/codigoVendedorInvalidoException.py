

class CodigoVendedorInvalidoException(Exception):
    def __init__(self):
        super().__init__("Codigo vendedor invalido!")
