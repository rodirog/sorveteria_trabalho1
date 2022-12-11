import PySimpleGUI as sg


class TelaSorvete:

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
        [sg.Text('-------- sorveteS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir sorvete', "RD1", key='1')],
        [sg.Radio('Excluir sorvete', "RD1", key='2')],
        [sg.Radio('Listar sorvetes', "RD1", key='3')],
        [sg.Radio('Alterar sorvetes', "RD1", key='4')],
        [sg.Radio('Relatório de sorvetes', "RD1", key='5')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de sorvetes').Layout(layout)

    def pegar_dados_sorvete(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Incluir novo sorvete")],
            [sg.Text("Codigo", size = (15,1)), sg.InputText(key="it_codigo")],
            [sg.Text("Estoque", size = (15,1)), sg.InputText(key="it_estoque")],
            [sg.Text("Descricao", size = (15,1)), sg.InputText(key="it_descricao")],
            [sg.Text("Valor", size = (15,1)), sg.InputText(key="it_valor")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de sorvetes').Layout(layout)

        button, values = self.open()
        codigo = int(values['it_codigo'])
        estoque = int(values['it_estoque'])
        descricao = values['it_descricao']
        valor = float(values['it_valor'])

        self.close()
        return {"codigo_sorvete": codigo, "estoque_sorvete": estoque, "descricao_sorvete": descricao, "valor_sorvete": valor}

    def alterar_dados_sorvete(self, dados_sorvete):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Alterar sorvete")],
            [sg.Text("Codigo", size = (15,1)), sg.InputText(dados_sorvete["codigo_sorvete"], key="it_codigo")],
            [sg.Text("Estoque", size = (15,1)), sg.InputText(dados_sorvete["estoque_sorvete"], key="it_estoque")],
            [sg.Text("Descricao", size = (15,1)), sg.InputText(dados_sorvete["descricao_sorvete"], key="it_descricao")],
            [sg.Text("Valor", size = (15,1)), sg.InputText(dados_sorvete["valor_sorvete"], key="it_valor")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de sorvetes').Layout(layout)

        button, values = self.open()
        codigo = int(values['it_codigo'])
        estoque = int(values['it_estoque'])
        descricao = values['it_descricao']
        valor = float(values['it_valor'])

        self.close()
        return {"codigo_sorvete": codigo, "estoque_sorvete": estoque, "descricao_sorvete": descricao, "valor_sorvete": valor}

    def mostrar_sorvetes(self, dados_sorvetes):
        string_todos_sorvetes = ""
        for sorvete in dados_sorvetes:
            string_todos_sorvetes = string_todos_sorvetes + "CODIGO: " + str(sorvete["codigo_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "ESTOQUE: " + str(sorvete["estoque_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "DESCRICAO: " + str(sorvete["descricao_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "VALOR: " + str(sorvete["valor_sorvete"]) + '\n\n'

        sg.Popup('-------- LISTA DE sorveteS ----------', string_todos_sorvetes)

    def selecionar_sorvete(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- SELECIONAR sorvete ----------', font=("Helvica", 25))],
        [sg.Text('Digite o codigo do sorvete que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('Codigo:', size=(15, 1)), sg.InputText(key='it_codigo')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona sorvete').Layout(layout)

        button, values = self.open()
        codigo = values['it_codigo']
        self.close()
        return int(codigo)

    def mostrar_relatorio_de_sorvetes(self, dados_sorvetes):
        string_todos_sorvetes = ""
        for dado in dados_sorvetes:
            string_todos_sorvetes = string_todos_sorvetes + "DESCRICAO: " + str(dado["descricao_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "QUANTIDADE VENDIDA: " + str(dado["quantidade_vendida_sorvete"]) + "Kg" + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "CODIGO: " + str(dado["codigo_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "ESTOQUE: " + str(dado["estoque_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "VALOR: " + str(dado["valor_sorvete"]) + '\n\n'

        sg.Popup('-------- LISTA DE SORVETES ----------', string_todos_sorvetes)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)
