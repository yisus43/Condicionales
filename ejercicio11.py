#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un programa para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.

# Solicitar la duración de la llamada en minutos
duracion = int(input("Introduce la duración de la llamada en minutos: "))

# Calcular el costo de la llamada
if duracion <= 5:
    costo = 1.0
elif duracion <= 8:
    costo = 1.0 + (duracion - 5) * 0.80
elif duracion <= 10:
    costo = 1.0 + 3 * 0.80 + (duracion - 8) * 0.70
else:
    costo = 1.0 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

# Solicitar el día y el turno
dia = input("Introduce el día de la semana (Domingo/Semana): ")
turno = input("Introduce el turno (mañana/tarde): ")

# Calcular el impuesto
if dia.lower() == 'domingo':
    impuesto = costo * 0.03
else:
    if turno.lower() == 'mañana':
        impuesto = costo * 0.15
    else:
        impuesto = costo * 0.10

# Calcular el costo total
costo_total = costo + impuesto

# Mostrar el resultado
print("Costo total a pagar: {:.2f} euros".format(costo_total))
