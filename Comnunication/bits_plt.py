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
data = np.repeat(bit_signal, 2)
clock = 1 - np.arange(len(data)) % 2
manchester = 1 - np.logical_xor(clock, data)
dif_manchester = 0
b8zs = 0
hdb3 = 0

print(data)
print(clock)
print(manchester)

t = 0.5 * np.arange(len(data))

print(t)

create_axis('x', range(len(bit_signal)), color='.5', linewidth=0.5, linestyle = ":")
create_axis('y', [2, 4, 6], color='.5', linewidth=0.5, linestyle = ":")

plt.step(t, data + 6, 'r', linewidth = 1.5, where='post', label='data')
plt.step(t, clock + 4, 'blue', linewidth = 1.5, where='post', label='clock')
plt.step(t, manchester + 2, 'black', linewidth = 1.5, where='post', label='manchester')

plt.ylim([1,8])


for index, value in enumerate(bit_signal):
	plt.text(index + 0.5, 0.5, value)

plt.title('Codification')
plt.legend()
plt.gca().axis('off') # Remove Axis
plt.show()
