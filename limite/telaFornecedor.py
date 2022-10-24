class TelaFornecedor:

    def mostra_tela_opcoes(self):
        print("*" * 20)
        print("FORNECEDOR")
        print("*" * 20)
        print("1 - Incluir Fornecedor")
        print("2 - Excluir Fornecedor")
        print("3 - Listar Fornecedor")
        print("4 - Alterar Fornecedor")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_fornecedor(self):
        print("CADASTRO FORNECEDOR")
        nome_fornecedor = input("Nome do Fornecedor: ")
        cnpj_fornecedor = input("CNPJ do fornecedor")
        telefone_fornecedor = input("Telefone do Fornecedor: ")
        #nao ocorre instanciacao de cliente aqui pois tela nao conversa com entidade

        return {"nome_fornecedor": nome_fornecedor, "cnpj_fornecedor": cnpj_fornecedor, "telefone_fornecedor:": telefone_fornecedor}

    def mostra_fornecedor(self, dados_fornecedor):
        print("FORNECEDOR")
        print(f"Nome: {dados_fornecedor['nome_fornecedor']}")
        print(f"CNPJ: {dados_fornecedor['cnpj_fornecedor']}")
        print(f"Telefone: {dados_fornecedor['telefone_fornecedor']}")
        # nao pode print(cliente.nome) pq a tela nao pode falar com cliente
