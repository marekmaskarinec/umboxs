import collections
import json
import psycopg2

Package = collections.namedtuple('Package', ['name', 'secret'])

conn = None


def init(dbname, user, password, host):
    global conn
    conn = psycopg2.connect(dbname=dbname, user=user,
                            password=password, host=host)


def load_packages() -> dict:
    cur = conn.cursor()
    cur.execute("SELECT * FROM pak_main_packages")
    result = cur.fetchall()
    cur.close()
    return {r[0]: r[1] for r in result}


def get_package(name: str) -> Package:
    cur = conn.cursor()
    cur.execute("SELECT * FROM pak_main_packages WHERE name = %s", (name,))
    result = cur.fetchone()
    cur.close()
    if result is None:
        raise KeyError()
    return Package(name=result[0], secret=result[1])


def set_package(package: Package):
    cur = conn.cursor()
    cur.execute("INSERT INTO pak_main_packages (name, token) VALUES (%s, %s)",
                (package.name, package.secret))
    cur.close()
    conn.commit()


def get_meta(name: str) -> dict:
    try:
        with open(f"packages/{name}/pak.json", "r") as f:
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
