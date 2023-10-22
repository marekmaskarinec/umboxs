import collections
import json

# This is very TODO. I should probably use a real database.

Package = collections.namedtuple('Package', ['name', 'secret'])


def __load_modules() -> list[Package]:
    with open('packages.json', 'r') as f:
        return json.loads(f.read())


def __save_modules(modules: list[Package]):
    with open('packages.json', 'w') as f:
        f.write(json.dumps(modules))


def get_module(name: str) -> Package:
    mod = __load_modules()[name]
    return Package(*mod)


def set_module(name: str, value: Package):
    mods = __load_modules()
    mods[name] = value
    __save_modules(mods)
