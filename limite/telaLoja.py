import PySimpleGUI as sg
class TelaLoja:

    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        opcao = None
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema de vendas!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Sorvetes',"RD1", key='1')],
            [sg.Radio('Bebidas',"RD1", key='2')],
            [sg.Radio('Clientes',"RD1", key='3')],
            [sg.Radio('Vendedores',"RD1", key='4')],
            [sg.Radio('Notas Fiscais',"RD1", key='5')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de vendas').Layout(layout)

    def mostrar_mensagem(self, msg):
        print(msg)
        print()