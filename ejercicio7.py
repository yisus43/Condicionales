# Realiza un programa que calcule la potencia, para ello pide por teclado
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.


base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))


if exponente > 0:

    resultado = base ** exponente
elif exponente == 0:
 # Si el exponente es 0, el resultado es 1
    resultado = 1
else:
    # Si el exponente es negativo, calculamos la potencia y luego hacemos 1 dividido por ese resultado
    resultado = 1 / (base ** abs(exponente))

print("El resultado de", base, "elevado a", exponente, "es:", resultado)
