import pickle

class Persistencia:
  def salvar(self):
    self.__clientes = []

#  serialização (salvar)
  clientes = ['yaka', 'adan', 'ana']
  vendedores = ['lau', 'yog', 'wan']

  sistema = {
    'clientes': clientes,
    'vendedores': vendedores
  }

  arquivo_sistema = open('sistema.pkl', 'wb')

  pickle.dump(sistema, arquivo_sistema)
  arquivo_sistema.close()

  def carregar(self):
# desserialização (carregar)
    clientes_salvos = None
    vendedores_salvos = None
    sistema_salvo = None

    arquivo_sistema_salvo = open('sistema.pkl', 'rb')
    sistema_salvo = pickle.load(arquivo_sistema_salvo)
    arquivo_sistema_salvo.close()

    clientes_salvos = sistema_salvo['clientes']
    vendedores_salvos = sistema_salvo['vendedores']

    print(sistema_salvo, clientes_salvos, vendedores_salvos)