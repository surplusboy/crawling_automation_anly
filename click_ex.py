import click

@click.command()
@click.option('--count', default=1, help='반복 횟수')
@click.option('--name', prompt='Your name',
              help='이름 지정')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        # click.echo('Hello %s!' % name)
        click.echo('Hello {} !'.format(name))

if __name__ == '__main__':
    hello()