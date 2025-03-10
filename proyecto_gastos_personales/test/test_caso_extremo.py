import pytest
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.model.aplicacion import Aplicacion
from src.model.exception import (ErrorTransaccionCantidadCero, ErrorCrearTransaccionSinDatos, ErrorFechaTransaccion, ErrorHoraTransaccion,
                                 ErrorVisualizarSinFechas, ErrorIniciarSesionSinNombre, ErrorMuchosIntentosFallidos, ErrorSistemaCaido,
                                 ErrorFechaNoValida, ErrorCorreoNoValido, ErrorContrasenaNoSegura, ErrorContrasenaIntentosFallidos)

def test_transaccion_gran_cantidad_de_dinero_1():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Pepe", "cedula", 220091, "qwer123", "pepe_103@gmail.com", "09/05/1998")
    app.iniciar_sesion("Pepe", "qwer123")
    transaccion: Transacciones = Transacciones(1000000000, "salario", "30/01/2025", "10:00")
    usuario.realizar_transaccion(transaccion)
    assert len(usuario.transacciones) == 1

def test_transaccion_cero_cantidad_2():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Pepe", "cedula", 220091, "qwer123", "pepe_103@gmail.com","09/05/1998")
    app.iniciar_sesion("Pepe", "qwer123")
    transaccion: Transacciones = Transacciones(0, "salario", "30/01/2025", "10:00")
    with pytest.raises(ErrorTransaccionCantidadCero):
        usuario.realizar_transaccion(transaccion)

def test_transaccion_sin_datos_3():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "023pp", "rrio_103@gmail.com","09/05/1998")
    app.iniciar_sesion("Rio", "023pp")
    transaccion: Transacciones = Transacciones("","","","")
    with pytest.raises(ErrorCrearTransaccionSinDatos):
        usuario.realizar_transaccion(transaccion)

def test_actualizar_cero_cantidad_4():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "023pp", "rrio_103@gmail.com", "09/05/1998")
    app.iniciar_sesion("Rio", "023pp")
    transaccion: Transacciones = Transacciones(-10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(0,"comida","03/02/2025","9:45")
    with pytest.raises(ErrorTransaccionCantidadCero):
        usuario.actualizar_transaccion(nueva_transaccion)

def test_actualizar_fecha_no_valida_5():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "023pp", "rrio_103@gmail.com", "09/05/1998")
    app.iniciar_sesion("Rio", "023pp")
    transaccion: Transacciones = Transacciones(-10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(-7000,"comida","03/02/2039","9:45")
    with pytest.raises(ErrorFechaTransaccion):
        usuario.actualizar_transaccion(nueva_transaccion)
    
def test_actualizar_hora_no_valida_6():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "023pp", "rrio_103@gmail.com", "09/05/1998")
    app.iniciar_sesion("Rio", "023pp")
    transaccion: Transacciones = Transacciones(-10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(-7000,"comida","03/02/2025","39:70")
    with pytest.raises(ErrorHoraTransaccion):
        usuario.actualizar_transaccion(nueva_transaccion)

def test_visualizar_sin_fechas_7():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "023pp", "rrio_103@gmail.com", "09/05/1998")
    app.iniciar_sesion("Rio", "023pp")
    transaccion: Transacciones = Transacciones(-10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    with pytest.raises(ErrorVisualizarSinFechas):
        usuario.visualizar_transacciones("","")

def test_visualizar8():
    pass

def test_visualizar9():
    pass

def test_iniciar_sesion_sin_nombre_10():
    app: Aplicacion = Aplicacion()
    with pytest.raises(ErrorIniciarSesionSinNombre):
        app.iniciar_sesion("", "1234qwer")

def test_iniciar_sesion_muchas_veces_fallidas_11():
    app: Aplicacion = Aplicacion()
    app.iniciar_sesion("Carlos", "402390ad")
    app.iniciar_sesion("Carlos", "943u00d")
    app.iniciar_sesion("Carlos", "1234aa")
    with pytest.raises(ErrorMuchosIntentosFallidos):
        app.iniciar_sesion("Carlos", "12345as")

def test_iniciar_sesion_sistema_caido_12():
    app: Aplicacion = Aplicacion()
    nombre = "Carlos"
    contrasena = "12345as"
    with pytest.raises(ErrorSistemaCaido):
        app.iniciar_sesion(nombre, contrasena)

def test__crear_cuenta_contrasena_muy_larga_13():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Fred", "cedula", 16564532, "12345678900qwertyuiopasdfghjklñzxcvbnm", "fredd1995@gmail.com", "09/05/1998")
    lon = len(app.usuarios)
    app.crear_cuenta(usuario)
    assert len(app.usuarios) == lon+1

def test_crear_cuenta_fecha_muy_antigua_14():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Fred", "cedula", 16564532, "12345ty", "fredd1995@gmail.com", "09/05/1920")
    with pytest.raises(ErrorFechaNoValida):
        app.crear_cuenta(usuario)

def test_crear_cuenta_correo_no_valido_15():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Fred", "cedula", 16564532, "12345ty", "fredd1995gmail.com", "09/05/1920")
    with pytest.raises(ErrorCorreoNoValido):
        app.crear_cuenta(usuario)

def test_cambiar_contrasena_no_segura_16():
    app: Aplicacion = Aplicacion()
    app.iniciar_sesion("Carlos", "carlitos1_")
    nueva_contrasena = "carlos_"
    with pytest.raises(ErrorContrasenaNoSegura):
        app.cambiar_contrasena(nueva_contrasena)

def test_cambiar_contrasena_demasiados_intentos_fallidos_17():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 100043134, "carlitos1_", "carloss130@gmail.com", "10/12/2001")
    app.iniciar_sesion("Carlos", "carlitos1_")
    nueva_contrasena1 = "carlos_"
    usuario.validar_contrasena(nueva_contrasena1)
    nueva_contrasena2 = "carlos01"
    usuario.validar_contrasena(nueva_contrasena2)
    nueva_contrasena3 = "carlos9"
    usuario.validar_contrasena(nueva_contrasena3)
    with pytest.raises(ErrorContrasenaIntentosFallidos):
        app.cambiar_contrasena(nueva_contrasena3)

def test_cambiar_contrasena_solo_un_numero_18():
    app: Aplicacion = Aplicacion()
    app.iniciar_sesion("Carlos", "carlitos1_")
    nueva_contrasena = "00000000000000000"
    with pytest.raises():
        app.cambiar_contrasena(nueva_contrasena)