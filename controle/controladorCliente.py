from excecoes.clienteJahExisteException import ClienteJahExisteException
from excecoes.clienteNaoExisteException import ClienteNaoExisteException
from excecoes.cpfInvalidoException import CpfInvalidoException
from excecoes.emailInvalidoException import EmailInvalidoException
from excecoes.nomeInvalidoException import NomeInvalidoException
from excecoes.telefoneInvalidoException import TelefoneInvalidoException
from limite.telaCliente import TelaCliente
from entidade.cliente import Cliente


class ControladorCliente:
    def __init__(self):
        #self.__controlador_principal = controlador_principal
        self.__tela_cliente = TelaCliente([])
        self.__clientes = []

    def adicionar_cliente(self):
        dados_cliente = self.__tela_cliente.pegar_dados_cliente()

        cpf_cliente = dados_cliente["cpf_cliente"]
        if not self.eh_cpf_valido(cpf_cliente):
            raise CpfInvalidoException

        cliente_encontrado = self.encontrar_cliente(cpf_cliente)
        if cliente_encontrado:
            raise ClienteJahExisteException

        nome_cliente = dados_cliente["nome_cliente"]
        if not self.eh_nome_valido(nome_cliente):
            raise NomeInvalidoException

        email_cliente = dados_cliente["email_cliente"]
        if not self.eh_email_valido(email_cliente):
            raise EmailInvalidoException

        telefone_cliente = dados_cliente["telefone_cliente"]
        if not self.eh_telefone_valido(telefone_cliente):
            raise TelefoneInvalidoException

        cliente = Cliente(nome_cliente,
                          cpf_cliente,
                          email_cliente,
                          telefone_cliente)

        self.__clientes.append(cliente)
        self.__tela_cliente.mostrar_mensagem(
            "O cliente foi cadastrado com sucesso!")

    def excluir_cliente(self):
        cpf_cliente = self.__tela_cliente.selecionar_cliente()
        if not self.eh_cpf_valido(cpf_cliente):
            raise CpfInvalidoException

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
        cpf_cliente = self.__tela_cliente.selecionar_cliente()
        if not self.eh_cpf_valido(cpf_cliente):
            raise CpfInvalidoException
            
        cliente_encontrado = self.encontrar_cliente(cpf_cliente)
        if not cliente_encontrado:
            raise ClienteNaoExisteException

        dados_cliente = self.__tela_cliente.pegar_dados_cliente()

        nome_cliente = dados_cliente["nome_cliente"]
        if not self.eh_nome_valido(nome_cliente):
            raise NomeInvalidoException

        if not self.eh_cpf_valido(cpf_cliente):
            raise CpfInvalidoException
        cpf_cliente = int(cpf_cliente)

        email_cliente = dados_cliente["email_cliente"]
        if not self.eh_email_valido(email_cliente):
            raise EmailInvalidoException

        telefone_cliente = dados_cliente["telefone_cliente"]
        if not self.eh_telefone_valido(telefone_cliente):
            raise TelefoneInvalidoException

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
                "cpf_cliente": cliente.cpf,
                "email_cliente": cliente.email,
                "telefone_cliente": cliente.telefone
            }
            dados_clientes.append(dados_cliente)

        return dados_clientes
        self.__tela_cliente.mostrar_clientes(dados_clientes)

    def mostrar_tela_opcoes(self):
        opcoes = {
            1: self.adicionar_cliente,
            2: self.listar_clientes,
            3: self.alterar_cliente,
            4: self.excluir_cliente
        }

        while True:
            dados_clientes = self.listar_clientes()
            opcao = self.__tela_cliente.mostrar_tela_opcoes(dados_clientes)

            if opcao == 0:
                break

            try:
                opcoes[opcao]()
            except (ClienteJahExisteException, ClienteNaoExisteException, NomeInvalidoException, CpfInvalidoException, EmailInvalidoException, TelefoneInvalidoException) as err:
                self.__tela_cliente.mostrar_mensagem(f"Erro: {err.args[0]}")

    def eh_nome_valido(self, nome_cliente):
        return nome_cliente.isalpha()

    def eh_cpf_valido(self, cpf_cliente):
        return isinstance(cpf_cliente, int)

    def eh_email_valido(self, email_cliente):
        return isinstance(email_cliente, str)

    def eh_telefone_valido(self, telefone_cliente):
        return telefone_cliente.isalnum()
