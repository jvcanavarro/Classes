# Naive Bayes com Modelo
# by elf - Eloi Favero 2018
# processamento de arquivo txt .arff
# cria modelo, baseado no domínio
# ver bayesn.y e bayesn_mod
import re
#arff_file = open("weather.nominal.arff", "r")
#arff_file = open("contact-lenses.arff", "r")
arff_file = open("zoo.arff", "r")
# Globais
dom = []
data = []  # dom(ninio)= meta dados
def remNull(Xs): return list(filter(lambda x: x != '', Xs))
#


def parseDomData(arff_f):
    dom = []
    data = []
    for line in arff_f:
        line = line.strip()  # tira brancos pontas
        line = line.lower()
        line = re.sub(r"[\n\t]*", "", line)  # tira
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

# AV=(atributo/coluna,valor)
# L=lista de AV; I=indice


def prob(data, AV):
    A, Val = AV
    I = attrI[A]
    vet = list(zip(* data))[I]
    return vet.count(Val)/len(vet)


def probC(data, AV1, AV2):  # dat as linhas AV1
    A, Val = AV1
    I = attrI[A]
    dat = [v for v in data if v[I] == Val]
    return round(prob(dat, AV2), 2)


# GLOBALS g_mod,g_clas
g_clas = attrs[-1]


def mkMod(attrV, data):
    mod = {}
    # print(clas);exit(1)
    for a in attrs[:-1]:
        vs = {}
        for v in attrV[a]:
            probCClas = [probC(data, (g_clas, vc), (a, v))
                         for vc in attrV[g_clas]]
            vs.update({v: probCClas})
        mod[a] = vs
    mod[g_clas] = [prob(data, (g_clas, vc)) for vc in attrV[g_clas]]
    return mod


# GLOBALS mod,clas
g_mod = mkMod(attrV, data)
print(g_mod)


def probM(mod, AV):
    A, V1 = AV
    if A != g_clas:
        print('erro probM')
        exit(1)
    return mod[A][attrV[g_clas].index(V1)]


def probCM(mod, AV1, AV2):
    A1, V1 = AV1
    A2, V2 = AV2
    if A1 != g_clas:
        print('erro probCM')
        exit(1)
    return mod[A2][V2][attrV[g_clas].index(V1)]


def inferModel(mod, L, AV):
    prod = 1
    for i in L:
        prod *= probCM(mod, AV, i)
    return prod*probM(mod, AV)


def classifyModel(mod, L, AV):
    a, v = AV
    xs = []
    for i in attrV[a]:
        xi = inferModel(mod, L, (a, i))
        xs.append((xi, i))
    # print(xs)
    return max(xs)[1]


# Roda para todo o arquivo
# Acuracia
D = list(attrs)[:-1]  # menos a coluna classe
CHUTE = []
ESPER = list(zip(* data))[-1]  # ultima col
for d in data:
    # print('\n',d)
    clas1 = classifyModel(g_mod, list(zip(D, d[:-1])), (g_clas, None))
    CHUTE.append(clas1)
print(CHUTE[:10])
print(ESPER[:10])

ESPxCHUT = zip(CHUTE, ESPER)
acertos = [1 for (c, e) in ESPxCHUT if c == e]
print(acertos)
print('sum acertos', sum(acertos))
print('acuracia acertos/total:', sum(acertos)/len(ESPER))
