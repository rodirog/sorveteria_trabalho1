from excecoes.clienteJahExisteException import ClienteJahExisteException
from excecoes.clienteNaoExisteException import ClienteNaoExisteException
from limite.telaCliente import TelaCliente
from entidade.cliente import Cliente


class ControladorCliente:
    def __init__(self, controlador_principal):
        #self.__controlador_principal = controlador_principal
        self.__tela_cliente = TelaCliente()
        self.__clientes = []

    def adicionar_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cpf_cliente = dados_cliente["cpf_cliente"]
        if self.encontrar_cliente(cpf_cliente):
            raise ClienteJahExisteException

        cliente = Cliente(dados_cliente["nome_cliente"],
                          dados_cliente["cpf_cliente"],
                          dados_cliente["email_cliente"],
                          dados_cliente["telefone_cliente"])

        self.__clientes.append(cliente)
        self.__tela_cliente.mostrar_mensagem(
            "O cliente foi cadastrado com sucesso!")

    def excluir_cliente(self):
        cpf_cliente = self.__tela_cliente.pegar_cpf_cliente()
        cliente_encontrado = self.encontrar_cliente(cpf_cliente)
        if not cliente_encontrado:
            raise ClienteNaoExisteException

        self.__clientes.remove(cliente_encontrado)
        self.__tela_cliente.mostrar_mensagem(
            "O cliente foi removido com sucesso!")

    def encontrar_cliente(self, cpf_cliente):
        for cliente in self.__clientes:
            if cliente.cpf == cpf_cliente:
                return cliente

    def alterar_cliente(self):
        cpf_cliente = self.__tela_cliente.pegar_cpf_cliente()
        cliente_encontrado = self.encontrar_cliente(cpf_cliente)
        if not cliente_encontrado:
            raise ClienteNaoExisteException

        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        nome_cliente = dados_cliente["nome_cliente"]
        email_cliente = dados_cliente["email_cliente"]
        cpf_cliente = dados_cliente["cpf_cliente"]
        telefone_cliente = dados_cliente["telefone_cliente"]

        cliente_encontrado.nome = nome_cliente
        cliente_encontrado.email = email_cliente
        cliente_encontrado.cpf = cpf_cliente
        cliente_encontrado.telefone = telefone_cliente

        self.__tela_cliente.mostrar_mensagem(
            "O cliente foi alterado com sucesso!")

    def listar_clientes(self):
        dados_clientes = []
        for cliente in self.__clientes:
            dados_cliente = {
                "nome_cliente": cliente.nome,
                "telefone_cliente": cliente.telefone
            }
            dados_clientes.append(dados_cliente)

        self.__tela_cliente.mostrar_clientes(dados_clientes)

    def selecionar_cliente(self):
        self.__tela_cliente.mostrar_mensagem(
            "Insira o cpf do cliente que deseja selecionar")
        cpf_cliente = self.__tela_cliente.pegar_cpf_cliente()
        print(cpf_cliente)

    def mostrar_tela_opcoes(self):
        opcoes = {
            1: self.adicionar_cliente,
            2: self.excluir_cliente,
            3: self.selecionar_cliente,
            4: self.listar_clientes,
            5: self.alterar_cliente
        }

        while True:
            opcao = self.__tela_cliente.mostrar_tela_opcoes()

            if opcao == 0:
                break

            try:
                opcoes[opcao]()
            except ClienteJahExisteException:
                self.__tela_cliente.mostrar_mensagem("O cliente já existe!")
            except ClienteNaoExisteException:
                self.__tela_cliente.mostrar_mensagem("O cliente não existe!")
