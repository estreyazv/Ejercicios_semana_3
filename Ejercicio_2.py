class Numero:
    def __init__(self, entero):
        self.entero = entero
    def entero_a_romano(self):
        equivalencias = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        num_romano = ''
        for numero, letras in equivalencias:
            while self.entero >= numero:
                num_romano += letras
                self.entero -= numero
        return num_romano

entero_dado = int(input('Escribe un número entero: '))
numero_entero = Numero(entero_dado)
print(numero_entero.entero_a_romano())