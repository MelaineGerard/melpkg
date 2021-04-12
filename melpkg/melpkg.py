import urllib.request as ur


def install_package(name: str):
    print(f"Installing package {name}...")
    print(f"Package {name} installed!")


def remove_package(name: str):
    print(f"Removing package {name}...")
    print(f"Package {name} removed!")


def search_package(name: str):
    print(f"Searching package {name}...")
    print(f"Package {name} founded!")


def update_list():
    print("Updating the list of package...")
    with open("/etc/melpkg/sources.list") as sources:
        for repo in sources:
            repo_url = repo.replace('\n', '')
            data = ur.urlopen(f"{repo_url}/Packages")
            data = data.split("\n")
            for line in data:
                print(line.decode('utf-8'))
    print("List of package updated!")


def upgrade_packages():
    print("Upgrading packages...")
    print("Packages upgraded!")
