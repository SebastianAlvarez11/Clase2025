from src.model.aplicacion import Aplicacion

class UIConsola:
    
    def menu(self):
        app = Aplicacion()
        while True:
            print("\n--- Gestión gastos personales ---")
            print("1.  Crear Cuenta")
            print("2. Iniciar Sesión")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre: ")
                tipo_documento =  input("Ingrese el tipo de documento: ") 
                numero_documento = input("Ingrese el número de documento: ")
                contrasena = input("Ingrese la contraseña: ")
                correo = input("Ingrese el correo: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento(dd/mm/yyyy): ")
                app.crear_cuenta(nombre, tipo_documento, numero_documento, contrasena, correo, fecha_nacimiento)
                print("Usuario registrado con éxito.")

            if opcion == "2":
                nombre = input("Ingrese el nombre: ")
                contrasena = input("Ingrese la contraseña: ")

