
import numpy as np
import matplotlib.pyplot as plt


string ='00000000011001100001'
string = '1100001000000000'
string = '100110001000000111'
strOutput = []
strOutputLabel = []
def output():
    contador = 0
    pulsoAnterior = 0
    Violaciones = 0
    pulsoViolacion = 0

    for bit in string:
        # print(bit)
        if int(bit) == 1:
            # print('ok')
            if pulsoAnterior == 1:
                strOutput.append(-1)
                strOutputLabel.append(-1)
                pulsoAnterior = -1
                pulsoViolacion = -1
                Violaciones = Violaciones + 1
            elif pulsoAnterior == -1:
                strOutput.append(1)
                strOutputLabel.append(1)
                pulsoAnterior = 1
            elif pulsoAnterior == 0:
                strOutput.append(bit)
                strOutputLabel.append(bit)
                pulsoAnterior = int(bit)
        elif int(bit) == 0:
            # print('0')
            contador = contador + 1
            if contador == 4:
                strOutput.pop()
                strOutput.pop()
                strOutput.pop()
                strOutputLabel.pop()
                strOutputLabel.pop()
                strOutputLabel.pop()
                if Violaciones % 2 == 0:
                    #B00V
                    pulsoViolacion = pulsoAnterior * -1
                    strOutput.extend([pulsoViolacion,0,0,pulsoViolacion])
                    strOutputLabel.extend(["B",0,0,"V"])
                    Violaciones = Violaciones + 1
                    pulsoAnterior = pulsoViolacion

                else:
                    #000V
                    strOutputLabel.extend([0,0,0,"V"])
                    strOutput.extend([0,0,0,pulsoViolacion])
                    Violaciones = Violaciones + 1
                contador = 0
            else :
                strOutput.append(bit)
                strOutputLabel.append(bit)


output()

#Graph
x = np.arange(len(strOutput))
print(strOutput)
test = []
for bit in strOutput:
    test.append(int(bit))

# strOutput = [int(bit) for bit in str(strOutput)]
print(test)
plt.step(x, test)
plt.xlabel(strOutputLabel)
plt.xlim(-1, len(strOutput) + 1)
plt.ylim(-3, 3)
plt.title('HDB3 Encoding')
plt.show()