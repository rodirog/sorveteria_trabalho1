

class TelaNotaFiscal:
    def mostrar_tela_opcoes(self):
        print("*" * 20)
        print("NOTA FISCAL")
        print("*" * 20)
        print("1 - Incluir item")
        print("2 - Excluir item")
        print("3 - Encontrar nota")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pegar_dados_nota(self):
        pass

    def mostrar_nota(self):
        pass

    def selecionar_nota_fiscal(self):
        print()
        numero_nota = input("Insira o número da nota que deseja selecionar: ")
        return numero_nota

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
