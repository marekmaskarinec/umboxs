import bottle
import hashlib
import os
import time

import db


@bottle.get('/api/register/<package_name>')
def register(package_name):
    exists = True
    try:
        db.get_package(package_name)
    except KeyError:
        exists = False

    if exists:
        return bottle.HTTPError(409, "Packages already registered")

    token = hashlib.sha1(
        (package_name + str(time.time())).encode()).hexdigest()
    secret = hashlib.blake2b(token.encode()).hexdigest()

    db.set_package(package_name, db.Package(package_name, secret))

    os.mkdir(f"packages/{package_name}")

    return token
