import bottle
import json

from . import package


def search(query: str) -> list:
    packs = package.load_all()

    return [(pack, package.Package(pack).get_meta()) for pack in packs if query in pack]

def api_ok(data: object) -> bottle.HTTPResponse:
    return bottle.HTTPResponse(json.dumps({
        "ok": True,
        "data": data
    }), status = 200, headers={ "Content-Type": "application/json" })
    
def api_error(code: int, message: str) -> bottle.HTTPResponse:
    return bottle.HTTPResponse(json.dumps({
        "ok": False,
        "msg": message
    }), status = code, headers={ "Content-Type": "application/json" })
