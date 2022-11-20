class TelaProduto:

    def mostrar_tela_opcoes(self):
        print("*" * 20)
        print("PRODUTO")
        print("*" * 20)
        print("1 - Incluir Produto")
        print("2 - Excluir Produto")
        print("3 - Listar Produto(s)")
        print("4 - Alterar Produto")
        print("5 - Relatorio de sorvetes")
        print("6 - Relatorio de bebidas")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pegar_dados_produto(self):
        print()
        print("CADASTRO PRODUTO")
        codigo_produto = int(input("Codigo do Produto: "))
        estoque_produto = int(input("Estoque do Produto: "))
        descricao_produto = str(input("Descricao do Produto: "))
        tipo_produto = int(input("Tipo do Produto (insira '1' para sorvete ou '2' para bebida): "))
        valor_produto = float(input("Valor do Produto: "))

        return {"codigo_produto": codigo_produto, "estoque_produto": estoque_produto, "descricao_produto": descricao_produto, "tipo_produto": tipo_produto, "valor_produto": valor_produto}

    def alterar_dados_produto(self):
        print()
        print("ALTERAR PRODUTO")
        codigo_produto = int(input("Codigo do Produto: "))
        estoque_produto = int(input("Estoque do Produto: "))
        descricao_produto = str(input("Descricao do Produto: "))
        valor_produto = float(input("Valor do Produto: "))

        return {"codigo_produto": codigo_produto, "estoque_produto": estoque_produto, "descricao_produto": descricao_produto, "valor_produto": valor_produto}

    def mostrar_produto(self, dados_produto):
        print()
        print("PRODUTO")
        print(f"Codigo: {dados_produto['codigo_produto']}")
        print(f"Estoque: {dados_produto['estoque_produto']}")
        print(f"Descricao: {dados_produto['descricao_produto']}")
        print(f"Tipo: {dados_produto['tipo_produto']}")
        print(f"Valor: {dados_produto['valor_produto']}")
        print()

    def selecionar_produto(self):
        print()
        codigo = int(input("Insira o codigo do produto que deseja selecionar: "))
        return codigo

    def mostrar_relatorio_de_sorvetes(self, dados_sorvete):
        print()
        print("SORVETE")
        print(f"Peso total vendido: {dados_sorvete['quantidade_vendida_produto']}kg")
        print(f"Codigo: {dados_sorvete['codigo_produto']}")
        print(f"Estoque: {dados_sorvete['estoque_produto']}")
        print(f"Descricao: {dados_sorvete['descricao_produto']}")
        print(f"Valor: {dados_sorvete['valor_produto']}")
        print()

    def mostrar_relatorio_de_bebidas(self, dados_bebida):
        print()
        print("BEBIDA")
        print(f"Quantidade total vendida: {dados_bebida['quantidade_vendida_produto']} unidade(s)")
        print(f"Codigo: {dados_bebida['codigo_produto']}")
        print(f"Estoque: {dados_bebida['estoque_produto']}")
        print(f"Descricao: {dados_bebida['descricao_produto']}")
        print(f"Valor: {dados_bebida['valor_produto']}")
        print()

    def mostrar_mensagem(self, msg):
        print(msg)
        print()