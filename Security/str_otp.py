import click

@click.command()
@click.option('-t', 'text', required=True)
@click.option('-k', 'key')
def onetime_pad(text, key):
    if not key:
        key = generate_key()

if __name__ == '__main__':
    onetime_pad()
