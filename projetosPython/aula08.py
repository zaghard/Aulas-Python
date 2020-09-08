#Modulos e funções lambida
from aula07_televisao import Televisao
from aula07_calculadora01 import Calculadora
from aula08_pc_palavras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(10,2)
    print(calculadora.valor_a)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras= contador_letras(lista)
    print('Total de letras por palavra da lista:"{}"'.format(total_letras))
