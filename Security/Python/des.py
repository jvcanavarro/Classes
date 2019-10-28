from collections import Counter
from Crypto.Cipher import DES
from functools import reduce
from Crypto import Random
from operator import add


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


def generate_key():
    rnd = Random.OSRNG.posix.new().read(DES.block_size)
    return rnd


def encrypt(key, iv, data):
    des = DES.new(key, DES.MODE_CBC, iv)
    data = pad_data(data)
    return des.encrypt(data)


def decrypt(key, iv, data):
    des = DES.new(key, DES.MODE_CBC, iv)
    data = des.decrypt(data)
    return unpad_data(data)


def test_crypto():
    msg = b"This is some super secret message.  Please don't tell anyone about it or I'll have to shoot you."
    key = generate_key()

    iv1 = b"12345678"
    iv2 = b"12345679"

    code1 = encrypt(key, iv1, msg)
    code2 = encrypt(key, iv2, msg)

    # decoded1 = decrypt(key, iv1, code1)
    # decoded2 = decrypt(key, iv2, code2)

    occ_bits = map(lambda x: Counter(bin(x)[2:]), code1)
    sum_bits1 = reduce(add, occ_bits)
    print(sum_bits1)

    occ_bits = map(lambda x: Counter(bin(x)[2:]), code2)
    sum_bits2 = reduce(add, occ_bits)
    print(sum_bits2)


if __name__ == '__main__':
    test_crypto()
