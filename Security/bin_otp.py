import numpy as np
import click


def generate_key(length):
    return np.random.randint(2, size=length)


def encrypt_message(message, key):
    return [int(m_bit) ^ k_bit for m_bit, k_bit in zip(message, key)]


def binarize_sentence(sentence):
    sentence = map(bin, bytearray(sentence, 'utf8'))
    return ''.join(bit[2:] for bit in sentence)


def string_sentence(sentence):
    sentence = [str(bit) for bit in sentence]
    sentence = [''.join(sentence[i:i + 8]) for i in range(0, len(sentence), 7)]
    print(sentence)
    print(int(sentence[0], 2))
    return ''.join(map(lambda bit: int(bit, 2), sentence))



@click.command()
@click.option('-m', 'message')
@click.option('-s', 'sentence', is_flag=True)
def onetime_pad(message, sentence):
    if sentence:
        message = binarize_sentence(message)

    key = generate_key(len(message))
    print(list(key), '| Key')

    enc_message = encrypt_message(message, key)
    print(enc_message, '| Encrypted Message')

    dec_message = encrypt_message(enc_message, key)
    print(dec_message, '| Decrypted Message')

    if sentence:
        print(string_sentence(dec_message))

if __name__ == '__main__':
    onetime_pad()
