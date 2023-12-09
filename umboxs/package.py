
import hashlib
import os
import tarfile
import zipfile
import json
import bottle

from . import db


def authorize(name, token):
    try:
        module = db.get_package(name)
    except KeyError:
        return False

    return module.secret == token


def write_file(name, file, data):
    with open(f"packages/{name}/{file}", "wb") as f:
        f.write(data)


def post_upload(name, file):
    match os.path.basename(file):
        case "box.json":
            with open(f"packages/{name}/{file}", "r") as f:
                box = json.loads(f.read())

            if 'name' not in box:
                box['name'] = name
            if box['name'] != name:
                box['name'] = name
            if 'version' not in box:
                box['version'] = "v0.1.0"
            if 'description' not in box:
                box['description'] = ""
            if 'author' not in box:
                box['author'] = ""
            if 'license' not in box:
                box['license'] = ""
            if 'dependencies' not in box:
                box['dependencies'] = []
            if 'link' not in box:
                box['link'] = ""

            version = ""
            try:
                with open(f"packages/{name}/version", "r") as f:
                    version = f.read()
            except:
                pass

            if version.startswith(box["version"]):
                version = f"{box['version']}-{int(version.split('-')[1]) + 1}"
            else:
                version = f"{box['version']}-0"

            with open(f"packages/{name}/version", "w") as f:
                f.write(version)

        case "docs.zip":
            if not os.path.isdir(f"packages/{name}/docs"):
                os.mkdir(f"packages/{name}/docs")

            with zipfile.ZipFile(f"packages/{name}/{file}", "r") as zip_ref:
                zip_ref.extractall(f"packages/{name}/docs")

        case "box.tar":
            if not os.path.isdir(f"packages/{name}/data"):
                os.mkdir(f"packages/{name}/data")

            with tarfile.TarFile(f"packages/{name}/{file}", "r") as tf:
                tf.extractall(f"packages/{name}/data/")


@bottle.get('/package/<name>')
def package(name):
    return bottle.template('package', name=name, meta=db.get_meta(name))


@bottle.get('/package/<name>/browse/<path:path>')
def browse(name, path):
    return bottle.template('docs',
                           title=f"Browse {name}",
                           filepath=os.path.join(
                               "packages", name, "data", path),
                           wl=[".md", ".html", ".txt", ".um"],
                           dir=os.path.join("packages", name, "data"),
                           prefix=f"/package/{name}/browse")


@bottle.get('/package/<name>/browse')
@bottle.get('/package/<name>/browse/')
def browse_empty(name):
    return browse(name, "README.md")
