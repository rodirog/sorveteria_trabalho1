import PySimpleGUI as sg
class TelaLoja:

    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
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
        
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
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

    # def mostrar_tela_inicial(self):
    #     print("*" * 20)
    #     print("Sistema Vendas")
    #     print("*" * 20)
    #     print("1 - Produtos")
    #     print("2 - Clientes")
    #     print("3 - Vendedores")
    #     print("4 - Notas Fiscais")
    #     print("0 - Sair")
    #     opcao = int(input("Escolha a opcao: "))
    #     return opcao

    def mostrar_mensagem(self, msg):
        print(msg)
        print()