#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.

# Solicitar el día de la semana
dia = int(input("Introduce el día de la semana (1-7): "))

# Determinar el día correspondiente
if dia == 1:
    dia_nombre = "Lunes"
elif dia == 2:
    dia_nombre = "Martes"
elif dia == 3:
    dia_nombre = "Miércoles"
elif dia == 4:
    dia_nombre = "Jueves"
elif dia == 5:
    dia_nombre = "Viernes"
elif dia == 6:
    dia_nombre = "Sábado"
elif dia == 7:
    dia_nombre = "Domingo"
else:
    dia_nombre = None

# Mostrar el resultado
if dia_nombre is not None:
    print("El día correspondiente es:", dia_nombre)
else:
    print("ERROR: número incorrecto.")
