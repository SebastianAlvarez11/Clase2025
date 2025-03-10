from src.model.transacciones import Transacciones

class Usuario:
    def __init__(self, nombre: str, tipo_documento: str, numero_documento: int, contrasena: str, correo: str, fecha_nacimiento):
        self.transacciones:list[Transacciones] = []
        pass

    def realizar_transaccion(self, transaccion: Transacciones):
        pass
    
    def actualizar_transaccion(self, nueva_transaccion: Transacciones):
        pass

    def visualizar_transacciones(self, fecha_inicial, fecha_final):
        pass

    def validar_nombre(self):
        pass

    def validar_tipo_documento(self):
        pass

    def validar_contrasena(self, contrasena):
        pass
    
    def validar_correo(self):
        pass

    def validar_fecha_nacimiento(self):
        pass


