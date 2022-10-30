class ClienteJahExisteException(Exception):
    def __init__(self):
        super().__init__("Cliente já existe!")
