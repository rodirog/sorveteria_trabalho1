import PySimpleGUI as sg


class TelaBebida:

    def __init__(self):
        self.__window = None
        self.init_opcoes()


    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- bebidaS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir bebida', "RD1", key='1')],
        [sg.Radio('Excluir bebida', "RD1", key='2')],
        [sg.Radio('Listar bebidas', "RD1", key='3')],
        [sg.Radio('Alterar bebidas', "RD1", key='4')],
        [sg.Radio('Relatório de bebidas', "RD1", key='5')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de bebidas').Layout(layout)

    def pegar_dados_bebida(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Incluir novo bebida")],
            [sg.Text("Codigo", size = (15,1)), sg.InputText(key="it_codigo")],
            [sg.Text("Estoque", size = (15,1)), sg.InputText(key="it_estoque")],
            [sg.Text("Descricao", size = (15,1)), sg.InputText(key="it_descricao")],
            [sg.Text("Valor", size = (15,1)), sg.InputText(key="it_valor")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de bebidas').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            raise TypeError
        codigo = int(values['it_codigo'])
        estoque = int(values['it_estoque'])
        descricao = values['it_descricao']
        valor = float(values['it_valor'])

        self.close()
        return {"codigo_bebida": codigo, "estoque_bebida": estoque, "descricao_bebida": descricao, "valor_bebida": valor}

    def alterar_dados_bebida(self, dados_bebida):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Alterar bebida")],
            [sg.Text("Codigo", size = (15,1)), sg.InputText(dados_bebida["codigo_bebida"], key="it_codigo")],
            [sg.Text("Estoque", size = (15,1)), sg.InputText(dados_bebida["estoque_bebida"], key="it_estoque")],
            [sg.Text("Descricao", size = (15,1)), sg.InputText(dados_bebida["descricao_bebida"], key="it_descricao")],
            [sg.Text("Valor", size = (15,1)), sg.InputText(dados_bebida["valor_bebida"], key="it_valor")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de bebidas').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            raise TypeError
        codigo = int(values['it_codigo'])
        estoque = int(values['it_estoque'])
        descricao = values['it_descricao']
        valor = float(values['it_valor'])

        self.close()
        return {"codigo_bebida": codigo, "estoque_bebida": estoque, "descricao_bebida": descricao, "valor_bebida": valor}

    def mostrar_bebidas(self, dados_bebidas):
        string_todos_bebidas = ""
        for bebida in dados_bebidas:
            string_todos_bebidas = string_todos_bebidas + "CODIGO: " + str(bebida["codigo_bebida"]) + '\n'
            string_todos_bebidas = string_todos_bebidas + "ESTOQUE: " + str(bebida["estoque_bebida"]) + '\n'
            string_todos_bebidas = string_todos_bebidas + "DESCRICAO: " + str(bebida["descricao_bebida"]) + '\n'
            string_todos_bebidas = string_todos_bebidas + "VALOR: " + str(bebida["valor_bebida"]) + '\n\n'

        sg.Popup('-------- LISTA DE bebidaS ----------', string_todos_bebidas)

    def selecionar_bebida(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- SELECIONAR bebida ----------', font=("Helvica", 25))],
        [sg.Text('Digite o codigo do bebida que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('Codigo:', size=(15, 1)), sg.InputText(key='it_codigo')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona bebida').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            raise TypeError
        codigo = values['it_codigo']
        self.close()
        return int(codigo)

    def mostrar_relatorio_de_bebidas(self, dados_bebidas):
        string_todos_bebidas = ""
        for dado in dados_bebidas:
            string_todos_bebidas = string_todos_bebidas + "DESCRICAO: " + str(dado["descricao_bebida"]) + '\n'
            string_todos_bebidas = string_todos_bebidas + "QUANTIDADE VENDIDA: " + str(dado["quantidade_vendida_bebida"]) + " unidade(s)" + '\n'
            string_todos_bebidas = string_todos_bebidas + "CODIGO: " + str(dado["codigo_bebida"]) + '\n'
            string_todos_bebidas = string_todos_bebidas + "ESTOQUE: " + str(dado["estoque_bebida"]) + '\n'
            string_todos_bebidas = string_todos_bebidas + "VALOR: " + str(dado["valor_bebida"]) + '\n\n'

        sg.Popup('-------- LISTA DE bebidaS ----------', string_todos_bebidas)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)


   

