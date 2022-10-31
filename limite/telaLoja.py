
class TelaLoja:

    def mostrar_tela_inicial(self):
        print("*" * 20)
        print("Sistema Vendas")
        print("*" * 20)
        print("1 - Produtos")
        print("2 - Clientes")
        print("3 - Vendedores")
        print("4 - Notas Fiscais")
        print("0 - Sair")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_mensagem(self, msg):
        print(msg)
        print()