import Crypto.Random
import numpy as np
import click


def generate_key(length):
    a = Crypto.Random.get_random_bytes(length)
    print(a)
    return Crypto.Random.get_random_bytes(length)
    # return np.random.randint(2, size=length)


def encrypt_message(message, key):
    return [int(m_bit) ^ k_bit for m_bit, k_bit in zip(message, key)]


def text_to_bits(text, encoding='utf-8'):
    bits = bin(int.from_bytes(text.encode(encoding), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8'):
    n = int(''.join(map(str, bits)), 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding)


@click.command()
@click.option('--file', type=click.File('r'))
@click.option('--text')
def onetime_pad(file, text):

    if file:
        text = file.read()
        print(text.split())

    enc_message = []
    dec_message = []


    for word in text.split():
        word = text_to_bits(word)
        key = generate_key(len(word))

        enc_message.append(encrypt_message(word, key))
        dec_message.append(encrypt_message(enc_message[-1], key))

        dec_message[-1] = text_from_bits(dec_message[-1])

        # print(enc_message)
        # print(dec_message[-1], '\n')

    print("Encrypted Message: ", enc_message)
    print("Decrypted Message: ",  ' '.join(dec_message))


if __name__ == '__main__':
    onetime_pad()
