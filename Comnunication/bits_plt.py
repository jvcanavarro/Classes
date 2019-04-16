import matplotlib.pyplot as plt
import numpy as np

def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

bits = [1,0] * 5
data = np.repeat(bits, 2)
clock = 1 - np.arange(len(data)) % 2
manchester = 1 - np.logical_xor(clock, data)

t = 0.5 * np.arange(len(data))

my_lines('x', range(len(bits)), color='.5', linewidth=0.5, linestyle = ":")
my_lines('y', [2, 4, 6], color='.5', linewidth=0.5, linestyle = ":")
plt.step(t, clock + 4, 'blue', linewidth = 1.5, where='post', label='clock')
plt.step(t, data + 2, 'r', linewidth = 1.5, where='post', label='data')
plt.step(t, manchester + 6, 'black', linewidth = 1.5, where='post', label='manchester')
plt.ylim([1,8])

for tbit, bit in enumerate(bits):
    plt.text(tbit + 0.5, 1.5, str(bit))

plt.title('Codification')
plt.legend()
plt.gca().axis('off') # Remove retas de coordenadas
plt.show()