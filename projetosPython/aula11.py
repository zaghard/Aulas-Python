
lista = [1, 10]

try:
    arquivo = open('text.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[3]

    print('Fechando arquivo')
    arquivo.close()

except ZeroDivisionError:
    print('Não é possível realizar divi~sao por 0')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro:"{}"'.format(ex))
else:
    print('Excuta quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
