class Criptografia:

    def __init__(self) -> None:
        pass

    
class CifraCesar(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for letra in texto:
            if letra.isalpha():
                if letra.isupper():
                    codigo = ord(letra) - ord('A')
                    codigo = (codigo + self.chave) % 26
                    letra_cifrada = chr(codigo + ord('A'))
                else:
                    codigo = ord(letra) - ord('a')
                    codigo = (codigo + self.chave) % 26
                    letra_cifrada = chr(codigo + ord('a'))
                texto_cifrado += letra_cifrada
            else:
                texto_cifrado += letra
        print(texto_cifrado)

    def decifrar(self, cifrado):
        decifrado = ""
        for letra in cifrado:
            if letra.isalpha():
                if letra.isupper():
                    codigo = ord(letra) - ord('A')
                    codigo = (codigo - self.chave) % 26
                    letra_decifrada = chr(codigo + ord('A'))
                else:
                    codigo = ord(letra) - ord('a')
                    codigo = (codigo - self.chave) % 26
                    letra_decifrada = chr(codigo + ord('a'))
                decifrado += letra_decifrada
            else:
                decifrado += letra
        print(decifrado)


class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for letra in texto:
            letra_cifrada = chr(ord(letra) ^ self.chave)
            texto_cifrado += letra_cifrada
        print(texto_cifrado)

    def decifrar(self, texto_cifrado):
        self.cifrar(texto_cifrado)

cesar = CifraCesar(2)
cesar.cifrar(input("Texto para cifrar: "))
cesar.decifrar(input("Texto para decifrar: "))


XOR = CifraXor(4)
XOR.cifrar(input("Texto para cifrar: "))
XOR.decifrar(input("Texto para decifrar: "))