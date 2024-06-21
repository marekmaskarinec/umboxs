
import bottle
import hashlib
import json
import os
import secrets
import sqlite3
import tarfile
import zipfile

conn = None

class Package:
    def __init__(self, name):
        self.name = name
        self.has_db = False

    def load_db(self):
        if self.has_db:
            return

        cur = conn.cursor()
        cur.execute("SELECT * FROM packages WHERE name = ?", (self.name,))
        result = cur.fetchone()
        cur.close()

        if result is None:
            raise KeyError()

        self.secret = result[1]
        self.download_count = result[2]

        self.has_db = True

    def save_db(self):
        cur = conn.cursor()
        cur.execute("INSERT INTO packages (name, token) VALUES (?, ?)",
                    (self.name, self.secret))
        cur.close()
        conn.commit()

    def fpath(self, file):
        return f"packages/{self.name}/{file}"

    def get_meta(self):
        try:
            with open(self.fpath("box.json"), "r") as f:
                return json.loads(f.read())
        except:
            return {
                "name": self.name,
                "description": "No description (NOTE: seems like the box.json file is missing)",
                "version": "0.0.0",
                "author": "Unknown",
                "license": "Unknown",
                "dependencies": []
            }

    def post_upload(self, file):
        match os.path.basename(file):
            case "box.tar":
                if not os.path.isdir(self.fpath("data")):
                    os.mkdir(self.fpath("data"))

                with tarfile.TarFile(self.fpath(file), "r") as tf:
                    tf.extractall(self.fpath("data/"))

                box = {}
                with open(self.fpath("data/box.json"), "r") as f:
                    box = json.loads(f.read())
                    
                if 'name' not in box:
                    box['name'] = self.name
                if box['name'] != self.name:
                    box['name'] = self.name
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

                with open(self.fpath("box.json"), "w") as f:
                    f.write(json.dumps(box, indent=4))

                version = ""
                try:
                    with open(self.fpath("version"), "r") as f:
                        version = f.read()
                except:
                    pass

                if version.startswith(box["version"]):
                    version = f"{box['version']}-{int(version.split('-')[1]) + 1}"
                else:
                    version = f"{box['version']}-0"

                with open(self.fpath("version"), "w") as f:
                    f.write(version)

    def write_file(self, file, data):
        with open(self.fpath(file), "wb") as f:
            f.write(data)

    def inc_downloads(self):
        if not self.has_db:
            self.load_db()
        self.download_count += 1
        cur = conn.cursor()
        cur.execute("UPDATE packages SET download_count = ? WHERE name = ?", (self.download_count + 1, self.name))
        cur.close()
        conn.commit()
        
    def register(self):
        token = secrets.token_hex(32)
        secret = hashlib.blake2b(token.encode()).hexdigest()

        self.secret = secret
        self.save_db()
        os.mkdir(self.fpath(""))
        
        return token

    def exists(self):
        if self.has_db:
            return True
        try:
            self.load_db()
        except:
            return False

        return True

    def authorize(self, secret):
        if not self.has_db:
            self.load_db()
        return secret == self.secret

def init_db(path):
    global conn
    conn = sqlite3.connect(path)

def load_all(order = 'name', asc = True) -> list[str]:
    cur = conn.cursor()
    cur.execute(f"SELECT name from PACKAGES ORDER BY ? {"ASC" if asc else "DESC"}", (order,))
    res = cur.fetchall()
    cur.close()
    return [r[0] for r in res]

@bottle.get('/package/<name>')
def package(name):
    pack = Package(name)
    pack.load_db()
    return bottle.template('package', pack=pack, meta=pack.get_meta())


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
