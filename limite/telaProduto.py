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
        codigo_produto = int(input("Codigo do Produto: "))
        estoque_produto = int(input("Estoque do Produto: "))
        descricao_produto = str(input("Descricao do Produto: "))
        tipo_produto = str(input("Tipo do Produto (insira 'Sorvete' ou 'Bebida'): ").capitalize())
        valor_produto = float(input("Valor do Produto: "))
        #nao ocorre instanciacao de cliente aqui pois tela nao conversa com entidade

        return {"codigo_produto": codigo_produto, "estoque_produto": estoque_produto, "descricao_produto": descricao_produto, "tipo_produto": tipo_produto, "valor_produto": valor_produto}

    def mostrar_produto(self, dados_produto):
        print()
        print("PRODUTO")
        print(f"Codigo: {dados_produto['codigo_produto']}")
        print(f"Estoque: {dados_produto['estoque_produto']}")
        print(f"Descricao: {dados_produto['descricao_produto']}")
        print(f"Tipo: {dados_produto['tipo_produto']}")
        print(f"Valor: {dados_produto['valor_produto']}")
        print()
        # nao pode print(cliente.nome) pq a tela nao pode falar com cliente

    def selecionar_produto(self):
        print()
        codigo = int(input("Insira o codigo do produto que deseja selecionar: "))
        return codigo

    def mostrar_mensagem(self, msg):
        print(msg)
        print()