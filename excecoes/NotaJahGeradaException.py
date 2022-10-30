

class NotaJahGeradaException(Exception):
    def __init__(self):
        super().__init__("Nota já gerada!")
