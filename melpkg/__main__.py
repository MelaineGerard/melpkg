import sys
import click


@click.group()
@click.version_option("1.0.0")
def main():
    """A package manager for linux packages"""
    print("Hey")
    pass


@main.command()
def update(**kwargs):
    """Update repository list"""
    click.echo(kwargs)
    pass


@main.command()
@click.argument('name', required=False)
def install(**kwargs):
    """Install a package"""
    click.echo(kwargs)
    pass


@main.command()
@click.argument('name', required=False)
def remove(**kwargs):
    """Remove a package"""
    click.echo(kwargs)
    pass


@main.command()
@click.argument('name', required=False)
def search(**kwargs):
    """Search a package"""
    click.echo(kwargs)
    pass


@main.command()
def upgrade(**kwargs):
    """Upgrade all the packages"""
    click.echo(kwargs)
    pass


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("MelPKG")
    main()
