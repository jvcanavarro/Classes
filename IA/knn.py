### KNN em python em 100 linhas by elf
### knn.py => iris.csv

from collections import Counter
import random
from csv import reader
from math import sqrt
inf=10**-20
def moda(s):
    #print(s)
    lf=Counter(s).items()
    x=sorted(lf,key=lambda x: x[1])
    return x[-1][0]

### medidas de distancia e similaridade em vetores
def euclD(x,y):return round(sqrt(sum(pow(a-b,2) for a, b in zip(x, y))),3)
def manhD(x,y):return round(sum(abs(a-b) for a,b in zip(x,y)),3)
def rootX2(x ):return round(sqrt(sum([a*a for a in x])),3)
def cosiV(x,y):return round(sum(a*b for a,b in zip(x,y))/(inf+float(rootX2(x)*rootX2(y))),3)

def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def mapFloat(linha): #mapeia para float os valores
    lin2=[]
    for i in range(len(linha)):
        if isFloat(linha[i]):
            lin2 += [float(linha[i])]
        else: lin2 += [linha[i]]
    return lin2
maxVet=0 # max col Vetor
def col(i,dat):return [dat[j][i] for j in range(0,len(dat))]
def med(c): return sum(c)/len(c)
def suml(l): return sum(l[0:maxVet])

# Load a CSV file
def load_csv(filename):
	dataset = []
	with open(filename, 'r') as file:
		linhas = reader(file)  #leitor do pacote CSV
		for row in linhas:
			if not row: continue
			dataset.append(mapFloat(row))
	return dataset

# Load dataset
filename = 'C:/Users/Eloi Favero/Desktop/IA-2019/iris.csv'
dataset = load_csv(filename)
maxVet=len(dataset[1])-1
print('\n'*3)
print('Arquivo   :',filename)
print('carregou  :',len(dataset), 'linhas cada com', len(dataset[0]), 'colunas')
print('cabeçalho :',dataset[0])
print('ex linhas :',dataset[1:5])

random.seed(13)
#print(dataset[:10])
del dataset[0]
random.shuffle(dataset)
dataset=dataset[:100]

percent=0.7
meio=int(percent*len(dataset))
TREINO=dataset[    :meio]
TESTE =dataset[meio:    ]
print('dataset len:', len(dataset))
print('treino  len:', len(TREINO), 'teste len:', len(TESTE))

########KNN###########
def knn(k,j):
    RANGE=range(len(TREINO))
    LIN=[]; teste_j=TESTE[j][:maxVet]
    for i in RANGE:
        LIN.append( (i, euclD(teste_j,TREINO[i][:maxVet]) )) #cosiV(...) ))
    LIN.sort(key=lambda x: x[1])                             #reverse=True)
    idx,_=zip(* LIN[0:k])
    return moda([TREINO[i][-1] for i in idx])

########ACURACIA######
CHUTE=[]; k=1
for i in range(len(TESTE)):CHUTE.append(knn(k,i))
ESPER=col(-1,TESTE)
print(CHUTE[:10])
print(ESPER[:10])
#exit(1)
ESPxCHUT=zip(CHUTE,ESPER)
acertos=[1 for (c,e) in ESPxCHUT if c==e]
print(acertos)
print('sum acertos', sum(acertos))
print('acuracia acertos/total:',sum(acertos)/len(TESTE))

##############

'''
Questões sobre KNN em python em 100 linhas
49. Explique qual é o significado da variavel "percent" e "meio"?
50. Qual são os papeis das listas TREINO e TESTE?
51. o que faz a linha: random.seed(13)?
52. O que faz a linha "del dataset[0]", porque é necessária?
53. O que faz a linha random.shuffle(dataset)?
54. o que faz a linha dataset=dataset[:100]?
53. Como testar o algoritmo KNN apenas com 30 linhas do dataset?
54. Porque o KNN calcula a distancia de uma
linha do TESTE contra todas do TREINO?
55. Para que foi declarada a variável inf=10**-20?
56. Se trocamos euclD por cosiV porque precisa usar sort(key=lambda x: x[1], reverse=True)?
57. O que faz esta linha: idx,_=zip(* LIN[0:k])?
58. Na ultima linha em TREINO[i][-1] o que o (-1) significa?
59. Para seed(13) e dataset[:100] qual a acuracai para manhD()?
60. Para seed(13) e dataset[:100] qual a acuracai para euclD()?
61. Para seed(13) e dataset[:100] qual a acuracai para cosiV()?
62. Para seed(13) e dataset[:100] se colocarmos o comando TREINO,TESTE=TESTE,TREINO o que acontece?
63. Porque a variável se chama CHUTE?
64. Porque o (-1) em ESPER=col(-1,TESTE)?
65. Porque a variável se chama ESPER?
66. Se CHUTE=ESPER qual é a acurácia?
67. O programa esta com k=3, se aumentar para 5 melhora ou piora?
68. O programa esta com k=3, se aumentar para 10 melhora ou piora?
69. Com k=1 melhora ou piora?
70. O k pode ser zero?
71. Qual é o maior valor de k, que faça sentido?
72. O que ocorre se colocamos k com valor máximo?
73. Porque foi defina a var maxVet?
74. No iris.csv temos 4 atributos numericos e um atributo nominal a classe;
totalizando 5 colunas; O que precisa mudar para carregar um arquivo com mais de 5 colunas?
#Entrando no Weka->Explorer->Preprocess->Open File: C:\Program Files\Weka-3-8\data
Trabalhar com arquivos iris.__; credit-g.__; diabetes.__
== Summary ===
Correctly Classified Instances         733               73.3    %
Incorrectly Classified Instances       267               26.7    %
Kappa statistic                          0.3168
Mean absolute error                      0.3191
Root mean squared error                  0.4559
Relative absolute error                 75.9522 %
Root relative squared error             99.4789 %
Total Number of Instances             1000

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0,861    0,567    0,780      0,861    0,819      0,322    0,690     0,797     good
                 0,433    0,139    0,573      0,433    0,493      0,322    0,690     0,465     bad
Weighted Avg.    0,733    0,438    0,718      0,733    0,721      0,322    0,690     0,697

=== Confusion Matrix ===

   a   b   <-- classified as
 603  97 |   a = good
 170 130 |   b = bad
75. Como converter um arquivo .arff para .csv?
76. O que significa "mean absolute error", como é calculado?
77. O que significa "Root mean squared error", como é calculado?
78. o que é "Precision", como é calculado?
79. o que é "Recall", como é calculado?
80. O que é "F-measure", como é calculado?
81. O que é uma matriz de confusão?
82. Em qual aba dos classificadores do Weka esta o IBk?

####TRABALHO EM DUPLA####
0. Mude random.seed(13) para random.seed(NRO-MAT-ALUNO)
   O objetivo é que cada dupla tenha resultado um pouco diferentes
I. Rode o IBk, com k=1 e k=3 para os três arquivos no Weka. Use uma configuração de 66%
para TREINO e 33% para teste. Salve a saida.
Dentro do possivel gere uma saida similar para uma versão do KNN que roda com os três
arquivos: imprimindo as métricas acuracia, nro de acertos e as metricas
citadas nos ex 76 a 80; e a matriz de confusão.

II. Mostre com cada um dos tres arquivos um gráfico,
para decidir qual é o melhor k. Considere a divisão 66/33.

III. Mostre que seu KNN supera o weka em pelo menos um dos arquivos. Como vc pode me convencer
que seu código é mais preciso ou resulta em melhor acuracia? Quais configurações?
'''


