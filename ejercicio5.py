# Escribe un programa que pida un nombre de usuario y una contraseña
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema",
# sino se da un error.


usuario = input("Introduce tu nombre de usuario: ")
password = input("Introduce tu contraseña: ")
if usuario == "pepe" and password == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error: Usuario o contraseña incorrectos")
