from dtos.cliente_dto import ClienteDto
from excecoes.clienteJahExisteException import ClienteJahExisteException
from excecoes.clienteNaoExisteException import ClienteNaoExisteException
from excecoes.cpfInvalidoException import CpfInvalidoException
from excecoes.emailInvalidoException import EmailInvalidoException
from excecoes.nomeInvalidoException import NomeInvalidoException
from excecoes.telefoneInvalidoException import TelefoneInvalidoException
from limite.telaCliente import TelaCliente
from entidade.cliente import Cliente
from persistencia.cliente_dao import ClienteDAO


class ControladorCliente:
    def __init__(self):
        self.__tela_cliente = TelaCliente()
        self.__cliente_dao = ClienteDAO()
        # self.__clientes = []

    def adicionar_cliente(self):
        cliente_dto = self.__tela_cliente.pegar_dados_cliente()

        cpf = cliente_dto.cpf
        if not self.eh_cpf_valido(cpf):
            raise CpfInvalidoException

        nome = cliente_dto.nome
        if not self.eh_nome_valido(nome):
            raise NomeInvalidoException

        email = cliente_dto.email
        if not self.eh_email_valido(email):
            raise EmailInvalidoException

        telefone = cliente_dto.telefone
        if not self.eh_telefone_valido(telefone):
            raise TelefoneInvalidoException

        cliente = Cliente(nome,
                          cpf,
                          email,
                          telefone)

        self.__cliente_dao.adicionar(cliente)
        self.__tela_cliente.mostrar_mensagem(
            "O cliente foi cadastrado com sucesso!")

    def excluir_cliente(self):
        cpf = self.__tela_cliente.selecionar_cliente()
        if not self.eh_cpf_valido(cpf):
            raise CpfInvalidoException

        self.__cliente_dao.remover(cpf)
        self.__tela_cliente.mostrar_mensagem(
            "O cliente foi removido com sucesso!")

    def encontrar_cliente(self, cpf: int):
      return self.__cliente_dao.encontrar(cpf)

    def alterar_cliente(self):
        cpf = self.__tela_cliente.selecionar_cliente()
            
        cliente_encontrado = self.encontrar_cliente(cpf)
        if not cliente_encontrado:
            raise ClienteNaoExisteException

        cliente_dto = ClienteDto(cliente_encontrado.nome, cliente_encontrado.email, cliente_encontrado.telefone, cliente_encontrado.cpf)

        cliente_dto = self.__tela_cliente.alterar_dados_cliente(cliente_dto)

        nome = cliente_dto.nome
        if not self.eh_nome_valido(nome):
            raise NomeInvalidoException

        email = cliente_dto.email
        if not self.eh_email_valido(email):
            raise EmailInvalidoException

        telefone = cliente_dto.telefone
        if not self.eh_telefone_valido(telefone):
            raise TelefoneInvalidoException

        cliente_encontrado.nome = nome
        cliente_encontrado.email = email
        cliente_encontrado.telefone = telefone

        self.__cliente_dao.atualizar(cliente_encontrado)
        self.__tela_cliente.mostrar_mensagem(
            "O cliente foi alterado com sucesso!")

    def listar_clientes(self):
        clientes_dtos = []
        clientes = self.__cliente_dao.listar()
        for cliente in clientes:
            cliente_dto = ClienteDto(cliente.nome, cliente.email, cliente.telefone, cliente.cpf)
            clientes_dtos.append(cliente_dto)

        self.__tela_cliente.mostrar_clientes(clientes_dtos)

    def mostrar_tela_opcoes(self):
        opcoes = {
            1: self.adicionar_cliente,
            2: self.listar_clientes,
            3: self.alterar_cliente,
            4: self.excluir_cliente
        }

        while True:
            opcao = self.__tela_cliente.mostrar_tela_opcoes()

            if opcao == 0:
                break

            try:
                opcoes[opcao]()
            except (ClienteJahExisteException, ClienteNaoExisteException, NomeInvalidoException, CpfInvalidoException, EmailInvalidoException, TelefoneInvalidoException) as err:
                self.__tela_cliente.mostrar_mensagem(f"Erro: {err.args[0]}")

    def eh_nome_valido(self, nome):
        return nome.replace(' ', '').isalpha()

    def eh_cpf_valido(self, cpf):
        return isinstance(cpf, int)

    def eh_email_valido(self, email):
        return isinstance(email, str)

    def eh_telefone_valido(self, telefone):
        return telefone.isalnum()
