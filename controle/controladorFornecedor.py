from limite.telaFornecedor import TelaFornecedor
from entidade.fornecedor import Fornecedor


class ControladorFornecedor:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        #aqui define que a relacao eh bidirecional
        self.__tela_fornecedor = TelaFornecedor()
        self.__fornecedores = []

    def inclui_fornecedor(self):
        dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecedor()
        fornecedor = Fornecedor(dados_fornecedor["nome_fornecedor"],
                                dados_fornecedor["cnpj_fornecedor"],
                                dados_fornecedor["telefone_fornecedor"])
        if not self.retorna_fornecedor_pelo_nome(fornecedor.nome):
            self.__fornecedores.append(fornecedor)

    def retorna_fornecedor_pelo_nome(self, nome):
        for fornecedor in self.__fornecedores:
            if fornecedor.nome == nome:
                return fornecedor

    def altera_fornecedor(self):
        pass

    def exclui_fornecedor(self):
        pass

    def lista_fornecedor(self):
        for fornecedor in self.__fornecedores:
            dados_fornecedor = {"nome_fornecedor": fornecedor.nome,
                                "cnpj_fornecedor": fornecedor.cnpj,
                                "telefone_fornecedor": fornecedor.telefone}

            self.__tela_fornecedor.mostra_fornecedor(dados_fornecedor)

    def mostra_tela_opcoes(self):
        opcoes = {1: self.inclui_fornecedor, 2: self.exclui_fornecedor,
                  3:self.lista_fornecedor, 4: self.altera_fornecedor}

        while True:
            opcao = self.__tela_fornecedor.mostra_tela_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
