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

def plot_bits_stepmode():
	pass

def create_random_bit_signal(signal_length=7):
	return [np.random.randint(2) for bit in range(signal_length)]


signal_length = int(input('Enter Signal Length: '))
bit_signal = create_random_bit_signal(signal_length)

print('Signal: ', bit_signal)

bit_signal.append(bit_signal[-1])
data = np.repeat(bit_signal, 2)
clock = 1 - np.arange(len(data)) % 2
manchester = 1 - np.logical_xor(clock, data)
dif_manchester = 0
b8zs = 0
hdb3 = 0

t = 0.5 * np.arange(len(data) - 1)


create_axis('x', range(len(bit_signal)), color='.5', linewidth=0.5, linestyle = ":")
create_axis('y', [2, 4, 6], color='.5', linewidth=0.5, linestyle = ":")

plt.step(t, data[:-1] + 6, 'r', linewidth = 1.5, where='pre', label='data')
plt.step(t, clock[:-1] + 4, 'blue', linewidth = 1.5, where='pre', label='clock')
plt.step(t, manchester[:-1] + 2, 'black', linewidth = 1.5, where='pre', label='manchester')

plt.ylim([1,8])


for index, value in enumerate(bit_signal[:-1]):
	plt.text(index + 0.5, 0.5, value)

plt.title('Codification')
plt.legend()
plt.gca().axis('off') # Remove Axis
plt.show()
