import bottle
import hashlib
import os
import time
import secrets

from umboxs import db
from umboxs import common

enable = True

@bottle.get('/api/register/<package_name>')
def register(package_name):
    if not enable:
        return common.api_error(501, "Registrations are disabled, contact the server admin")

    exists = True
    try:
        db.get_package(package_name)
    except KeyError:
        exists = False

    if exists:
        return common.api_error(409, "Package already registered")

    token = secrets.token_hex(32)
    secret = hashlib.blake2b(token.encode()).hexdigest()

    db.set_package(db.Package(package_name, secret))

    os.mkdir(f"packages/{package_name}")

    return common.api_ok(token)
