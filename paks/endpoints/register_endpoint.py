import bottle
import hashlib
import os
import time

import db


@bottle.get('/register')
def register():
    return """
        <form action="/register" method="post">
                Module Name: <input name="module_name" type="text" />
                <input value="Register" type="submit" />
        </form>
        """


@bottle.post('/register')
def do_register():
    module_name = bottle.request.forms.get('module_name')

    exists = True
    try:
        db.get_module(module_name)
    except KeyError:
        exists = False

    if exists:
        return bottle.HTTPError(409, "Module already registered")

    token = hashlib.sha1((module_name + str(time.time())).encode()).hexdigest()
    secret = hashlib.blake2b(token.encode()).hexdigest()

    db.set_module(module_name, db.Module(module_name, secret))

    os.mkdir(f"modules/{module_name}")

    return token
