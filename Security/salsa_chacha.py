from Crypto.Cipher import Salsa20, ChaCha20
from Crypto.Random import get_random_bytes
import click


def generate_key():
    return get_random_bytes()


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
@click.option('-salsa', is_flag=True)
@click.option('-cha', is_flag=True)
def test_crypto(salsa, cha):
    msg = b"This is some super secret message.  Please don't tell anyone about it or I'll have to shoot you."
    key = generate_key()

    enc_text = encrypt(key, msg, salsa)

    dec_text = decrypt(key, enc_text)


if __name__ == '__main__':
    test_crypto()
