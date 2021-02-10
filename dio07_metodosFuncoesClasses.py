# funções: retorna valor
# metodos: não retorna valor - em python são definições

# definição : método

class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return(self.a+self.b)
    def subtacao(self):
        return(self.a-self.b)
    def produto(self):
        return(self.a*self.b)
    def divisao(self):
        return(self.a//self.b)
    def resto(self):
        return(self.a%self.b)

# Instanciar
calculadora = Calculadora(5,3)
print(calculadora.soma())
print(calculadora.subtacao())
print(calculadora.produto())
print(calculadora.divisao())
print(calculadora.resto())



class Calculadora2:
    def __init__(self):
        pass

    def soma(self,a,b):
        return(a+b)
    def subtacao(self,a,b):
        return(a-b)
    def produto(self,a,b):
        return(a*b)
    def divisao(self,a,b):
        return(a//b)
    def resto(self,a,b):
        return(a%b)

# Instanciar
calculadora = Calculadora2()
print(calculadora.soma(7,4))
print(calculadora.subtacao(7,4))
print(calculadora.produto(7,4))
print(calculadora.divisao(7,4))
print(calculadora.resto(7,4))
