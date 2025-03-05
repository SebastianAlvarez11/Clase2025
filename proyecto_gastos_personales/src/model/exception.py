class ErrorUsuarioExistente:
    """Excepción lanzada cuando se intenta registrar un usuario que ya existe."""
    def __init__(self):
        super().__init__(f"Error ya existe un usuario")