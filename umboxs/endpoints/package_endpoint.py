
import bottle
import os
import brotli
import mimetypes

from umboxs import package
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

    pack = package.Package(name)
    if not pack.exists():
        return common.api_error(400, "Package not found")

    if not pack.authorize(token):
        return common.api_error(401, "Unauthorized")

    pack.write_file(file, bottle.request.body.read())
    pack.post_upload(file)

    return common.api_ok(None)


@bottle.get('/api/package/<name>/download/<file>')
def download(name, file):
    pack = package.Package(name)
    if file == "box.tar":
        pack.inc_downloads()

    root = os.path.abspath(pack.fpath(""))
    file = os.path.abspath(os.path.join(root, file.strip('/\\')))
    if not file.startswith(root):
        return common.api_error(403, "Access denied.")
    if not os.path.exists(file) or not os.path.isfile(file):
        return common.api_error(404, "File does not exist.")
    if not os.access(file, os.R_OK):
        return common.api_error(403, "You do not have permission to access this file.")

    with open(file, "rb") as f:
        data = f.read()
    
    headers = {}
    mimetype, encoding = mimetypes.guess_type(file)
    if mimetype:
        headers["Content-Type"] = mimetype
    if encoding:
        headers["Content-Encoding"] = encoding

    if "br" in bottle.request.get_header("Accept-Encoding", ""):
        data = brotli.compress(data)
        headers["Content-Encoding"] = 'br'
        headers["Vary"] = 'Accept-Encoding'

    return bottle.HTTPResponse(data, status=200, headers=headers)
