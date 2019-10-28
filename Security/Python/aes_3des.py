from Crypto.Cipher import AES, DES3
from Crypto.Protocol import KDF
from Crypto import Random
import click


def pad_data(data):
    if len(data) % 16 == 0:
        return data
    databytes = bytearray(data)
    padding_required = 15 - (len(databytes) % 16)
    databytes.extend(b'\x80')
    databytes.extend(b'\x00' * padding_required)
    return bytes(databytes)


def unpad_data(data):
    if not data:
        return data

    data = data.rstrip(b'\x00')
    if data[-1] == 128:
        return data[:-1]
    else:
        return data


def generate_key(des3, password, salt=b'madhubal'):
    key = KDF.PBKDF2(password, salt, 16)
    return key


def encrypt(key, iv, data, des3):
    if des3:
        enc = DES3.new(key, DES3.MODE_ECB, iv)
    else:
        enc = AES.new(key, AES.MODE_ECB, iv)
    data = pad_data(data)
    return enc.encrypt(data)


def decrypt(key, iv, data, des3):
    if des3:
        dec = DES3.new(key, DES3.MODE_ECB, iv)
    else:
        dec = AES.new(key, AES.MODE_ECB, iv)
    data = dec.decrypt(data)
    return unpad_data(data)


@click.command()
@click.option('--des3', is_flag=True)
@click.option('-password')
def test_crypto(des3, password):
    msg = b"This is some super secret message.  Please don't tell anyone about it or I'll have to shoot you."
    key = generate_key(des3, password)

    iv = b"12345678"

    enc_text = encrypt(key, iv, msg, des3)

    dec_text = decrypt(key, iv, code)


if __name__ == '__main__':
    test_crypto()
