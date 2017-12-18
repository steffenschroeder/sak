import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def clone(name):
    click.echo('cloning ' + name)

@click.command()
@click.argument('name')
def release(name):
    click.echo('releasing ' + name)

@click.command()
@click.argument('name')
def toggle(name):
    click.echo('toggling' + name) 

cli.add_command(clone)
cli.add_command(release)
cli.add_command(toggle)
