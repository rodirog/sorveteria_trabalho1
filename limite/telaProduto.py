class TelaProduto:

    def mostrar_tela_opcoes(self):
        print("*" * 20)
        print("PRODUTO")
        print("*" * 20)
        print("1 - Incluir Produto")
        print("2 - Excluir Produto")
        print("3 - Listar Produto(s)")
        print("4 - Alterar Produto")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pegar_dados_produto(self):
        print()
        print("CADASTRO/ALTERAR PRODUTO")
        codigo_produto = input("Codigo do Produto: ")
        quantidade_produto = input("Quantidade do Produto: ")
        descricao_produto = input("Descricao do Produto: ")
        tipo_produto = input("Tipo do Produto: ")
        valor_produto = input("Valor do Produto: ")
        #nao ocorre instanciacao de cliente aqui pois tela nao conversa com entidade

        return {"codigo_produto": codigo_produto, "quantidade_produto": quantidade_produto, "descricao_produto": descricao_produto, "tipo_produto": tipo_produto, "valor_produto": valor_produto}

    def mostrar_produto(self, dados_produto):
        print()
        print("PRODUTO")
        print(f"Codigo: {dados_produto['codigo_produto']}")
        print(f"Quantidade: {dados_produto['quantidade_produto']}")
        print(f"Descricao: {dados_produto['descricao_produto']}")
        print(f"Tipo: {dados_produto['tipo_produto']}")
        print(f"Valor: {dados_produto['valor_produto']}")
        print()
        # nao pode print(cliente.nome) pq a tela nao pode falar com cliente

    def selecionar_produto(self):
        print()
        codigo = input("Insira o código do produto que deseja selecionar: ")
        return codigo

    def mostrar_mensagem(self, msg):
        print(msg)
        print()