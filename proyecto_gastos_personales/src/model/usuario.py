import string
from datetime import datetime, timedelta
from src.model.transacciones import Transacciones
from src.model.exception import (ErrorTipoDocConNumeros, ErrorTipoDocConEspeciales, ErrorContrasenaCorta, ErrorContrasenaVacia, ErrorTransaccionSinLoguearse,
                                 ErrorTransaccionNoExistente, ErrorTransaccionSinCambios, ErrorVisualizarSinLoguearse, ErrorVisualizarFechaInicialPosterior,
                                 ErrorVisualizarFechasFormato, ErrorTransaccionCantidadCero, ErrorCrearTransaccionSinDatos, ErrorFechaNoValida,
                                 ErrorCorreoNoValido, ErrorContrasenaNoSegura, ErrorVisualizarSinFechas, ErrorVisualizarSinFechaInicial, ErrorVisualizarSinFechaFinal)

class Usuario:
    def __init__(self, nombre: str, tipo_documento: str, numero_documento: int, contrasena: str, correo: str, fecha_nacimiento):
        self.transacciones:list[Transacciones] = []
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.contrasena = contrasena
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento

    def realizar_transaccion(self, transaccion: Transacciones):
        if transaccion.cantidad_dinero == 0:
            raise ErrorTransaccionCantidadCero()
        if not transaccion.cantidad_dinero or not transaccion.categoria or not transaccion.fecha or not transaccion.hora:
            raise ErrorCrearTransaccionSinDatos()
        transaccion.validar_fecha()
        transaccion.validar_hora()
        transaccion.validar_dinero()
        self.transacciones.append(transaccion)
    
    def actualizar_transaccion(self, nueva_transaccion: Transacciones):
        if nueva_transaccion.cantidad_dinero == 0:
            raise ErrorTransaccionCantidadCero()
    
        nueva_transaccion.validar_fecha()
        nueva_transaccion.validar_hora()

        for i in range(len(self.transacciones)):
            transaccion_actual = self.transacciones[i]
            if (transaccion_actual.categoria == nueva_transaccion.categoria and
                transaccion_actual.fecha == nueva_transaccion.fecha and
                transaccion_actual.hora == nueva_transaccion.hora):
                if (transaccion_actual.cantidad_dinero == nueva_transaccion.cantidad_dinero):
                    raise ErrorTransaccionSinCambios() 
                
            for transaccion in self.transacciones:
                if transaccion.id == nueva_transaccion.id:
                    transaccion.cantidad_dinero = nueva_transaccion.cantidad_dinero
                    transaccion.categoria = nueva_transaccion.categoria
                    transaccion.fecha = nueva_transaccion.fecha
                    transaccion.hora = nueva_transaccion.hora 
                    return True
            
        raise ErrorTransaccionNoExistente()
        

    def visualizar_transacciones(self, fecha_inicial, fecha_final):  
        if fecha_inicial == "" and fecha_final == "":
            raise ErrorVisualizarSinFechas()
        
        if not fecha_inicial:
            raise ErrorVisualizarSinFechaInicial()
        
        if not fecha_final:
            raise ErrorVisualizarSinFechaFinal()
        
        if fecha_inicial > fecha_final:
            raise ErrorVisualizarFechaInicialPosterior()
        
        try:
            fecha_inicial = datetime.strptime(fecha_inicial, "%d/%m/%Y")
            fecha_final = datetime.strptime(fecha_final, "%d/%m/%Y")
        except:
            raise ErrorVisualizarFechasFormato()
        
        transacciones_filtradas = [
            transaccion for transaccion in self.transacciones
            if transaccion.filtrar_fechas(fecha_inicial, fecha_final)
        ]
        return transacciones_filtradas

    def validar_nombre(self):
        pass

    def validar_tipo_documento(self, tipo_documento):
        if any(char.isdigit() for char in tipo_documento):
            raise ErrorTipoDocConNumeros()
        if any(char in string.punctuation for char in tipo_documento):
            raise ErrorTipoDocConEspeciales()

    def validar_contrasena(self, contrasena):
        if contrasena == "":
            raise ErrorContrasenaVacia()
        if len(contrasena) < 8:
            raise ErrorContrasenaCorta()
        if not any(char.isdigit() for char in contrasena):
            raise ErrorContrasenaNoSegura()
        if not any(char.isupper() for char in contrasena):
            raise ErrorContrasenaNoSegura()
        if not any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/~`' for char in contrasena):
            raise ErrorContrasenaNoSegura()
        return True

    def validar_correo(self, correo):
        if '@' not in correo or '.' not in correo.split('@')[-1]:
            raise ErrorCorreoNoValido()

    def validar_fecha_nacimiento(self, fecha_nacimiento):
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            if fecha_nacimiento > datetime.now():
                raise ErrorFechaNoValida()
            
            edad = datetime.now() - fecha_nacimiento
            if edad > timedelta(days=100 * 365):
                raise ErrorFechaNoValida()
            return True
        except:
            raise ErrorFechaNoValida()
        

        


