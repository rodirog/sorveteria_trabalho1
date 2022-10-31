class EstoqueVazioException(Exception):
    def __init__(self):
        super().__init__("ATENCAO: Quantidade/peso digitado eh maior do\
                         que a quantidade no estoque. Tente novamente.")
