import collections
import json

# This is very TODO. I should probably use a real database.

Module = collections.namedtuple('Module', ['name', 'secret'])


def __load_modules() -> list[Module]:
    with open('modules.json', 'r') as f:
        return json.loads(f.read())


def __save_modules(modules: list[Module]):
    with open('modules.json', 'w') as f:
        f.write(json.dumps(modules))


def get_module(name: str) -> Module:
    mod = __load_modules()[name]
    return Module(*mod)


def set_module(name: str, value: Module):
    mods = __load_modules()
    mods[name] = value
    __save_modules(mods)
