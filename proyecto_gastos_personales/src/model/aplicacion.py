import time
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.model.exception import (ErrorInicioSesionUsuarioNoExistente, ErrorInicioSesionContrasenaIncorrecta, ErrorInicioSesionActivo, ErrorUsuarioExistente,
                                 ErrorContrasenaIgual, ErrorIniciarSesionSinNombre, ErrorMuchosIntentosFallidos, ErrorSistemaCaido, ErrorContrasenaIntentosFallidos)

class Aplicacion:

    MAX_INTENTOS = 3 #CAMBIAR A 3 INTENTOS
    TIEMPO_BLOQUEO = 300
    def __init__(self):
        self.usuarios: list[Usuario] = []
        self.intentos_fallidos = {}
        self.tiempos_bloqueo = {}
        self.estado_usuario = None
    
    def crear_cuenta(self, usuario: Usuario):
        usuario.validar_tipo_documento(usuario.tipo_documento)
        usuario.validar_fecha_nacimiento(usuario.fecha_nacimiento)
        usuario.validar_correo(usuario.correo)
        for usuario_existe in self.usuarios:
            if usuario_existe.correo == usuario.correo:
                raise ErrorUsuarioExistente()
        self.usuarios.append(usuario)  

    def iniciar_sesion(self, nombre: str, contrasena: str):
        if not nombre and not contrasena:
            raise ErrorSistemaCaido()

        if self.intentos_fallidos.get(nombre, 0) >= Aplicacion.MAX_INTENTOS:
            raise ErrorMuchosIntentosFallidos()

        if not nombre:
            raise ErrorIniciarSesionSinNombre()

        if self.estado_usuario:
            raise ErrorInicioSesionActivo()
        
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.contrasena == contrasena:
                    self.estado_usuario = usuario
                    return True
                else:
                    self.intentos_fallidos[nombre] = self.intentos_fallidos.get(nombre, 0)+ 1
                    raise ErrorInicioSesionContrasenaIncorrecta()
        raise ErrorInicioSesionUsuarioNoExistente()

    def cambiar_contrasena(self, nueva_contrasena):
        if self.estado_usuario.contrasena == nueva_contrasena:
            raise ErrorContrasenaIgual()
        self.estado_usuario.validar_contrasena(nueva_contrasena)

        if self.intentos_fallidos.get(self.estado_usuario.nombre, 0) >= Aplicacion.MAX_INTENTOS:
            if self.tiempos_bloqueo.get(self.estado_usuario.nombre) and time.time() - self.tiempos_bloqueo[self.estado_usuario.nombre] < Aplicacion.TIEMPO_BLOQUEO:
                raise ErrorContrasenaIntentosFallidos()
            else:
                self.intentos_fallidos[self.estado_usuario.nombre] = 0
        self.estado_usuario.contrasena = nueva_contrasena
        
        self.intentos_fallidos[self.estado_usuario.nombre] = 0

        if self.estado_usuario.nombre in self.tiempos_bloqueo:
            del self.tiempos_bloqueo[self.estado_usuario.nombre]