class ErrorInicioSesionContrasenaIncorrecta(Exception):
    """Excepción lanzada cuando al iniciar sesión la contraseña es incorrecta."""
    def __init__(self):
        super().__init__(f"Error, contraseña incorrecta.")

class ErrorInicioSesionUsuarioNoExistente(Exception):
    """Excepción lanzada cuando se intenta iniciar sesión con un usuario que no existe."""
    def __init__(self):
        super().__init__(f"Error, no existe un usuario registrado.")

class ErrorInicioSesionActivo(Exception):
    """Excepción lanzada cuando intenta iniciar sesión cuando el usuario ya está autenticado."""
    def __init__(self):
        super().__init__(f"Error, el usuario ya está autenticado.")

class ErrorUsuarioExistente(Exception):
    """Excepción lanzada cuando se intenta registrar un usuario que ya existe."""
    def __init__(self):
        super().__init__(f"Error, el usuario ya existe.")

class ErrorTipoDocConNumeros(Exception):
    """Excepción lanzada cuando en el tipo de documento hay números."""
    def __init__(self):
        super().__init__(f"Error, no pueden haber números en el tipo de documento.")

class ErrorTipoDocConEspeciales(Exception):
    """Excepción lanzada cuando en el tipo de documento hay letras especiales."""
    def __init__(self):
        super().__init__(f"Error, no pueden haber letras especiales en el tipo de documento.")
    
class ErrorFechaTransaccion(Exception):
    """Excepción lanzada cuando la fecha de la transacción no es válida."""
    def __init__(self):
        super().__init__(f"Error, la fecha de la transacción no es válida.")
    
class ErrorCrearTransaccionSinDatos(Exception):
    """Excepción lanzada cuando se quiere crear una transacción sin datos."""
    def __init__(self):
        super().__init__(f"Error al crear transacción, faltan datos.")

class ErrorHoraTransaccion(Exception):
    """Excepción lanzada cuando la hora de la transacción no es válida."""
    def __init__(self):
        super().__init__(f"Error, la hora de la transacción no es válida.")

class ErrorContrasenaCorta(Exception):
    """Excepción lanzada cuando se intenta cambiar la contraseña por una muy corta."""
    def __init__(self):
        super().__init__(f"Error, la contraseña es muy corta, intentelo nuevamente.")

class ErrorContrasenaIgual(Exception):
    """Excepción lanzada cuando se intenta cambiar la contraseña por la misma que tenia el usuario."""
    def __init__(self):
        super().__init__(f"Error, no se puede cambiar la contraseña ya que es igual a la contraseña antigua.")

class ErrorContrasenaVacia(Exception):
    """Excepción lanzada cuando se intenta cambiar la contraseña por una contraseña vacía."""
    def __init__(self):
        super().__init__(f"Error, no se puede cambiar la contraseña por una contraseña vacía.")

class ErrorTransaccionSinLoguearse(Exception):
    """Excepción lanzada cuando se intenta actualizar una transacción sin haber iniciado sesión."""
    def __init__(self):
        super().__init__(f"Error, debe iniciar sesión para poder actualizar una transacción.")

class ErrorTransaccionNoExistente(Exception):
    """Excepción lanzada cuando se intenta actualizar una transacción no existente."""
    def __init__(self):
        super().__init__(f"Error, no existe una transacción.")

class ErrorTransaccionSinCambios(Exception):
    """Excepción lanzada cuando se intenta actualizar una transacción sin cambios."""
    def __init__(self):
        super().__init__(f"Error, la transacción nueva no tiene cambios.")

class ErrorVisualizarSinLoguearse(Exception):
    """Excepción lanzada cuando se intenta visualizar transacciones sin iniciar sesión."""
    def __init__(self):
        super().__init__(f"Error, debe iniciar sesión para poder visualizar las transacciones.")

class ErrorVisualizarFechaInicialPosterior(Exception):
    """Excepción lanzada cuando se intenta visualizar transacciones con una fecha inicial posterior a la fecha final."""
    def __init__(self):
        super().__init__(f"Error, la fecha inicial debe ser antes de la fecha final.")

class ErrorVisualizarFechasFormato(Exception):
    """Excepción lanzada cuando se intenta visualizar transacciones con una fecha en un formato que no es válido."""
    def __init__(self):
        super().__init__(f"Error, las fechas deben ir en un formato válido.")

class ErrorTransaccionCantidadCero(Exception):
    """Excepción lanzada cuando se intenta crear una transacción con 0 cantidad de dinero."""
    def __init__(self):
        super().__init__(f"Error, la cantidad de dinero debe ser diferente a 0.")

class ErrorTransaccionCantidaConLetras(Exception):
    """Excepción lanzada cuando se intenta crear una transacción con letras en la cantidad de dinero."""
    def __init__(self):
        super().__init__(f"Error, la cantidad de dinero no debe contener letras.")

class ErrorVisualizarSinFechas(Exception):
    """Excepción lanzada cuando se intenta visualizar transacciones con fechas vacías."""
    def __init__(self):
        super().__init__(f"Error, no se pueden visualizar transacciones sin unas fechas específicas.")

class ErrorVisualizarSinFechaInicial(Exception):
    """Excepción lanzada cuando se intenta visualizar transacciones sin fecha inicial."""
    def __init__(self):
        super().__init__(f"Error, no se pueden visualizar transacciones sin una fecha inicial.")

class ErrorVisualizarSinFechaFinal(Exception):
    """Excepción lanzada cuando se intenta visualizar transacciones sin fecha final."""
    def __init__(self):
        super().__init__(f"Error, no se pueden visualizar transacciones sin una fecha final.")

class ErrorIniciarSesionSinNombre(Exception):
    """Excepción lanzada cuando se intenta iniciar sesión solo con la contraseña."""
    def __init__(self):
        super().__init__(f"Error, no se puede iniciar sesión sin un nombre.")

class ErrorMuchosIntentosFallidos(Exception):
    """Excepción lanzada cuando se intenta iniciar sesión y hay muchos intentos fallidos."""
    def __init__(self):
        super().__init__(f"Error, demasiados intentos fallidos, usuario bloqueado.")

class ErrorSistemaCaido(Exception):
    """Excepción lanzada cuando el sistema esta caído."""
    def __init__(self):
        super().__init__(f"Error, por favor intente más tarde.")

class ErrorFechaNoValida(Exception):
    """Excepción lanzada cuando se intenta crear una cuenta con fecha de nacimieto de 1920 hacia abajo, tendria más de 105 años."""
    def __init__(self):
        super().__init__(f"Error, la edad es demasiado avanzada.")

class ErrorCorreoNoValido(Exception):
    """Excepción lanzada cuando se intenta crear una cuenta con un correo sin @."""
    def __init__(self):
        super().__init__(f"Error, el correo debe contener @.")

class ErrorContrasenaNoSegura(Exception):
    """Excepción lanzada cuando se intenta cambiar la contraseña por una no segura."""
    def __init__(self):
        super().__init__(f"Error, la contraseña debe contener al menos un número, una letra y una letra especial.")

class ErrorContrasenaIntentosFallidos(Exception):
    """Excepción lanzada cuando se intenta cambiar la contraseña con muchos intentos fallidos."""
    def __init__(self):
        super().__init__(f"Error, demasiados intentos fallidos, intente más tarde.")


