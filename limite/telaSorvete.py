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

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
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

     # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostrar_sorvetes(self, dados_sorvetes):
        string_todos_sorvetes = ""
        for sorvete in dados_sorvetes:
            string_todos_sorvetes = string_todos_sorvetes + "CODIGO: " + str(sorvete["codigo_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "ESTOQUE: " + str(sorvete["estoque_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "DESCRICAO: " + str(sorvete["descricao_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "VALOR: " + str(sorvete["valor_sorvete"]) + '\n\n'

        sg.Popup('-------- LISTA DE sorveteS ----------', string_todos_sorvetes)

     # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
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

    # def mostrar_relatorio_de_bebidas(self, dados_bebidas):
    #     string_todas_bebidas = ""
    #     for dado in dados_bebidas:
    #         string_todas_bebidas = string_todas_bebidas + "DESCRICAO: " + str(dado["descricao_bebida"]) + '\n'
    #         string_todas_bebidas = string_todas_bebidas + "QUANTIDADE VENDIDA: " + str(dado["quantidade_vendida_bebida"]) + " unidade(s)" + '\n'
    #         string_todas_bebidas = string_todas_bebidas + "CODIGO: " + str(dado["codigo_bebida"]) + '\n'
    #         string_todas_bebidas = string_todas_bebidas + "ESTOQUE: " + str(dado["estoque_bebida"]) + '\n'
    #         string_todas_bebidas = string_todas_bebidas + "VALOR: " + str(dado["valor_bebida"]) + '\n\n'

    #     sg.Popup('-------- LISTA DE BEBIDAS ----------', string_todas_bebidas)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)


    # def pegar_dados_sorvete(self):
    #     print()
    #     print("CADASTRO sorvete")
    #     codigo_sorvete = int(input("Codigo do sorvete: "))
    #     estoque_sorvete = int(input("Estoque do sorvete: "))
    #     descricao_sorvete = str(input("Descricao do sorvete: "))
    #     tipo_sorvete = int(input("Tipo do sorvete (insira '1' para sorvete ou '2' para bebida): "))
    #     valor_sorvete = float(input("Valor do sorvete: "))

    #     return {"codigo_sorvete": codigo_sorvete, "estoque_sorvete": estoque_sorvete, "descricao_sorvete": descricao_sorvete, "tipo_sorvete": tipo_sorvete, "valor_sorvete": valor_sorvete}

    # def alterar_dados_sorvete(self):
    #     print()
    #     print("ALTERAR sorvete")
    #     codigo_sorvete = int(input("Codigo do sorvete: "))
    #     estoque_sorvete = int(input("Estoque do sorvete: "))
    #     descricao_sorvete = str(input("Descricao do sorvete: "))
    #     valor_sorvete = float(input("Valor do sorvete: "))

    #     return {"codigo_sorvete": codigo_sorvete, "estoque_sorvete": estoque_sorvete, "descricao_sorvete": descricao_sorvete, "valor_sorvete": valor_sorvete}

    # def mostrar_sorvete(self, dados_sorvete):
    #     print()
    #     print("sorvete")
    #     print(f"Codigo: {dados_sorvete['codigo_sorvete']}")
    #     print(f"Estoque: {dados_sorvete['estoque_sorvete']}")
    #     print(f"Descricao: {dados_sorvete['descricao_sorvete']}")
    #     print(f"Tipo: {dados_sorvete['tipo_sorvete']}")
    #     print(f"Valor: {dados_sorvete['valor_sorvete']}")
    #     print()

    # def selecionar_sorvete(self):
    #     print()
    #     codigo = int(input("Insira o codigo do sorvete que deseja selecionar: "))
    #     return codigo



    # def mostrar_relatorio_de_bebidas(self, dados_bebida):
    #     print()
    #     print("BEBIDA")
    #     print(f"Quantidade total vendida: {dados_bebida['quantidade_vendida_sorvete']} unidade(s)")
    #     print(f"Codigo: {dados_bebida['codigo_sorvete']}")
    #     print(f"Estoque: {dados_bebida['estoque_sorvete']}")
    #     print(f"Descricao: {dados_bebida['descricao_sorvete']}")
    #     print(f"Valor: {dados_bebida['valor_sorvete']}")
    #     print()

