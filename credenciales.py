import easygui

def obtener_credenciales_gui():
    usuario = easygui.enterbox("Ingrese su nombre de usuario:")
    contrasena = easygui.passwordbox("Ingrese su contraseña:")
    return usuario, contrasena

usuario, contrasena = obtener_credenciales_gui()
print("Nombre de usuario ingresado:", usuario)
print("Contraseña ingresada:", contrasena)