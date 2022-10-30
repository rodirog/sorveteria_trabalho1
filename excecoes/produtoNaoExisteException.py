class ProdutoNaoExisteException(Exception):
    def __init__(self):
        super().__init__("Produto não existe!")
