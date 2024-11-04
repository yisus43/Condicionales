# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta

# Leer las opciones de los jugadores
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ")
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ")

# Determinar si las opciones son válidas
opciones_validas = ["piedra", "papel", "tijera"]

if jugador1 != "piedra":
    if jugador1 != "papel":
        if jugador1 != "tijera":
            print("Opción incorrecta.")
        else:
            jugador1_valido = True
    else:
        jugador1_valido = True
else:
    jugador1_valido = True

if jugador2 != "piedra":
    if jugador2 != "papel":
        if jugador2 != "tijera":
            print("Opción incorrecta.")
        else:
            jugador2_valido = True
    else:
        jugador2_valido = True
else:
    jugador2_valido = True

# Determinar el resultado solo si ambas opciones son válidas
if jugador1_valido and jugador2_valido:
    if jugador1 == jugador2:
        print("Empate.")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("Gana Jugador 1.")
    else:
        print("Gana Jugador 2.")
