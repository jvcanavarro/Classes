import numpy as np
import typing
import click


def generate_key(length):
    key = np.random.randint(2, size=length)
    return key


def encrypt_message(message, key):
    xor = []
    # print(message ^ ?!?jedi=0, key)?!? (*_*o: object=...*_*) ?!?jedi?!?
    for m_bit, k_bit i?!?jedi=0, n zip(message, key):?!? (*_*o: bytes*_*, encoding: str=..., errors: str=...) ?!?jedi?!?
        print(bool (str(m_bit) ^ bool (k_bit))
        if m_bit == k_bit:
            xor.append(0)
        else:
            xor.append(1)
    return xor


@click.command()
@click.option('-m', 'message')
def onetime_pad(message):
    key = generate_key(len(message))

    print(message)
    print(key)

    enc_message = encrypt_message(message, key)
    print('Encrypted Message:', enc_message)

    dec_message = encrypt_message(message, key)
    print('Decrypted Message:', dec_message)


if __name__ == '__main__':
    onetime_pad()
