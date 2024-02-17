import collections
import json
import sqlite3

Package = collections.namedtuple('Package', ['name', 'secret'])

conn = None


def init(path):
    global conn
    conn = sqlite3.connect(path)


def load_packages() -> dict:
    cur = conn.cursor()
    cur.execute("SELECT * FROM packages")
    result = cur.fetchall()
    cur.close()
    return {r[0]: r[1] for r in result}


def get_package(name: str) -> Package:
    cur = conn.cursor()
    cur.execute("SELECT * FROM packages WHERE name = ?", (name,))
    result = cur.fetchone()
    cur.close()
    if result is None:
        raise KeyError()
    return Package(name=result[0], secret=result[1])


def set_package(package: Package):
    cur = conn.cursor()
    cur.execute("INSERT INTO packages (name, token) VALUES (?, ?)",
                (package.name, package.secret))
    cur.close()
    conn.commit()


def get_meta(name: str) -> dict:
    try:
        with open(f"packages/{name}/box.json", "r") as f:
            return json.loads(f.read())
    except:
        return {
            "name": name,
            "description": "No description",
            "version": "0.0.0",
            "author": "Unknown",
            "license": "Unknown",
            "dependencies": []
        }
