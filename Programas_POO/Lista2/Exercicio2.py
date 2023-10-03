class Calculadora:
    
    def Soma(self,numero1,numero2):
        resultado = (numero1+numero2)
        return resultado

    def Subtração(self,numero1,numero2):
        resultado = (numero1-numero2)
        return resultado
    
    def Multiplicação(self,numero1,numero2):
        resultado = (numero1*numero2)
        return resultado

    def Divisão(self,numero1,numero2):
        if numero2 == 0:
            print("Não é possivel dividir por 0...")
            return -1
        else:
            resultado = (numero1/numero2)
            return resultado

