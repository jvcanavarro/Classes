from os import urandom
import click
'''
Return a string of n random bytes suitable for cryptographic use.

This function returns random bytes from an OS-specific randomness
source. The returned data should be unpredictable enough for
cryptographic applications, though its exact quality depends on
the OS implementation. On a UNIX-like system this will query
/dev/urandom, and on Windows it will use CryptGenRandom(). If a
randomness source is not found, NotImplementedError will be raised.

Python 2:
https://docs.python.org/2/library/os.html#os.urandom
Python 3:
https://docs.python.org/3/library/os.html#os.urandom
'''
@click.command()
@click.option('-size', type=int)
def safe_num_generator(size):
    key = urandom(size)
    print('Generated Key:', key)


if __name__ == '__main__':
    safe_num_generator()
