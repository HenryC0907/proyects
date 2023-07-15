import sys

abc = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27}

class cifrar:
    def __init__(self, mensaje, a, b):
        self.mensaje = mensaje
        self.__a = a
        self.__b = b

    def text_to_num(self):
        numeros = [abc[letra] for letra in self.mensaje]
        return numeros

    def transformation(self):
        numeros = self.text_to_num()
        num_cifrado = []
        if gcd(self.__a, 27) == 1: #correguir para que acepte espacios
            for i in numeros:
                x = (self.__a * i) + self.__b
                num_cifrado.append(x % 27)
            return num_cifrado
        else:
            print("El MCD de a y 27 no es 1. Programa finalizado.")
            sys.exit()

    def num_to_text(self):
        num_cifrado = self.transformation()
        text_cifrado = [letra for numero in num_cifrado for letra, valor in abc.items() if valor == numero]
        return ''.join(text_cifrado)

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

text = input('mensaje: ')
a = int(input('a: '))
b = int(input('b: '))

cifrado = cifrar(text, a, b)
print('mensaje enciptado: ' + cifrado.num_to_text())

