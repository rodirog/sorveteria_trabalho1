class EntidadeNaoExisteException(Exception):
    def __init__(self):
        super().__init__("Entidade não existe!")