import collections
import json

# This is very TODO. I should probably use a real database.

Package = collections.namedtuple('Package', ['name', 'secret'])


def load_packages() -> dict[str, list]:
    with open('packages.json', 'r') as f:
        return json.loads(f.read())


def save_packages(modules: dict[str, Package]):
    with open('packages.json', 'w') as f:
        f.write(json.dumps(modules))


def get_package(name: str) -> Package:
    mod = load_packages()[name]
    return Package(*mod)


def set_package(name: str, value: Package):
    mods = load_packages()
    mods[name] = value
    save_packages(mods)


def get_meta(name: str) -> dict:
    try:
        with open(f"packages/{name}/pak.json", "r") as f:
            return json.loads(f.read())
    except:
        return {
            "name": name,
            "description": "No description",
            "version": "0.0.0",
            "author": "Unknown",
            "license": "Unknown",
            "dependencies": []
        }
