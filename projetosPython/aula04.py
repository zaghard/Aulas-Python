#Laços de repetição: Comandos FOR - WHILE - RANGE
a = int(input('Primeira avaliação: '))
while a > 10:
    a = int(input('Você digitou errado...Digite Primeira avaliação: '))
b = int(input('Segunda avaliação: '))
while b > 10:
    b = int(input('Você digitou errado...Digite Segunda avaliação: '))
c = int(input('Terceira avaliação: '))
while c > 10:
    c = int(input('Você digitou errado...Digite Terceira avaliação: '))
d = int(input('Quarta avaliação: '))
while d > 10:
    d = int(input('Você digitou errado...Digite Quarta avaliação: '))
media =(a + b + c + d) / 4
print('media: {}'.format(media))



#<-------------------------------------------------------------------->
# nota = int(input('Entre com uma nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida! -- Entre com uma nota correta: '))
#     print(nota)

#<-------------------------------------------------------------------->
# a = 0
# while a < 10:
#     print(a)
#     a += 1

#<-------------------------------------------------------------------->
# a = int(input('Entre com o número: '))
# div = 0
# for x in range (1, a+1):
#    resto = a % x
#    print(x, resto)
#    if resto == 0
#        div  += 1
#        #div = div + 1
#
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))

#<-------------------------------------------------------------------->

# a = int(input('Entre com um valor: '))
#
# for num in range (a+1):
#     div = 0
#     for x in range (1, num+1):
#        resto = num % x
#        #print(x, resto)
#        if resto == 0:
#            div  += 1
#            #div = div + 1
#
#     if div == 2:
#         print(num)
# <------------------------------------------------------------------->
