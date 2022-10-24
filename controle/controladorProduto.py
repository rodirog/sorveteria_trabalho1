from limite.telaProduto import TelaProduto
from entidade.produto import Produto


class ControladorProduto:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        #aqui define que a relacao eh bidirecional
        self.__tela_produto = TelaProduto()
        self.__produtos = []

    def incluir_produto(self):
        dados_produto = self.__tela_produto.pegar_dados_produto()
        produto = Produto(dados_produto["codigo_produto"],
                          dados_produto["quantidade_produto"],
                          dados_produto["descricao_produto"])
        if not self.encontrar_produto_pelo_codigo(produto.codigo):
            self.__produtos.append(produto)

    def encontrar_produto_pelo_codigo(self, codigo):
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto

    def alterar_produto(self):
        codigo_produto = self.__tela_produto.pegar_dados_produto()["codigo_produto"]
        produto_encontrado = self.encontrar_produto_pelo_codigo(codigo_produto)
        if produto_encontrado:
            self.__produtos.remove(produto_encontrado)

    def excluir_produto(self):
        pass

    def listar_produto(self):
        for produto in self.__produtos:
            dados_produto = {"codigo_produto": produto.codigo,
                             "quantidade_produto": produto.quantidade,
                             "descricao_produto": produto.descricao}

            self.__tela_produto.mostrar_produto(dados_produto)

    def mostrar_tela_opcoes(self):
        opcoes = {1: self.incluir_produto, 2: self.excluir_produto,
                  3:self.listar_produto, 4: self.alterar_produto}

        while True:
            opcao = self.__tela_produto.mostrar_tela_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
