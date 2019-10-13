from operator import sub, add
import string
import random
import click


def get_index_of_char(letter):
    return string.ascii_lowercase.index(letter)


def generate_key(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def get_char_by_index(index):
    return string.ascii_lowercase[index]


def encrypt_message(message, key, func, decrypt=False):
    index_message = map(get_index_of_char, message)
    index_key = map(get_index_of_char, key)

    enc_message = map(func, index_message, index_key)
    enc_message = map(lambda x: x % 26, enc_message)

    return ''.join(map(get_char_by_index, enc_message))


@click.command()
@click.option('-m', 'message', help='Message', required=True)
@click.option('-k', 'key', help='Key',  default='')
def onetime_pad(message, key):
    if len(key) != len(message):
        print('Missing Key or Text/Key size is different.')
        print('Generating a Random Key.\n')
        key = generate_key(len(message))

    enc_message = encrypt_message(message, key, add)
    dec_message = encrypt_message(enc_message, key, sub, True)

    print('Original Message:  ', message)
    print('Encrypted Message: ', enc_message)
    print('Decrypted Message: ', dec_message)


if __name__ == '__main__':
    onetime_pad()
