
import db
import hashlib
import os
import zipfile
import json
import bottle


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

            if 'name' not in pak:
                pak['name'] = name
            if pak['name'] != name:
                pak['name'] = name
            if 'version' not in pak:
                pak['version'] = "v0.1.0"
            if 'description' not in pak:
                pak['description'] = ""
            if 'author' not in pak:
                pak['author'] = ""
            if 'license' not in pak:
                pak['license'] = ""
            if 'dependencies' not in pak:
                pak['dependencies'] = []
            if 'link' not in pak:
                pak['link'] = ""

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
            if not os.path.isdir(f"packages/{name}/docs"):
                os.mkdir(f"packages/{name}/docs")

            with zipfile.ZipFile(f"packages/{name}/{file}", "r") as zip_ref:
                zip_ref.extractall(f"packages/{name}/docs")

        case "pak.zip":
            if not os.path.isdir(f"packages/{name}/data"):
                os.mkdir(f"packages/{name}/data")

            with zipfile.ZipFile(f"packages/{name}/{file}", "r") as zip_ref:
                zip_ref.extractall(f"packages/{name}/data/")


@bottle.get('/package/<name>')
def package(name):
    return bottle.template('package', name=name, meta=db.get_meta(name))
