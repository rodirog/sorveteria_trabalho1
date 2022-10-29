from limite.telaFornecedor import TelaFornecedor
from entidade.fornecedor import Fornecedor


class ControladorFornecedor:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        #aqui define que a relacao eh bidirecional
        self.__tela_fornecedor = TelaFornecedor()
        self.__fornecedores = []

    def incluir_fornecedor(self):
        dados_fornecedor = self.__tela_fornecedor.pegar_dados_fornecedor()
        fornecedor = Fornecedor(dados_fornecedor["nome_fornecedor"],
                                dados_fornecedor["cnpj_fornecedor"],
                                dados_fornecedor["telefone_fornecedor"])
        if not self.encontrar_fornecedor_pelo_nome(fornecedor.nome):
            self.__fornecedores.append(fornecedor)

    def encontrar_fornecedor_pelo_nome(self, nome):
        for fornecedor in self.__fornecedores:
            if fornecedor.nome == nome:
                return fornecedor

    def alterar_fornecedor(self):
        self.listar_fornecedores()
        nome_fornecedor = self.__tela_fornecedor.selecionar_fornecedor()
        fornecedor = self.encontrar_fornecedor_pelo_nome(nome_fornecedor)

        if(fornecedor is not None):
            novos_dados_fornecedor = self.__tela_fornecedor.pegar_dados_fornecedor()
            fornecedor.nome = novos_dados_fornecedor["nome_fornecedor"]
            fornecedor.cnpj = novos_dados_fornecedor["cnpj_fornecedor"]
            fornecedor.telefone = novos_dados_fornecedor["telefone_fornecedor"]
            self.__tela_fornecedor.mostrar_mensagem("Fornecedor alterado com sucesso!")
            self.listar_fornecedores()

        else:
            self.__tela_fornecedor.mostrar_mensagem("ATENCAO: Fornecedor não existente")


    def excluir_fornecedor(self):
        nome_fornecedor = self.__tela_fornecedor.selecionar_fornecedor()
        fornecedor_encontrado = self.encontrar_fornecedor_pelo_nome(nome_fornecedor)
        if fornecedor_encontrado:
            self.__fornecedores.remove(fornecedor_encontrado)
            self.__tela_fornecedor.mostrar_mensagem("Fornecedor excluído com sucesso")
        else:
            self.__tela_produto.mostrar_mensagem("Fornecedor excluído com sucesso")

    def listar_fornecedores(self):
        for fornecedor in self.__fornecedores:
            dados_fornecedor = {"nome_fornecedor": fornecedor.nome,
                                "cnpj_fornecedor": fornecedor.cnpj,
                                "telefone_fornecedor": fornecedor.telefone}

            self.__tela_fornecedor.mostrar_fornecedor(dados_fornecedor)
            

    def mostrar_tela_opcoes(self):
        opcoes = {1: self.incluir_fornecedor, 2: self.excluir_fornecedor,
                  3:self.listar_fornecedores, 4: self.alterar_fornecedor}

        while True:
            opcao = self.__tela_fornecedor.mostrar_tela_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
