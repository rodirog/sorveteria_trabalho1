class NotaFiscalNaoExisteException(Exception):
    def __init__(self):
        super().__init__("Nota fiscal não existe!")
