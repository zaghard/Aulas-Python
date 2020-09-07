#Condicionais: IF- ELSE - ELIF
# operadores lógicos: AND - OR - NOT

#<-------------------------------------------------------------------->
''' int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print("O valor valor foi {}".format(a))
elif b > a and b > c:
    print('O maior valor foi {}'.format(b))
else:
    print('O maior número é: {}'.format(c))
print("Final do Programa")'''
#<-------------------------------------------------------------------->
# a = int(input('Entre com um valor: '))
# b = int(input('Entre com um valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('O número é par')
# else:
#     print('O número é impar')
# print('Fim do programa')
#<-------------------------------------------------------------------->
a = int(input('Primeira avaliação: '))
if a > 10:
    a = int(input('Você digitou errado...Digite Primeira avaliação: '))
b = int(input('Segunda avaliação: '))
if b > 10:
    b = int(input('Você digitou errado...Digite Segunda avaliação: '))
c = int(input('Terceira avaliação: '))
if c > 10:
    c = int(input('Você digitou errado...Digite Terceira avaliação: '))
d = int(input('Quarta avaliação: '))
if d > 10:
    d = int(input('Você digitou errado...Digite Quarta avaliação: '))
media =(a + b + c + d) / 4
print('media: {}'.format(media))
#<-------------------------------------------------------------------->
# if a <= 10 and b <= 10 and c <= 10 and  d <= 10:
# print('media: {}'.format(media))
# else:
#     print('Foi informado nota com valor errado!!!')
#<-------------------------------------------------------------------->
if media >= 7.0:
    print('O aluno foi aprovado!!!')
else:
    print('O aluno foi reprovado!!!!')
print('Fim do programa!!!')