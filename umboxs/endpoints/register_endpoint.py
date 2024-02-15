import bottle
import hashlib
import os
import time
import secrets

from umboxs import db

enable = True

@bottle.get('/api/register/<package_name>')
def register(package_name):
    if not enable:
        return bottle.HTTPError(501, "Registrations are disable, contact the server admin")

    exists = True
    try:
        db.get_package(package_name)
    except KeyError:
        exists = False

    if exists:
        return bottle.HTTPError(409, "Packages already registered")

    token = secrets.token_hex(32)
    secret = hashlib.blake2b(token.encode()).hexdigest()

    db.set_package(db.Package(package_name, secret))

    os.mkdir(f"packages/{package_name}")

    return token
