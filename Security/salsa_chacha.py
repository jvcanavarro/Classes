from Crypto.Cipher import Salsa20, ChaCha20
from Crypto.Random import get_random_bytes
import click


def generate_key(salsa):
    return get_random_bytes(256) if salsa else get_random_bytes(32)


def encrypt(key, data, salsa):
    if salsa:
        enc = Salsa20.new(key)
    else:
        enc = ChaCha20.new(key=key)
    return enc.nonce, enc.encrypt(data)


def decrypt(key, data, salsa):
    if salsa:
        dec = Salsa20.new(key)
    else:
        dec = ChaCha20.new(key=key)
    return dec.decrypt(data)


@click.command()
@click.option('-file', type=click.File('r'))
@click.option('-salsa', is_flag=True)
@click.option('-text')
def test_crypto(salsa, text, file):

    if file:
        pass

    text = b'Attack at dawn'

    key = generate_key(salsa)
    print(len(key))
    print(key)

    nonce, enc_text = encrypt(key, text, salsa)
    dec_text = decrypt(key, enc_text, salsa)

    print(enc_text)
    print(dec_text)


if __name__ == '__main__':
    test_crypto()
