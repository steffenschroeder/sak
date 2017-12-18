import click

@click.group()
def cli():
    pass

@click.command(help="clones a repository")
@click.argument('name')
def clone(name):
    click.echo('cloning ' + name)

@click.command(help="releases a component")
@click.argument('name')
def release(name):
    click.echo('releasing ' + name)

@click.command(help="hides/unhides a component from gradle")
@click.argument('name')
def toggle(name):
    click.echo('toggling' + name) 

cli.add_command(clone)
cli.add_command(release)
cli.add_command(toggle)
