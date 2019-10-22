from Crypto.Cipher import Salsa20, ChaCha20
from Crypto.Random import get_random_bytes
import click


def generate_key(salsa):
    return get_random_bytes(256) if salsa else get_random_bytes(8)


def encrypt(key, data, salsa):
    if salsa:
        enc = .new(key, .MODE_ECB)
    else:
        enc = .new(key, .MODE_ECB)
    return enc.encrypt(data)


def decrypt(key, data):
    if salsa:
        dec = .new(key, .MODE_ECB)
    else:
        dec = .new(key, .MODE_ECB)
    data = dec.decrypt(data)
    return data


@click.command()
@click.option('-file', type=click.File('r'))
@click.option('-salsa', is_flag=True)
@click.option('-text')
def test_crypto(salsa, text, file):

    if file:
        pass

    key = generate_key(salsa)

    enc_text = encrypt(key, msg, salsa)

    dec_text = decrypt(key, enc_text, salsa)


if __name__ == '__main__':
    test_crypto()
