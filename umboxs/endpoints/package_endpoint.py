
import bottle

from umboxs import package
from umboxs import db

valid_filenames = [
    "box.json",
    "box.tar",
    "docs.md"
]


@bottle.post('/api/package/<name>/<token>/upload/<file>')
def upload(name, token, file):
    if not file in valid_filenames:
        return bottle.HTTPError(400, "Invalid filename")

    try:
        db.get_package(name)
    except:
        return bottle.HTTPError(404, "Package not found")

    if not package.authorize(name, token):
        return bottle.HTTPError(401, "Invalid token")

    package.write_file(name, file, bottle.request.body.read())

    package.post_upload(name, file)

    return bottle.HTTPResponse(status=200)


@bottle.get('/api/package/<name>/download/<file>')
def download(name, file):
    try:
        return bottle.static_file(file, root=f"packages/{name}")
    except FileNotFoundError:
        return bottle.HTTPError(404, "File not found")
