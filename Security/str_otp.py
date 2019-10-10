import operator
import string
import random
import click


def get_index_of_char(letter):
    return string.ascii_lowercase.index(letter)


def generate_key(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def get_char_by_index(index):
    return string.ascii_lowercase[index]


def encrypt_message(message, key):
    index_message = map(get_index_of_char, message)
    index_key = map(get_index_of_char, key)

    enc_message = map(sum, zip(index_message, index_key))
    return map(lambda x: x % 26, enc_message)

def decrypt_message(message, key):
    index_key = map(get_index_of_char, key)

    dec_message = map(operator.sub, message, index_key)
    dec_message = map(lambda x: x % 26, dec_message)

    return ''.join(map(get_char_by_index, dec_message))


@click.command()
@click.option('-m', 'message', required=True)
@click.option('-k', 'key', default='')
def onetime_pad(message, key):
    if len(key) != len(message):
        print('Missing Key or Text/Key size is different.')
        print('Generating a Random Key.\n')
        key = generate_key(len(message))

    enc_message = encrypt_message(message, key)
    dec_message = decrypt_message(enc_message, key)
    print(enc_message)
    print(dec_message)

if __name__ == '__main__':
    onetime_pad()
