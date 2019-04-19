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


def hdb3(signal):
	hdb3 = []
	acc = 0
	anterior = 0
	zeros = 0
	pulso = 0
	for bit in signal:
		if bit == 1:
			if anterior == 1:
				hdb3.append(-1)
				anterior = -1
				pulso = -1
				zeros = zeros + 1
			elif anterior == -1:
				hdb3.append(1)
				anterior = 1
			elif anterior == 0:
				hdb3.append(bit)
				anterior = int(bit)
		elif bit == 0:
			acc = acc + 1
			if acc == 4:
				hdb3.pop()
				hdb3.pop()
				hdb3.pop()
				if zeros % 2 == 0:
					#B00V
					pulso = anterior * -1
					hdb3.extend([pulso,0,0,pulso])
					zeros +=  1
					anterior = pulso
				else:
					#000V
					hdb3.extend([0,0,0,pulso])
					zeros += 1
				acc = 0
			else :
				hdb3.append(bit)
		
	return hdb3

signal_length = int(input('Enter Signal Length: '))
bit_signal = create_random_bit_signal(signal_length)
# print('Signal: ', bit_signal)


bits = '01001100011'
# bits = '00000000011001100001'
# bits = ''

bit_signal = [int(bit) for bit in str(bits)]
bit_signal.append(bit_signal[-1])

data = np.repeat(bit_signal, 2)
clock = 1 - np.arange(len(data)) % 2

manchester = 1 - np.logical_xor(clock, data)
dif_manchester = np.asarray(dif_man(bit_signal[:-1]))
hdb3 = np.asarray(hdb3(bit_signal))
b8zs = 0


create_axis('x', range(len(bit_signal)), color='.5', linewidth=0.5, linestyle = ":")
create_axis('y', [0, 2, 5, 7, 9], color='.5', linewidth=0.5, linestyle = ":")

t = 0.5 * np.arange(len(data) - 1)
t2 = np.arange(len(hdb3))

plt.step(t, data[:-1] + 9, 'r', linewidth = 1.5, where='pre', label='data')
plt.step(t, clock[:-1] + 7, 'blue', linewidth = 1.5, where='pre', label='clock')
plt.step(t2, hdb3 + 5, 'orange', linewidth = 1.5, where='mid', label='hdb3')
plt.step(t, dif_manchester[:len(t)] + 2, 'green', linewidth = 1.5, where='pre', label='differential')
plt.step(t, manchester[:-1], 'black', linewidth = 1.5, where='pre', label='manchester')

plt.ylim([-1,11])


for index, value in enumerate(bit_signal[:-1]):
	plt.text(index + 0.5, -1, value)

plt.title('Codification')
plt.legend()
plt.gca().axis('off') # Remove Axis
plt.show()