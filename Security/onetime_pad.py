import numpy as np
import click


def generate_key(length):
    return np.random.randint(2, size=length)


def encrypt_message(message, key):
    return [int(m_bit) ^ k_bit for m_bit, k_bit in zip(message, key)]


@click.command()
@click.option('-m', 'message')
@click.option('-s', 'sentence', is_flag=True)
def onetime_pad(message, sentence):
    key = generate_key(len(message))
    print(list(key), '| Key')

    enc_message = encrypt_message(message, key)
    print(enc_message, '| Encrypted Message')

    dec_message = encrypt_message(enc_message, key)
    print(dec_message, '| Decrypted Message')


if __name__ == '__main__':
    onetime_pad()
