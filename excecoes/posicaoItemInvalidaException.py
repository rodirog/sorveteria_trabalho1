

class PosicaoItemInvalidaException(Exception):
    def __init__(self):
        super().__init__("Posição do item é invalida")
