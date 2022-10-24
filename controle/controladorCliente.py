from limite.telaCliente import TelaCliente
from entidade.cliente import Cliente

class ControladorCliente:
    def __init__(self, controlador_principal):
        #self.__controlador_principal = controlador_principal
        self.__tela_cliente = TelaCliente()
        self.__clientes = []

    def adicionar_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        if not self.__encontrar_cliente_pelo_nome(dados_cliente["nome_cliente"]):
            cliente = Cliente(dados_cliente["nome_cliente"],
                          dados_cliente["cpf"],
                          dados_cliente["email_cliente"],
                          dados_cliente["telefone_cliente"])

            self.__clientes.append(cliente)

    def excluir_cliente(self):
        nome_cliente = self.__tela_cliente.pega_dados_cliente()["nome_cliente"]
        cliente_encontrado = self.__encontrar_cliente_pelo_nome(nome_cliente)
        if cliente_encontrado:
            self.__clientes.remove(cliente_encontrado)

    def __encontrar_cliente_pelo_nome(self, nome):
        for cliente in self.__clientes:
            if cliente.nome == nome:
                return cliente
