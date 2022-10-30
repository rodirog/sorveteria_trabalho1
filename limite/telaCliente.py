

class TelaCliente:

    def mostrar_tela_opcoes(self):
        print("*" * 20)
        print("CLIENTES")
        print("*" * 20)
        print("1 - Incluir Cliente")
        print("2 - Excluir Cliente")
        print("3 - Selecionar Cliente")
        print("4 - Listar Cliente")
        print("5 - Alterar Cliente")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_clientes(self, dados_clientes):
        print("LISTA CLIENTES")
        for dados_cliente in dados_clientes:
            self.__mostrar_cliente(dados_cliente)

    def __mostrar_cliente(self, dados_cliente):
        nome_cliente = dados_cliente["nome_cliente"]
        telefone_cliente = dados_cliente["telefone_cliente"]
        print("/ CLIENTE")
        print(f"| Nome: {nome_cliente}")
        print(f"| Fone: {telefone_cliente}")
        print("\__________________")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def pegar_cpf_cliente(self):
        cpf_cliente = input("Cpf do Cliente:")
        return cpf_cliente

    def pegar_dados_cliente(self):
        print("CADASTRO CLIENTE")
        nome_cliente = input("Nome do Cliente: ")
        email_cliente = input("Email do Cliente:")
        cpf_cliente = self.pega_cpf_cliente()
        telefone_cliente = input("Telefone do Cliente: ")
        return {"nome_cliente": nome_cliente, "telefone_cliente": telefone_cliente, "email_cliente": email_cliente, "cpf_cliente": cpf_cliente}

    def selecionar_cliente(self):
        print()
        cpf = input("Insira o cpf do cliente que deseja selecionar: ")
        return cpf
