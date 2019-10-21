from Crypto import Random
import click


def generate_key(length):
    return Random.get_random_bytes(length)


def encrypt_message(message, key):
    return [int(m_bit) ^ k_bit for m_bit, k_bit in zip(message, key)]


def text_to_bits(text, encoding='utf-8'):
    bits = bin(int.from_bytes(text.encode(encoding), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8'):
    n = int(''.join(map(str, bits)), 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding)


@click.command()
@click.option('-file', type=click.File('r'))
@click.option('-text')
def onetime_pad(file, text):

    if file:
        text = file.read()

    message = text_to_bits(text)
    key = generate_key(len(message))

    enc_msg = encrypt_message(message, key)
    print('Encrypted Message:', enc_msg)

    dec_msg = encrypt_message(enc_msg, key)
    dec_msg = text_from_bits(dec_msg)

    print('Decrypted Message:', dec_msg)


if __name__ == '__main__':
    onetime_pad()
