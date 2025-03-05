from src.model.transacciones import Transacciones

class Usuario:
    def __init__(self, nombre: str, tipo_documento: int, numero_documento: int, contraseña: str):
        self.transacciones:list[Transacciones] = []
        pass

    def actualizar_transaccion(self):
        pass

    def ver_transacciones(self):
        pass

