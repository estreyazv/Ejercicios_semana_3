class Numero:
    def __init__(self, numero):
        self.numero = numero

    def es_par(self):
        if self.numero % 2 == 0:
            print(f'El numero {self.numero} es par')

    def es_impar(self):
        if self.numero % 2 != 0:
            print(f'El numero {self.numero} es impar')



numero_escogido = int(input('Escribe un número: '))
numero = Numero(numero_escogido)
print(numero.es_par())
print(numero.es_impar())