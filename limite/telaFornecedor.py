class TelaFornecedor:

    def mostrar_tela_opcoes(self):
        print("*" * 20)
        print("FORNECEDOR")
        print("*" * 20)
        print("1 - Incluir Fornecedor")
        print("2 - Excluir Fornecedor")
        print("3 - Listar Fornecedor(es)")
        print("4 - Alterar Fornecedor")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pegar_dados_fornecedor(self):
        print("CADASTRO/ALTERAR FORNECEDOR")
        nome_fornecedor = input("Nome do Fornecedor: ")
        cnpj_fornecedor = input("CNPJ do fornecedor: ")
        telefone_fornecedor = input("Telefone do Fornecedor: ")
        #nao ocorre instanciacao de cliente aqui pois tela nao conversa com entidade

        return {"nome_fornecedor": nome_fornecedor, "cnpj_fornecedor": cnpj_fornecedor, "telefone_fornecedor": telefone_fornecedor}

    def mostrar_fornecedor(self, dados_fornecedor):
        print()
        print("FORNECEDOR")
        print(f"Nome: {dados_fornecedor['nome_fornecedor']}")
        print(f"CNPJ: {dados_fornecedor['cnpj_fornecedor']}")
        print(f"Telefone: {dados_fornecedor['telefone_fornecedor']}")
        print()
        # nao pode print(cliente.nome) pq a tela nao pode falar com cliente

    def selecionar_fornecedor(self):
        print()
        nome = input("Insira o nome do fornecedor que deseja selecionar: ")
        return nome

    def mostrar_mensagem(self, msg):
        print(msg)
        print()



