import PySimpleGUI as sg


class TelaNotaFiscal:

    def __init__(self):
        self.__window = None
        self.init_notas_opcoes()

    def tela_notas_opcoes(self):
        self.init_notas_opcoes()
        opcao = None
        button, values = self.open()
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_notas_opcoes(self):
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
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_itens_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- ITEM NOTA FISCAL ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir Item', "RD1", key='1')],
        [sg.Radio('Excluir Item', "RD1", key='2')],
        [sg.Radio('Listar Itens', "RD1", key='3')],
        [sg.Radio('Gerar Nota', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de notas fiscais').Layout(layout)

    def mostrar_relatorio_da_nota(self, dados_nota_fiscal, dados_itens):
        sg.ChangeLookAndFeel('DarkTeal4')
        col1= [
            [sg.Text("Numero da nota: " + str(dados_nota_fiscal["numero_nota"]), font=("Helvica", 12))],
            [sg.Text("")],
            [sg.Text("Nome do(a) cliente:", font=("Helvica", 10))],
            [sg.Text(str(dados_nota_fiscal["nome_cliente_nota"]), font=("Helvica", 12))],
            [sg.Text("")],
            [sg.Text("Nome do(a) vendedor(a):", font=("Helvica", 10))],
            [sg.Text(str(dados_nota_fiscal["nome_vendedor_nota"]), font=("Helvica", 12))],
            [sg.Text("")],
            [sg.Text("Data:", font=("Helvica", 10))],
            [sg.Text(str(dados_nota_fiscal["data_nota"]), font=("Helvica", 10))],
            [sg.Text("")],
            [sg.Text("Total:", font=("Helvica", 30))],
            [sg.Text(str(dados_nota_fiscal["valor_total_nota"]), font=("Helvica", 14))],
            ]
        
        col2 = [[sg.Text("Numero do item:", font=("Helvica", 10))]]
        
        for item in dados_itens:
            col2.append([sg.Text(str(item["numero_item"]), font=("Helvica", 10))])

        col3 = [[sg.Text("Codigo produto:", font=("Helvica", 10))]]
        
        for item in dados_itens:
            col3.append([sg.Text(str(item["codigo_produto"]), font=("Helvica", 10))])
                        
        col4 = [[sg.Text("Descricao:", font=("Helvica", 10))]]
        for item in dados_itens:
            col4.append([sg.Text(str(item["descricao_produto"]), font=("Helvica", 10))])

        col5 = [[sg.Text("Quantidade:", font=("Helvica", 10))]]
        for item in dados_itens:
            col5.append([sg.Text(str(item["qtd_item"]), font=("Helvica", 10))])

        col6 = [[sg.Text("Valor:", font=("Helvica", 10))]]
        for item in dados_itens:
            col6.append([sg.Text(str(item["valor_item"]), font=("Helvica", 10))])

        col7 = [[sg.Text("Total:", font=("Helvica", 10))]]
        for item in dados_itens:
            col7.append([sg.Text(str(item["total_item"]), font=("Helvica", 10))])
        

        layout = [[[[sg.Text('------------- Relatório da Nota -------------', font=("Helvica", 25))],
            [sg.Column(col1, key='c1', element_justification='l', expand_x=True),
             sg.Column(col2, key='c2', element_justification='c', vertical_alignment='t', expand_x=True),
             sg.Column(col3, key='c3', element_justification='c', vertical_alignment='t', expand_x=True),
             sg.Column(col4, key='c4', element_justification='c', vertical_alignment='t', expand_x=True),
             sg.Column(col5, key='c5', element_justification='c', vertical_alignment='t', expand_x=True),
             sg.Column(col6, key='c6', element_justification='c', vertical_alignment='t', expand_x=True),
             sg.Column(col7, key='c7', element_justification='c', vertical_alignment='t', expand_x=True)
             ]
        ],
        ],
            [sg.Button('Retornar')]
        ]
        
        self.__window = sg.Window('Relatório de nota fiscal').Layout(layout)

        button, values = self.open()
        
        self.close()

    def mostrar_notas(self, dados_notas):
        string_todas_notas = ""
        for nota in dados_notas:
            string_todas_notas = string_todas_notas + "NUMERO: " + str(nota["numero_nota"]) + '\n'
            string_todas_notas = string_todas_notas + "CLIENTE: " + str(nota["nome_cliente_nota"]) + '\n'
            string_todas_notas = string_todas_notas + "VENDEDOR: " + str(nota["nome_vendedor_nota"]) + '\n'
            string_todas_notas = string_todas_notas + "VALOR: " + str(nota["valor_total_nota"]) + '\n'
            string_todas_notas = string_todas_notas + "DATA: " + str(nota["data_nota"]) + '\n\n'

        sg.Popup('-------- LISTA DE NOTAS ----------', string_todas_notas)

    def mostrar_itens_nota(self, dados_itens):
        sg.ChangeLookAndFeel('DarkTeal4')
        col1 = [[sg.Text("Numero do item:", font=("Helvica", 10))]]
        
        for item in dados_itens:
            col1.append([sg.Text(str(item["numero_item"]), font=("Helvica", 10))])

        col2 = [[sg.Text("Codigo produto:", font=("Helvica", 10))]]
        
        for item in dados_itens:
            col2.append([sg.Text(str(item["codigo_produto"]), font=("Helvica", 10))])
                        
        col3 = [[sg.Text("Descricao:", font=("Helvica", 10))]]
        for item in dados_itens:
            col3.append([sg.Text(str(item["descricao_produto"]), font=("Helvica", 10))])

        col4 = [[sg.Text("Quantidade:", font=("Helvica", 10))]]
        for item in dados_itens:
            col4.append([sg.Text(str(item["qtd_item"]), font=("Helvica", 10))])
        
        layout = [[[[sg.Text('------------- Itens da Nota -------------', font=("Helvica", 15))],
            [sg.Column(col1, key='c1', element_justification='l', expand_x=True),
             sg.Column(col2, key='c2', element_justification='c', vertical_alignment='t', expand_x=True),
             sg.Column(col3, key='c3', element_justification='c', vertical_alignment='t', expand_x=True),
             sg.Column(col4, key='c4', element_justification='c', vertical_alignment='t', expand_x=True)
             ]
        ],
        ],
            [sg.Button('Retornar')]
        ]
        
        self.__window = sg.Window('Itens da Nota').Layout(layout)

        button, values = self.open()
        
        self.close()

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
        if button in (None, "Cancelar"):
            raise TypeError
        self.close()
        return {"cpf_cliente": cpf_cliente, "codigo_vendedor": codigo_vendedor}

    def pegar_dados_item_nota(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Cadastro Item Nota Fiscal")],
            [sg.Radio('Sorvete', "RADIO01", default=True, key="rd_sorvete"), sg.Radio('Bebida', "RADIO01")],
            [sg.Text("Codigo produto", size = (15,1)), sg.InputText(key="it_codigo_produto_item_nota")],
            [sg.Text("Quantidade/peso item", size = (15,1)), sg.InputText(key="it_quantidade_item_nota")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Notas Fiscais').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            return TypeError

        tipo_produto = values["rd_sorvete"]
        codigo_produto = values['it_codigo_produto_item_nota']
        quantidade_produto = values['it_quantidade_item_nota']

        self.close()
        return {"rd_sorvete": tipo_produto, "it_codigo_produto_item_nota": codigo_produto, "it_quantidade_item_nota": quantidade_produto}

    def selecionar_nota_fiscal(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- SELECIONAR NOTA FISCAL ----------', font=("Helvica", 25))],
        [sg.Text('Digite o numero da nota que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('Numero:', size=(15, 1)), sg.InputText(key='it_numero_nota')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona nota fiscal').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            raise TypeError
        numero = values['it_numero_nota']

        self.close()
        return int(numero)

    def selecionar_item_nota(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- SELECIONAR ITEM DA NOTA ----------', font=("Helvica", 25))],
        [sg.Text('Digite o numero do item que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('Numero:', size=(15, 1)), sg.InputText(key='it_numero_item')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona item').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            raise TypeError
        numero = values['it_numero_item']
        self.close()
        return int(numero)

