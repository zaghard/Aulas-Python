#Conjuntos, Sub-conjuntos & Aplicações

#<-------------------------------------------------------------------->
# conjunto = {1, 2, 3, 4, 4, 2}  -----    # em conjutos não há duplicidade de elementos
# conjunto.add(5) #.add( para adiciona um elemento em um conjunto
# conjunto.discard(2) #.discard() para remover um elemento de um conjunto
# print(type(conjunto))
# print(conjunto)
#<-------------------------------------------------------------------->

conjunto = {1, 2, 3 ,4, 5}
conjunto2 = {5, 6, 7, 8}

comjunto_uniao = conjunto.union(conjunto2) #.union() para unir os elementos de um conjunto
print('União: "{}"'.format(comjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2) #.intersection() para fazer a intersecção dos elementos.
print('Interseccão: "{}"'.format(conjunto_interseccao))

conjunto_diferença1 = conjunto.difference(conjunto2)
conjunto_diferença2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: "{}"'.format(conjunto_diferença1))
print('Diferença entre 2 e 1: "{}"'.format(conjunto_diferença2))

conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simétrica: "{}"'.format(conjunto_dif_simetrica))

#<-------------------------------------------------------------------->

conjunto_a = {1, 2, 3, 4}
conjunto_b = {1, 2, 3, 4, 5, 6}

conjunto_subset = conjunto_a.issubset(conjunto_b) #.issubset() verifica se um conjunto é sub-conjunto de outro
print('A é um subconjunto de B:"{}"'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)#.issuperset() verfica se um conjunto é super-conjunto de outro
print('B é um superconjunto de A:"{}"'.format(conjunto_superset))

#<-------------------------------------------------------------------->
# Conventendo lista em conjunto e removendo duplicidade
lista = ['cachorro','gato','gato', 'elefante']

conjunto_ani =set(lista)
print(conjunto_ani)

lista_ani = list(conjunto_ani)
print(lista_ani)
lista_ani.sort()
print(lista_ani)