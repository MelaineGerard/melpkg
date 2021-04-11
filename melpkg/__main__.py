import sys
import click
import melpkg as mp


@click.group()
@click.version_option("0.0.1")
def main():
    """A package manager for linux packages"""
    print("Starting to work on your demand...")
    pass


@main.command()
@click.argument('name', required=True)
def install(**kwargs):
    """Install a package"""
    mp.install_package(kwargs['name'])
    pass


@main.command()
@click.argument('name', required=True)
def remove(**kwargs):
    """Remove a package"""
    mp.remove_package(kwargs['name'])
    pass


@main.command()
@click.argument('name', required=True)
def search(**kwargs):
    """Search a package"""
    mp.search_package(kwargs['name'])
    pass


@main.command()
def update(**kwargs):
    """Update repository list"""
    mp.update_list()
    pass


@main.command()
def upgrade(**kwargs):
    """Upgrade all the packages"""
    mp.upgrade_packages()
    pass


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("MelPKG")
    main()
