class ErrorUsuarioExistente:
    """Excepción lanzada cuando se intenta registrar un usuario que ya existe."""
    def __init__(self):
        super().__init__(f"Error ya existe un usuario")

class ErrorTipoDocConNumeros:
    """Excepción lanzada cuando en el tipo de documento hay números."""
    def __init__(self):
        super().__init__(f"Error, no pueden haber números en el tipo de documento.")

class ErrorTipoDocConEspeciales:
    """Excepción lanzada cuando en el tipo de documento hay letras especiales."""
    def __init__(self):
        super().__init__(f"Error, no pueden haber letras especiales en el tipo de documento.")
    
class ErrorNombresConNumeros:
    """Excepción lanzada cuando en el nombre hay números."""
    def __init__(self):
        super().__init__(f"Error, no pueden haber números en el nombre.")

class ErrorNombresConEspeciales:
    """Excepción lanzada cuando en el nombre hay letras especiales."""
    def __init__(self):
        super().__init__(f"Error, no pueden haber letras especiales en el nombre.")

class ErrorNumeroDocumentoLetras:
    """Excepción lanzada cuando hay letras en el número de documento."""
    def __init__(self):
        super().__init__(f"Error, no pueden haber letras en el número de documento.")

class ErrorNumeroDocumentoEspeciales:
    """Excepción lanzada cuando en el tipo de documento hay letras especiales."""
    def __init__(self):
        super().__init__(f"Error, no pueden haber letras especiales en el tipo de documento.")
    
class ErrorTransaccion:
    pass
