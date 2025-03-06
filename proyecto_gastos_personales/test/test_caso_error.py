import pytest
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.model.aplicacion import Aplicacion
from src.model.exception import ErrorUsuarioExistente

def test_caso_error1():
    with pytest.raises(ErrorUsuarioExistente):
        app: Aplicacion = Aplicacion()
        usuario: Usuario = Usuario("Carlos", "cedula", 23434, "Hola")
        pass  
        
        