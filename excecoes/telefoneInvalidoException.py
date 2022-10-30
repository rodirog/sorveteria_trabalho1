

class TelefoneInvalidoException(Exception):
    def __init__(self):
        super().__init__("Telefone invalido")
