
import bottle

from paks import package

valid_filenames = [
    "pak.json",
    "pak.zip",
    "docs.md"
]


@bottle.post('/api/package/<name>/<token>/upload/<file>')
def upload(name, token, file):
    if not file in valid_filenames:
        return bottle.HTTPError(400, "Invalid filename")

    if not package.authorize(name, token):
        return bottle.HTTPError(401, "Invalid token")

    package.write_file(name, file, bottle.request.body.read())

    package.post_upload(name, file)

    return bottle.HTTPResponse(status=200)


@bottle.get('/api/package/<name>/download/<file>')
def download(name, file):
    try:
        with open(f"packages/{name}/{file}", "rb") as f:
            return f.read()
    except FileNotFoundError:
        return bottle.HTTPError(404, "File not found")
