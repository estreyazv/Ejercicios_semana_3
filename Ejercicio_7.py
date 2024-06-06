import random

def opcion_escogida(num_ordenador):

    if num_ordenador == 1:
        opcion = 'Papel'
    elif num_ordenador == 2:
        opcion = 'Tijera'
    else:
        opcion = 'Piedra'
    return opcion


# Comienzo del programa principal

print('Escoge una opción: ')
print('1. Papel')
print('2. Tijera')
print('3. Piedra')

jugador = int(input("Elige un número: "))
ordenador = random.randint(1, 3)


# Juego
if jugador == ordenador:
    print("Empate. Ambos eligieron", opcion_escogida(ordenador))
elif (jugador == 1 and ordenador == 3) or (jugador == 2 and ordenador == 1) or (jugador == 3 and ordenador == 2):
    print('Has ganado. El ordenador escogió: ',opcion_escogida(ordenador))
else:
    print('Has perdido. El ordenador escogió:', opcion_escogida(ordenador))