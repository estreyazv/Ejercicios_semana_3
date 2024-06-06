
class Texto:
    def __init__(self, texto):
        self.texto = texto

    def invertir_orden(self):
        lista = self.texto.split(' ')
        lista.reverse()
        final = ' '.join(lista)
        return final

texto_escrito = input('Escribe un texto: ')
texto = Texto(texto_escrito)
print(texto.invertir_orden())