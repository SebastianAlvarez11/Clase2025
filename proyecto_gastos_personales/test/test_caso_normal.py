import pytest
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.model.aplicacion import Aplicacion

def test_caso_normal_1():
    app : Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 23434, "Hola")
    lon = len(app.usuarios)
    app.registrar_usuario(usuario)
    assert len(app.usuarios) == lon+1

def test_caso_normal_2():
    transaccion: Transacciones = Transacciones(20000, "pago deuda", "05/03/2025", "10:30")
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "mdsse")
    lon = len(usuario.transacciones)
    usuario.crear_transaccion(transaccion)
    assert len(usuario.transacciones) == 1

def test_caso_normal_3():
    pass