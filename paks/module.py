
import db
import hashlib
import os
import zipfile


def authorize(name, token):
    try:
        module = db.get_module(name)
    except KeyError:
        return False

    return module.secret == hashlib.blake2b(token.encode()).hexdigest()


def write_file(name, file, data):
    with open(f"modules/{name}/{file}", "wb") as f:
        f.write(data)


def post_upload(name, file):
    match os.path.basename(file):
        case "docs.zip":
            with zipfile.ZipFile(f"modules/{name}/{file}", "r") as zip_ref:
                zip_ref.extractall(f"modules/{name}/")
