
import db


def search(query: str) -> list:
    packs = db.load_packages().keys()

    return [(pack, db.get_meta(pack)) for pack in packs if query in pack]
