import sys

abc = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
    'L': 11, 'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
    'a': 27, 'b': 28, 'c': 29, 'd': 30, 'e': 31, 'f': 32, 'g': 33, 'h': 34, 'i': 35, 'j': 36,
    'k': 37, 'l': 38, 'm': 39, 'n': 40, 'ñ': 41, 'o': 42, 'p': 43, 'q': 44, 'r': 45, 's': 46,
    't': 47, 'u': 48, 'v': 49, 'w': 50, 'x': 51, 'y': 52, 'z': 53,
    '0': 54, '1': 55, '2': 56, '3': 57, '4': 58, '5': 59, '6': 60, '7': 61, '8': 62, '9': 63,
    ' ': 64, '!': 65, '¡': 66
}




n = len(abc)

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
        if gcd(self.__a, n) == 1:
            for i in numeros:
                x = (self.__a * i) + self.__b
                num_cifrado.append(x % n)
            return num_cifrado
        else:
            print("El MCD de a y {} no es 1. Coma mierda.".format(n))
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


