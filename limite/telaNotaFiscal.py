

class TelaNotaFiscal:
    def mostrar_tela_opcoes(self):
        print("*" * 20)
        print("NOTA FISCAL")
        print("*" * 20)
        print("1 - Incluir nota")
        print("2 - Listar nota")
        print("3 - Excluir nota")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_tela_item_opcoes(self):
        print("*" * 20)
        print("ITEM NOTA FISCAL")
        print("*" * 20)
        print("1 - Incluir item")
        print("2 - Excluir item")
        print("3 - Gerar nota")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_notas(self, dados_notas_fiscais):
        print("LISTA NOTAS")
        for dados_nota_fiscal in dados_notas_fiscais:
            self.__mostrar_nota(dados_nota_fiscal)

    def __mostrar_nota(self, dados_nota_fiscal):
        numero_nota = dados_nota_fiscal["numero_nota"]
        cliente_nota = dados_nota_fiscal["nome_cliente_nota"]
        vendedor_nota = dados_nota_fiscal["nome_vendedor_nota"]
        valor_total_nota = dados_nota_fiscal["valor_total_nota"]
        data_nota = dados_nota_fiscal["data_nota"]

        print("/ NOTA")
        print(f"| Número: {numero_nota}")
        print(f"| Cliente: {cliente_nota}")
        print(f"| Vendedor: {vendedor_nota}")
        print(f"| Valor total: {valor_total_nota}")
        print(f"| Data: {data_nota}")
        print("\__________________")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def pegar_dados_nota(self):
        print("CADASTRO NOTA FISCAL")
        cpf_cliente = input("Cpf do cliente: ")
        codigo_vendedor = input("Codigo do Vendedor:")

        return {"cpf_cliente": cpf_cliente, "codigo_vendedor": codigo_vendedor}

    def pegar_dados_item_nota(self):
        print("CADASTRO ITEM NOTA FISCAL")
        codigo_produto_item_nota = input("Codigo produto: ")
        quantidade_item_nota = input("Quantidade do produto:")
        peso_item_nota = input("Peso do produto:")

        return {
            "codigo_produto_item_nota": codigo_produto_item_nota,
            "quantidade_item_nota": quantidade_item_nota,
            "peso_item_nota": peso_item_nota
        }

    def selecionar_nota_fiscal(self):
        print()
        numero_nota = input("Insira o número da nota que deseja selecionar: ")
        return numero_nota

    def selecionar_item_nota(self):
        print()
        posicao_item_nota = input(
            "Insira o numero do item da nota que deseja selecionar: ")
        return posicao_item_nota
