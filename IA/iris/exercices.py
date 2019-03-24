
import numpy as np
import pandas as pd
import random
from collections import Counter
import math


inf = float(1e-20)


def rootX2(x):
    aux = 0
    for i in range(len(x)):
        aux += (x[i])**2
    return np.sqrt(aux)


def dot_product(x, y):
    return np.dot(x, y)


def cosine_distance(x, y):
    return sum(a*b for a, b in zip(x, y))/(inf+float(rootX2(x)*rootX2(y)))


def euc_distance(x, y):
    aux = 0
    for i in range(len(x)):
        aux += (x[i]-y[i])**2
    return np.sqrt(aux)


def moda(s):
    lf = Counter(s).items()
    x = sorted(lf, key=lambda x: x[1])
    return x[-1][0]


def norma(x):
    aux = 0
    for i in range(len(x)):
        aux += (x[i])**2
    return np.sqrt(aux)


def manhattan_distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


x = [6, 1, 3, 2]
y = [3, 1, 1, 4]
z = [6, 2, 2, 8]
a = [1, 2, 1]
b = [3, 1, 2]
cd = [(1, 2), (5, 6), (11, 3)]

print(list(zip(x, y)))
print(list(zip(a, b)))
c, d = zip(* cd)
print('cd:', c, d)

print('Distance X - Y:', euc_distance(x, y))
print('Distance Y - Z:', euc_distance(y, z))

print('Norma X:', norma(x))
print('Norma Y:', norma(y))

print('Moda X:', moda(x))
print('Moda Y:', moda(y))

print('Manhattan Distance X - Y:', manhattan_distance(x, y))
print('Manhattan Distance Y - Z:', manhattan_distance(x, z))

print('Euclidian Distance X - Y:', euc_distance(x, y))
print('Euclidian Distance Y - Z:', euc_distance(y, z))

print('Cosine Distance X - Y:', cosine_distance(x, y))
print('Cosine Distance Y - Z:', cosine_distance(y, z))

print('Distancia De Manhattan: é a distância entre dois pontos medidos ao longo dos eixos em ângulos retos. É frequentemente utilizada em circuitos integrados onde os fios so correm em paralelo as eixos (X, Y).\n')
print('Distancia Euclidiana: represente a distancia ''em linha reta'' entre dois pontos dentro de um espaço euclidiano. É calculada a partir da norma e o quadrado da diferença entre os pontos x-y.\n')
print('A Norma de um Vetor: representa o comprimento desse vetor, que pode ser calculado por meio da distância de seu ponto final até a origem.\n')
print('Produtor Escalar: Dados os vetores u=(a,b) e v=(c,d), definimos o produto escalar entre os vetores u e v, como o número real obtido por: u.v = a.c + b.d .\n')

print('Dot Product X - Y:', dot_product(x, y))

print('Cosine Distance X - X:', cosine_distance(x, x))
print('Manhattan Distance X- X:', manhattan_distance(x, x))
print('Euclidian Distance X - X:', euc_distance(x, x))

print('Arquivos ''Comma Separeted Values'', ou seja, arquivos com valores separados por vírgulas.\n')

print('O leitor (reader) do pacote CSV, retorna uma lista de linhas onde cada linha é uma string (F ou T)? F, segundo a documentação da biblioteca ele retorna um Reader Object, pelo qual é possivel iterar por todas as linhas do arquivo.\n')
print('O leitor (reader) do pacote CSV, retorna uma lista de listas; cada linha é uma lista de campos string (F ou T)? F, ver reposta acima.\n')

answers = ['1.a', '2.e', '3.c', '4.b', '5.a',
           '6.b', '7.a', '8.c', '9.d', '10.b']
student_answers = ['1.a', '2.b', '3.c', '4.b',
                   '5.c', '6.b', '7.a', '8.c', '9.a', '10.b']
acc = 0
for question in student_answers:
    if question in answers:
        acc += 1

print("Accuracy:", acc / len(answers))

print('random.sample(population, k) -> Return a k length list of unique elements chosen from the population sequence. Used for random sampling without replacement.\n')
print('random.shuffle(x, random) -> Shuffle method takes two parameters. Out of the two random is an optional parameter. Shuffle method used to shuffle the sequence in place. i.e., it changes the position of items in a list. We call it a randomizes the elements of a list in place.\n')

print('Range(1,10):',list(range(1, 10)), '\n')

array = [i for i in range(1, 101)]
array = random.sample(array, 100)

lista1, lista2 = array[30:], array[:30]

random.shuffle(lista1)
random.shuffle(lista2)

print('Shuffle Lista 1:', lista1, '\n')
print('Shuffle Lista 2:', lista2, '\n')

# lista1.sort(key=lambda x: x[0])
# lista1.sort(key=lambda x: x[1])
# lista1.sort(key=lambda x: x[2])
print(lista1)

print('A função array.sort() ordena um vetor em ordem crescente ou descrecente (reverse = True).\n')
print('Na função array.sort(key=lambda x: x[0]), key é uma função que será chamada para transformar a coleção de itens antes dele serem comparados, o paramêtro passado para key deve ser algo que seja callable. Na lista criada elas não conseguem iterar com x[0,1,2], no entanto a ideia seria transformar todos os itens da lista para que eles fossem iguais aos 1,2,3º itens.\n')
print('Instance-Based Learning: é uma família de algoritmos de aprendizado que compararam novas instâncias de problemas/testes com as vistas em treinamento, ao invés de comparar com as instâncias armazenadas na memória. Um exemplo de algoritmo IBL é k-nearest neighbors.\n')
print('O ''k'' em IBK significa K-Nearest Neighbors(K-NN), que significa K Vizinhos +Próximos. Nesse caso o K faz relação ao número de vizinhos mais próximos analisados, por exemplo em IBK3 nos procuramos o resultado nos 3 vizinhos mais próximos.\n')

s = [1,2,3,4,1,2,3,3,1,2,3,4,5]

print('Moda S:', moda(s))

print('A moda é necessária quando levamos em conta o conjunto que mais aparece dentro de um DataFrame, já que ela mostra o item que teve maior ocorrência. Desta forma, quando levamos em conta também a relação entre item e dataFrame, a moda é muito útil.\n')

print('A função Counter() retorna os valores de X em dicionários. Os elementos são salvos como as chaves do dicionário e sua contagem (nº de ocorrências) como os valores do dicionário\n')

print('Counter(x).keys():',Counter(x).keys())
print('Counter(x).value():',Counter(x).values())
print('Counter(x).items():',Counter(x).items())
print()

aux = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'aa']
print('Moda [''aa'', ''bb'', ..]:', moda(aux))
aux = [1,2,3,1,4,5,6,1,2,3,5,6,6,7,8,4,5,6,7]
print('Moda [1,2,3,..]:', moda(aux))