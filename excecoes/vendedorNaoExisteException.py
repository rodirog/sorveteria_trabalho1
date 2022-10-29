class VendedorNaoExisteException(Exception):
  def __init__(self):
    super().__init__("Vendedor não existe!")