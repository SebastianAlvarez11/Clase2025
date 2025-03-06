from src.model.transacciones import Transacciones

class Usuario:
    def __init__(self, nombre: str, tipo_documento: str, numero_documento: int, contraseña: str):
        self.transacciones:list[Transacciones] = []
        pass

    def crear_transaccion(self, transaccion):
        pass
    
    def actualizar_transaccion(self):
        pass

    def ver_transacciones(self):
        pass

