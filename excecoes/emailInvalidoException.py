

class EmailInvalidoException(Exception):
    def __init__(self):
        super().__init__("Email invalido")
