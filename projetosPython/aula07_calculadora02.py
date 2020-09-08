class calculadora:
    def __init__(self):
        pass


    def soma (self, valor_a , valor_b):
        return valor_a + valor_b

    def subtracao (self, valor_a , valor_b):
        return valor_a - valor_b

    def multiplicacao (self, valor_a , valor_b):
        return valor_a * valor_b

    def divisao (self, valor_a , valor_b):
        return valor_a / valor_b

calculadora = calculadora()
print(calculadora.valor_a)
print(calculadora.soma(10, 2))
print(calculadora.subtracao(8,5))
print(calculadora.multiplicacao(9,8))
print(calculadora.divisao(100, 5))