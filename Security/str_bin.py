message = 'ana luiza'

bin_message = ' '.join(map(bin,bytearray(message, 'utf8')))

for bit in bin_message.split():
    print(int(bit, 2))
