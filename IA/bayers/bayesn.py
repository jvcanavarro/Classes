# Naive Bayes
# by elf - Eloi Favero 2018
# processamento de arquivo txt .arff
# extrai os metadados do arquivo
# extrai dados não numéricos
# usa modulo expressões regulares = re
# usa funções alta ordem: filter(), map(), lambda, eval(), zip()
#
import re
arff_file = open("weather.nominal.arff", "r")
# Globais
dom = []
data = []  # dom(ninio)= meta dados

# filter()=lazy=preguiçosa=>retorna iterable; list=>força execução


def remNull(Xs): return list(filter(lambda x: x != '', Xs))


#print( list(filter(lambda x:x!=3, [3,4,5,6,3,4,5,6])) );exit(1)
#print( remNull([1,'12', '', '', 'a', '','','']));exit(1)
#print("1 12 1 a aa aaa aaaaa    aaa   ".split());
#print(re.split('@|,|{|}| ', " attrVibute play {yes, no}"));exit(1)
#
# string in-line para testar
lll = '''
@relation weather.symbolic
   @attrVibute outlook {sunny, overcast, rainy}
@attrVibute play {yes, no}

@data
sunny,hot,high,TRUE,no
overcast,hot,high, FALSE, yes
'''.split('\n')


def parseDomData(arff_f):
    dom = []
    data = []
    for line in arff_f:
        line = line.strip()                   # tira brancos
        line = line.strip("\n")
        if(line.startswith("%")):
            continue  # comentario
        if (line.startswith("@")):          # meta dados = dom(inio)
            line = re.split('@|,|{|}| ', line)
            line = remNull(line)
            if line != []:
                dom.append(line)
        else:                               # instancia dados
            line = re.split(';|,|{|}| ', line)
            line = remNull(line)
            if line != []:
                data.append(line)
    return (dom, data)


# print(parseDomData(lll));exit(1)
'''    
[['relation', 'weather.symbolic'],
 ['attrVibute', 'outlook', 'sunny', 'overcast', 'rainy'],
 ['attrVibute', 'play', 'yes', 'no'],
 ['data']],
[['sunny', 'hot', 'high', 'TRUE', 'no'],
 ['overcast', 'hot', 'high', 'FALSE', 'yes']]
'''

dom, data = parseDomData(arff_file)
# apaga linhas
if dom[0][0] == 'relation':
    del dom[0]
if dom[-1][0] == 'data':
    del dom[-1]
# print(dom);exit(1)
#
attrV = {}  # {atributo: [valores] }
attrI = {}  # {(nome :indice) das coluna}
#
for at in dom:
    attrV[at[1]] = at[2:]
attrs = [at[1] for at in dom]
attrI = dict(zip(attrs, range(len(attrV))))
#print(attrV); print(attrI);exit(1)

'''
    {'outlook': ['sunny', 'overcast', 'rainy'],
     'temperature': ['hot', 'mild', 'cool'],
     'humidity': ['high', 'normal'],
     'windy': ['TRUE', 'FALSE'],
     'play': ['yes', 'no']} 
 {'outlook': 0, 'temperature': 1, 'humidity': 2, 'windy': 3, 'play': 4}
'''

# AV=(atributo/coluna,valor)
# L=lista de AV; I=indice


def prob(data, AV):
    A, Val = AV
    I = attrI[A]
    vet = list(zip(* data))[I]
    # print(vet.count(Val),'/',len(vet))
    return vet.count(Val)/len(vet)
# print(prob(data,('outlook','sunny')))
# print(prob(data,('play','yes')))


def probC(data, AV1, AV2):  # dat as linhas AV1
    I, Val = AV1
    I = attrI[I]
    dat = [v for v in data if v[I] == Val]
    return prob(dat, AV2)


print(probC(data, ('play', 'yes'), ('outlook', 'sunny')))


def inferNBayes(data, L, AV):
    prod = 1
    for i in L:
        prod *= probC(data, AV, i)
    return prod*prob(data, AV)
#
# o parametro V do AV não é considerado


def classifyNBayes(data, L, AV):
    a, v = AV
    xs = []
    for i in attrV[a]:
        xi = inferNBayes(data, L, (a, i))
        xs.append((xi, i))
    # print(xs)
    return max(xs)


L1 = [('outlook', 'sunny'), ('temperature', 'cool'),
      ('humidity', 'high'), ('windy', 'TRUE')]
L2 = [('outlook', 'rainy'), ('temperature', 'cool'),
      ('humidity', 'high'), ('windy', 'FALSE')]
print()
print(inferNBayes(data, L1, ('play', 'yes')))
print(inferNBayes(data, L1, ('play', 'no')))
print(inferNBayes(data, L2, ('play', 'yes')))
print(inferNBayes(data, L2, ('play', 'no')))

# Roda para todo o arquivo
D = attrs[:-1]  # menos a coluna classe
predit = []
real = list(zip(* data))[-1]
print(real)
exit(1)
for i in range(len(data)):
    d = data[i]
    print('\n\n', d)
    print(classifyNBayes(data, list(zip(D, d[:-1])), ('play', 'yes')))
