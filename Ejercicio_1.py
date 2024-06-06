
class Romano:
    def __init__(self, numero):
        self.numero = numero

    def romano_a_entero(self):
        valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        entero = 0
        valor_anterior = 0
        for letra in reversed(self.numero):
            valor_actual = valores[letra]
            if valor_actual < valor_anterior:
                entero -= valor_actual
            else:
                entero += valor_actual
            valor_anterior = entero
        return entero

numero_romano_elegido = input('Escribe un número romano: ').upper()
numero_romano = Romano(numero_romano_elegido)
print(numero_romano.romano_a_entero())
