import bottle
import hashlib
import os
import time
import secrets

from umboxs import common
from umboxs import package

enable = True

@bottle.get('/api/register/<package_name>')
def register(package_name):
    if not enable:
        return common.api_error(501, "Registrations are disabled, contact the server admin")

    pack = package.Package(package_name)
    if pack.exists():
        return common.api_error(409, "Package already registered")

    token = secrets.token_hex(32)
    secret = hashlib.blake2b(token.encode()).hexdigest()

    pack.secret = secret
    pack.save_db()

    os.mkdir(pack.fpath(""))

    return common.api_ok(token)
