

class TelaVendedor:
    def mostrar_tela_opcoes(self):
        print("*" * 20)
        print("VENDEDOR")
        print("*" * 20)
        print("1 - Incluir vendedor")
        print("2 - Listar vendedor")
        print("3 - Alterar Vendedor")
        print("4 - Excluir vendedor")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_vendedores(self, dados_vendedores):
        print("LISTA VENDEDORES")
        for dados_vendedor in dados_vendedores:
            self.__mostrar_vendedor(dados_vendedor)

    def __mostrar_vendedor(self, dados_vendedor):
        codigo_vendedor = dados_vendedor["codigo_vendedor"]
        nome_vendedor = dados_vendedor["nome_vendedor"]
        cpf_vendedor = dados_vendedor["cpf_vendedor"]
        print("/ VENDEDOR")
        print(f"| Codigo: {codigo_vendedor}")
        print(f"| Nome: {nome_vendedor}")
        print(f"| Cpf: {cpf_vendedor}")
        print("\__________________")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def pegar_dados_vendedor(self):
        print("CADASTRO VENDEDOR")
        nome_vendedor = input("Nome do vendedor: ")
        cpf_vendedor = input("Cpf do Vendedor:")

        return {"nome_vendedor": nome_vendedor, "cpf_vendedor": cpf_vendedor}

    def selecionar_vendedor(self):
        codigo_vendedor = input(
            "Insira o codigo do vendedor que deseja selecionar: ")
        return codigo_vendedor
