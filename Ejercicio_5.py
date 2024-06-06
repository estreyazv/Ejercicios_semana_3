class Fibonacci:
    def __init__(self, numero):
        self.numero = numero

    def fibonacci(self):
        secuencia_fib = []
        a, b = 0, 1
        while len(secuencia_fib) < self.numero:
            secuencia_fib.append(a)
            a, b = b, a + b
        return secuencia_fib


numero_elegido = int(input('Escribe un número: '))
numero_elegido = Fibonacci(numero_elegido)
print('La secuencia de fibonacci del número elegido es: ', numero_elegido.fibonacci())
