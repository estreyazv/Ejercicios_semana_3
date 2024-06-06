def cifrar_cesar(texto, clave):
    resultado = []
    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                posicion_inicial = ord('A')
            else:
                posicion_inicial = ord('a')
            desplazamiento = (ord(caracter) - posicion_inicial + clave) % 26
            nuevo_caracter = chr(posicion_inicial + desplazamiento)
            resultado.append(nuevo_caracter)
        else:
            resultado.append(caracter)
    return ''.join(resultado)

def descifrar_cesar(texto, clave):
    return cifrar_cesar(texto, -clave)

# Inicio del programa principal

print('Escoge una opción:')
print('1. Cifrar texto en César')
print('2. Descifrar texto desde César')

opcion_escogida = int(input(': '))

clave = 3
if opcion_escogida == 1:
    texto_en_cesar = input('Escribe el texto: ')
    texto_cifrado = cifrar_cesar(texto_en_cesar, clave)
    print(f"Texto cifrado: {texto_cifrado}")

elif opcion_escogida == 2:
    texto_legible = input('Escribe el texto: ')
    texto_descifrado = descifrar_cesar(texto_legible, clave)
    print(f"Texto descifrado: {texto_descifrado}")

else:
    print('El valor introducido no es correcto, introduce un valor válido')