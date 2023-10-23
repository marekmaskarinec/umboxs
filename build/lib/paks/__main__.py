#!/usr/bin/env python
import bottle
import os

from paks import db
import common

from paks.endpoints import register_endpoint
from paks.endpoints import search_endpoint
from paks.endpoints import package_endpoint


@bottle.get('/static/<filepath:path>')
def file(filepath):
    fname, ext = os.path.splitext(filepath)

    if ext == "":
        return file(filepath + "index.md")

    if fname == "":
        return file(filepath + "/index.md")

    if ext == ".md":
        return bottle.template('markdown', title=fname, filepath=os.path.join('static', filepath))

    return bottle.static_file(filepath, root='static')


@bottle.get('/')
@bottle.get('')
def root():
    return file('index.md')


@bottle.get('/all')
def all():
    packs = db.load_packages().keys()

    return bottle.template('packages', title="All packages", packages=[(pack, db.get_meta(pack)) for pack in packs])


@bottle.post('/search')
def search():
    query = bottle.request.forms.get('query')

    packs = common.search(query)

    bottle.TEMPLATES.clear()
    return bottle.template('packages', title=f"Search results for '{query}'", packages=packs)


def notapi_filter(config):
    return not config['path'].startswith('/api')


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080, debug=True)
