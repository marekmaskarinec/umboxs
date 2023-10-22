import bottle
import hashlib
import os
import time

import db


@bottle.get('/register')
def register():
    return """
        <form action="/register" method="post">
                Package Name: <input name="package_name" type="text" />
                <input value="Register" type="submit" />
        </form>
        """


@bottle.post('/register')
def do_register():
    package_name = bottle.request.forms.get('package_name')

    exists = True
    try:
        db.get_module(package_name)
    except KeyError:
        exists = False

    if exists:
        return bottle.HTTPError(409, "Packages already registered")

    token = hashlib.sha1(
        (package_name + str(time.time())).encode()).hexdigest()
    secret = hashlib.blake2b(token.encode()).hexdigest()

    db.set_module(package_name, db.Module(package_name, secret))

    os.mkdir(f"packages/{package_name}")

    return token
