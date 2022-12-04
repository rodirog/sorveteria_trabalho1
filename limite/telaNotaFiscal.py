import PySimpleGUI as sg


class TelaNotaFiscal:

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    # def mostrar_tela_opcoes(self):
    #     print("*" * 20)
    #     print("NOTA FISCAL")
    #     print("*" * 20)
    #     print("1 - Incluir nota")
    #     print("2 - Listar nota")
    #     print("3 - Excluir nota")
    #     print("0 - Voltar")
    #     opcao = int(input("Escolha a opcao: "))
    #     return opcao

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
    #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- NOTAS FISCAIS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir Nota Fiscal', "RD1", key='1')],
        [sg.Radio('Listar Notas Fiscais', "RD1", key='2')],
        [sg.Radio('Excluir Nota Fiscal', "RD1", key='3')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de notas fiscais').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def tela_itens_opcoes(self):
        self.init_itens_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_itens_opcoes(self):
    #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- ITEM NOTA FISCAL ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir Item', "RD1", key='1')],
        [sg.Radio('Excluir Item', "RD1", key='2')],
        [sg.Radio('Gerar Nota', "RD1", key='3')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de notas fiscais').Layout(layout)

    # def mostrar_tela_item_opcoes(self):
    #     print("*" * 20)
    #     print("ITEM NOTA FISCAL")
    #     print("*" * 20)
    #     print("1 - Incluir item")
    #     print("2 - Excluir item")
    #     print("3 - Gerar nota")
    #     print("0 - Voltar")
    #     opcao = int(input("Escolha a opcao: "))
    #     return opcao
    def mostrar_relatorio_da_nota(self, dados_nota_fiscal):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Relatório da Nota ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Relatório de nota fiscal').Layout(layout)

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

    def pegar_dados_nota(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Cadastro Nota Fiscal")],
            [sg.Text("CPF Cliente", size = (15,1)), sg.InputText(key="it_cpf_cliente")],
            [sg.Text("Codigo Vendedor", size = (15,1)), sg.InputText(key="it_codigo_vendedor")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Notas Fiscais').Layout(layout)

        button, values = self.open()
        cpf_cliente = values['it_cpf_cliente']
        codigo_vendedor = values['it_codigo_vendedor']
        
        self.close()
        return {"cpf_cliente": cpf_cliente, "codigo_vendedor": codigo_vendedor}

    # def pegar_dados_nota(self):
    #     print("CADASTRO NOTA FISCAL")
    #     cpf_cliente = input("Cpf do cliente: ")
    #     codigo_vendedor = input("Codigo do Vendedor:")

    #     return {"cpf_cliente": cpf_cliente, "codigo_vendedor": codigo_vendedor}

    def pegar_dados_item_nota(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Cadastro Item Nota Fiscal")],
            [sg.Text("Codigo produto", size = (15,1)), sg.InputText(key="it_codigo_produto_item_nota")],
            [sg.Text("Quantidade/peso item", size = (15,1)), sg.InputText(key="it_quantidade_item_nota")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Notas Fiscais').Layout(layout)

        button, values = self.open()
        codigo_produto = values['it_codigo_produto_item_nota']
        quantidade_produto = values['it_quantidade_item_nota']
        
        self.close()
        return {"it_codigo_produto_item_nota": codigo_produto, "it_quantidade_item_nota": quantidade_produto}

    # def pegar_dados_item_nota(self):
    #     print("CADASTRO ITEM NOTA FISCAL")
    #     codigo_produto_item_nota = input("Codigo produto: ")
    #     quantidade_item_nota = input("Quantidade/peso do produto:")

    #     return {
    #         "codigo_produto_item_nota": codigo_produto_item_nota,
    #         "quantidade_item_nota": quantidade_item_nota,
    #     }

    def selecionar_nota_fiscal(self):
        print()
        numero_nota = input("Insira o número da nota que deseja selecionar: ")
        return numero_nota

    def selecionar_item_nota(self):
        print()
        posicao_item_nota = input(
            "Insira o numero do item da nota que deseja selecionar: ")
        return posicao_item_nota
