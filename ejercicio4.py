# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.

print("Programa que que pida al usuario dos números y muestre su división ")
print("si el segundo no es cero, o un mensaje de aviso en caso contrario")
num1=int(input('Ingresa el primer numero:'))
num2=int(input('Ingresa el 2 numero'))
if num2==0:
    print('No puede ser 0 cambia el numero')
else:
    print("El resultado de la division es:",num1/num2)