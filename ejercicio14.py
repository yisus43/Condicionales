#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.

# Solicitar un número del 1 al 12
mes = int(input("Introduce un número del 1 al 12: "))

# Determinar el número de días del mes
if mes == 1:  # Enero
    dias = 31
elif mes == 2:  # Febrero
    dias = 28  
elif mes == 3:  # Marzo
    dias = 31
elif mes == 4:  # Abril
    dias = 30
elif mes == 5:  # Mayo
    dias = 31
elif mes == 6:  # Junio
    dias = 30
elif mes == 7:  # Julio
    dias = 31
elif mes == 8:  # Agosto
    dias = 31
elif mes == 9:  # Septiembre
    dias = 30
elif mes == 10:  # Octubre
    dias = 31
elif mes == 11:  # Noviembre
    dias = 30
elif mes == 12:  # Diciembre
    dias = 31
else:
    dias = None

# Mostrar el resultado
if dias is not None:
    print("El mes tiene", dias, "días.")
else:
    print("ERROR: número incorrecto.")
