
import db
import hashlib
import os
import zipfile
import json


def authorize(name, token):
    try:
        module = db.get_package(name)
    except KeyError:
        return False

    return module.secret == hashlib.blake2b(token.encode()).hexdigest()


def write_file(name, file, data):
    with open(f"packages/{name}/{file}", "wb") as f:
        f.write(data)


def post_upload(name, file):
    match os.path.basename(file):
        case "pak.json":
            with open(f"packages/{name}/{file}", "r") as f:
                pak = json.loads(f.read())

            version = ""
            try:
                with open(f"packages/{name}/version", "r") as f:
                    version = f.read()
            except:
                pass

            if version.startswith(pak["version"]):
                version = f"{pak['version']}-{int(version.split('-')[1]) + 1}"
            else:
                version = f"{pak['version']}-0"

            with open(f"packages/{name}/version", "w") as f:
                f.write(version)

        case "docs.zip":
            with zipfile.ZipFile(f"packages/{name}/{file}", "r") as zip_ref:
                zip_ref.extractall(f"packages/{name}/")
