from src.model.usuario import Usuario

class Aplicacion:
    def __init__(self):
        self.usuarios: list[Usuario] = []
        pass
    
    def crear_cuenta(self, usuario: Usuario):
        pass

    def iniciar_sesion(self, nombre: Usuario, contrasena: Usuario):
        pass

    def cambiar_contrasena(self, nueva_contrasena:Usuario):
        pass