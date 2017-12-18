import click

import commands


@click.group()
def cli():
    pass


@click.command(help="clones a repository")
@click.argument('name')
def clone(name):
    commands.clone(name)


@click.command(help="releases a component")
@click.argument('name')
def release(name):
    commands.release(name)


@click.command(help="hides/unhides a component from gradle")
@click.argument('name')
def toggle(name):
    commands.toggle(name)


cli.add_command(clone)
cli.add_command(release)
cli.add_command(toggle)
