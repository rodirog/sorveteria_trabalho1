

class CpfInvalidoException(Exception):
    def __init__(self):
        super().__init__("Cpf invalido")
