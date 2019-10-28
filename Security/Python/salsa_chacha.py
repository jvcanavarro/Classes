from Crypto.Cipher import Salsa20, ChaCha20
from Crypto.Random import get_random_bytes
import click


def generate_key():
    return get_random_bytes(32)


def encrypt(key, data, salsa):
    if salsa:
        enc = Salsa20.new(key=key)
    else:
        enc = ChaCha20.new(key=key)

    return enc.nonce + enc.encrypt(data)


def decrypt(key, data, salsa):
    if salsa:
        dec = Salsa20.new(key=key, nonce=data[:8])
    else:
        dec = ChaCha20.new(key=key, nonce=data[:8])

    return dec.decrypt(data[8:])


@click.command()
@click.option('-file', type=click.File('r'))
@click.option('-salsa', is_flag=True)
@click.option('-text')
def test_crypto(salsa, text, file):

    if file:
        text = file.read()

    text = str.encode(text)
    key = generate_key()

    enc_text = encrypt(key, text, salsa)
    dec_text = decrypt(key, enc_text, salsa)

    print('Encrypted Text:\n', enc_text)
    print()
    print('Decrypted Text:\n', dec_text)


if __name__ == '__main__':
    test_crypto()
