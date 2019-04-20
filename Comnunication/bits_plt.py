import matplotlib.pyplot as plt
import numpy as np

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
			dif_man.extend([0,0,1])
			start = False
			pre = 'one'
		elif signal[i]==1 and start :
			dif_man.extend([1,1,0])
			start = False
			pre = 'zero'
		else:
			if signal[i]==0:
				if pre == 'one':
					dif_man.extend([0,1])
				else:
					dif_man.extend([1,0])
			else:
				if pre == 'zero':
					pre = 'one'
					dif_man.extend([0,1])
				else:
					pre = 'zero'
					dif_man.extend([1,0])

	return dif_man


def hdb3(signal): #consecutive four zeros
	hdb3 = []
	num_zeros = 0
	num_ones = 0
	last_pulse = -1

	for bit in signal:
		if bit == 1:
			if last_pulse == 0 or last_pulse == -1:
				hdb3.append(1)
				last_pulse = 1
				num_ones += 1
			else:
				hdb3.append(-1)
				last_pulse = -1
				num_ones += 1
			num_zeros = 0
		else:
			hdb3.append(0)
			num_zeros += 1
			if num_zeros == 4:
				hdb3 = hdb3[:-4]
				if num_ones % 2 == 0: # even
					hdb3.extend([last_pulse*-1, 0, 0, last_pulse*-1])
				else: # odd
					hdb3.extend([0, 0, 0, last_pulse])
				num_zeros = 0
				num_ones = 0
				last_pulse = hdb3[-1]

	return hdb3


def b8zs(signal): #consecutive eight zeros
    b8zs = []
    num_zeros = 0
    last_pulse = -1

    for bit in signal:
        if bit == 1:
            if last_pulse == 0 or last_pulse == -1:
                b8zs.append(1)
                last_pulse = 1
            else:
                b8zs.append(-1)
                last_pulse = -1
            num_zeros = 0
        else:
            b8zs.append(0)
            num_zeros += 1
            if num_zeros == 8:
                b8zs = b8zs[:-8]
                if last_pulse >= 0:
                    b8zs.extend([ 0, 0, 0, 1, -1, 0, -1, 1])
                else:
                    b8zs.extend([ 0, 0, 0, -1, 1, 0, 1, -1])
                num_zeros = 0
                last_pulse = b8zs[-1]

    return b8zs


# bits = ''
# bits = '01001100011'
# bits = '10100111001'
# bits = '1100001000000000'
bits = '0000000001100110000'

bit_signal = [int(bit) for bit in str(bits)]


data = np.repeat(bit_signal, 2)
clock = 1 - np.arange(len(data)) % 2
manchester = np.logical_xor(clock, data)
dif_manchester = np.asarray(dif_man(bit_signal))
hdb3 = np.asarray(hdb3(bit_signal))
b8zs = np.asarray(b8zs(bit_signal))


print('hdb3: ', hdb3)
print('b8zs: ', b8zs)
create_axis('x', range(len(bit_signal)), color='.5', linewidth=0.5, linestyle = ":")
create_axis('y', [0, 2, 5, 8, 10, 12], color='.5', linewidth=0.5, linestyle = ":")

t = 0.5 * np.arange(len(data))

plt.step(t, data + 12, 'r', linewidth = 1.5, where='post', label='data')
plt.step(t, clock + 10, 'blue', linewidth = 1.5, where='post', label='clock')
plt.step(np.arange(len(b8zs)), b8zs + 8, 'purple', linewidth = 1.5, where='post', label='b8zs')
plt.step(np.arange(len(hdb3)), hdb3 + 5, 'orange', linewidth = 1.5, where='post', label='hdb3')
plt.step(t, dif_manchester[:-1] + 2, 'green', linewidth = 1.5, where='pre', label='differential')
plt.step(t, manchester, 'black', linewidth = 1.5, where='post', label='manchester')

plt.ylim([-1,14])


for index, value in enumerate(bit_signal):
	plt.text(index + 0.5, -1, value)

plt.title('Codification')
plt.legend()
plt.gca().axis('off') # Remove Axis
plt.show()