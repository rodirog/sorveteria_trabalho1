
class TelaLoja:

    def mostra_tela_inicial(self):
        print("*" * 20)
        print("Sistema Vendas")
        print("*" * 20)
        print("1 - Fornecedores")
        print("2 - Produtos")
        print("3 - Notas Fiscais")
        print("0 - Sair")
        opcao = int(input("Escolha a opcao: "))
        return opcao