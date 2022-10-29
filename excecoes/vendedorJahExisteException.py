class VendedorJahExisteException(Exception):
  def __init__(self):
    super().__init__("Vendedor já existe!")