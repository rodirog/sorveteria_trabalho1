
class TelaLoja:

    def mostrar_tela_inicial(self):
        print("*" * 20)
        print("Sistema Vendas")
        print("*" * 20)
        print("1 - Fornecedores")
        print("2 - Produtos")
        print("3 - Clientes")
        print("4 - Vendedores")
        print("5 - Notas Fiscais")
        print("0 - Sair")
        opcao = int(input("Escolha a opcao: "))
        return opcao