class EstoqueVazioException(Exception):
    def __init__(self):
        super().__init__("ATENCAO: Quantidade digitada eh maior do\
                         que a quantidade no estoque. Tente novamente.")
