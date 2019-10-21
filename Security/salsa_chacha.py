from Crypto.Cipher import Salsa20, ChaCha20
from Crypto.Random import get_random_bytes
import click


def generate_key(salsa):
    if salsa:
        return get_random_bytes(256)
    return get_random_bytes(8)


def encrypt(key, data):
    if des3:
        enc = DES3.new(key, DES3.MODE_ECB, iv)
    else:
        enc = AES.new(key, AES.MODE_ECB, iv)
    return enc.encrypt(data)


def decrypt(key, data):
    if des3:
        dec = DES3.new(key, DES3.MODE_ECB, iv)
    else:
        dec = AES.new(key, AES.MODE_ECB, iv)
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

    dec_text = decrypt(key, enc_text)


if __name__ == '__main__':
    test_crypto()
