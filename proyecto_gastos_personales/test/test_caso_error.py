import pytest
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.model.aplicacion import Aplicacion
from src.model.exception import ErrorUsuarioExistente

def caso_error1():
    with pytest.raises(ErrorUsuarioExistente):
        usuario: Usuario = Usuario("Carlos", "cedula", 23434, "Hola")
        usuario_nuevo = usuario.registrar_usuario()
        