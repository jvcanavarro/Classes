import matplotlib.pyplot as plt
import numpy as np
import random
def create_axis(ax, coordenates, *args, **kwargs):
    if ax == 'x':
        for coordenate in coordenates:
            plt.axvline(coordenate, *args, **kwargs) # vertical line
    elif ax == 'y':
        for coordenate in coordenates:
            plt.axhline(coordenate, *args, **kwargs) # horizontal line

def create_random_bit_signal(signal_length=7):
	return [np.random.randint(2) for bit in range(signal_length)]

def dif_man(signal):
    dif_man = []
    start = True
    pre = ''
    for i in range(len(signal)):
        if signal[i]==0 and start:
            dif_man.append(0)
            dif_man.append(0)
            dif_man.append(1)
            start = True
            pre = 'one'
        elif signal[i]==1 and start :
            dif_man.append(1)
            dif_man.append(1)
            dif_man.append(0)
            start = False
            pre = 'zero'
        else:
            if signal[i]==0:
                if pre == 'zero':
                    dif_man.append(0);dif_man.append(1)
                else:
                    dif_man.append(1);dif_man.append(0)
            else:
                if pre == 'zero':
                    pre = 'one'
                    dif_man.append(0);dif_man.append(1)
                else:
                    pre = 'zero'
                    dif_man.append(1);dif_man.append(0)

    return dif_man   


def output():
    contador = 0
    pulsoAnterior = 0
    Violaciones = 0
    pulsoViolacion = 0

    for bit in string:
        if bit == str(1):
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
        elif bit == str(0):
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


signal_length = int(input('Enter Signal Length: '))
bit_signal = create_random_bit_signal(signal_length)

print('Signal: ', bit_signal)
bit_signal = [0,1,0,0,1,1,0,0,0,1,1]

bit_signal.append(bit_signal[-1])
data = np.repeat(bit_signal, 2)
clock = 1 - np.arange(len(data)) % 2
manchester = 1 - np.logical_xor(clock, data)
dif_manchester = dif_man(bit_signal[:-1])
b8zs = 0
hdb3 = 0

t = 0.5 * np.arange(len(data) - 1)

create_axis('x', range(len(bit_signal)), color='.5', linewidth=0.5, linestyle = ":")
create_axis('y', [0, 2, 4, 6], color='.5', linewidth=0.5, linestyle = ":")

plt.step(t, data[:-1] + 6, 'r', linewidth = 1.5, where='pre', label='data')
plt.step(t, clock[:-1] + 4, 'blue', linewidth = 1.5, where='pre', label='clock')
plt.step(t, manchester[:-1] + 2, 'black', linewidth = 1.5, where='pre', label='manchester')
plt.step(t, dif_manchester[:len(t)], 'green', linewidth = 1.5, where='pre', label='differential')

plt.ylim([-1,10])


for index, value in enumerate(bit_signal[:-1]):
	plt.text(index + 0.5, -1, value)

plt.title('Codification')
plt.legend()
plt.gca().axis('off') # Remove Axis
plt.show()
