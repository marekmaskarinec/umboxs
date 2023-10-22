
import bottle

import module

valid_filenames = [
    "pak.json",
    "pak.zip",
    "docs.md"
]


@bottle.post('/module/<name>/<token>/upload/<file>')
def upload(name, token, file):
    if not file in valid_filenames:
        return bottle.HTTPError(400, "Invalid filename")

    if not module.authorize(name, token):
        return bottle.HTTPError(401, "Invalid token")

    module.write_file(name, file, bottle.request.body.read())

    module.post_upload(name, file)

    return bottle.HTTPResponse(status=200)


@bottle.get('/module/<name>/download/<file>')
def download(name, file):
    try:
        with open(f"modules/{name}/{file}", "rb") as f:
            return f.read()
    except FileNotFoundError:
        return bottle.HTTPError(404, "File not found")
