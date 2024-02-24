
import bottle
import os

from umboxs import package
from umboxs import db
from umboxs import common

valid_filenames = [
    "box.tar",
    "init.tar"
]

@bottle.post('/api/package/<name>/upload/<file>')
def upload(name, file):
    token = bottle.request.get_header("Authorization")
    if token == None:
        return common.api_error(401, "Unauthorized (missing Authorization header)")
    token = token.split(' ')
    if len(token) != 2 and token[0] != 'UmBox':
        return common.api_error(401, "Unauthorized (invalid Authorization header)")
    token = token[1]

    if not file in valid_filenames:
        return common.api_error(400, "This filename is not allowed")

    try:
        db.get_package(name)
    except:
        return common.api_error(400, "Package not found")

    if not package.authorize(name, token):
        return common.api_error(401, "Unauthorized")

    package.write_file(name, file, bottle.request.body.read())

    package.post_upload(name, file)

    return common.api_ok(None)


@bottle.get('/api/package/<name>/download/<file>')
def download(name, file):
    if file == "box.tar":
        db.increment_downloads(name)

    try:
        return bottle.static_file(file, root=f"packages/{name}")
    except FileNotFoundError:
        return common.api_error(404, "File not found")
