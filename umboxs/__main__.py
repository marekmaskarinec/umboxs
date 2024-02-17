#!/usr/bin/env python
import bottle
import os
import argparse

from . import db
from . import common

from .endpoints import register_endpoint
from .endpoints import search_endpoint
from .endpoints import package_endpoint

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


@bottle.get('/dl/<filepath:path>')
def dl(filepath):
    bottle.redirect(f"https://mrms.cz/dl/umbox/{filepath}")


@bottle.get('/docs/<filepath:path>')
def docs(filepath):
    return bottle.template('docs',
                           title=f"{filepath}",
                           filepath=os.path.join("static/docs", filepath),
                           wl=['.md', '.html'],
                           dir='static/docs',
                           prefix='/docs')


@bottle.get('/docs')
@bottle.get('/docs/')
def docs_empty():
    return docs('01-index.md')


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
    par = argparse.ArgumentParser(prog="UmBoxS", description='UmBox server')

    par.add_argument('--host', type=str, default='localhost',
                     help='Host to bind to')
    par.add_argument('--port', type=int, default=4832, help='Port to bind to')
    par.add_argument('--debug', action='store_true', help='Enable debug mode')

    par.add_argument('--db', type=str, default=None, help='Path to sqlite3 database')
    par.add_argument('--no-register', action='store_true', default=False)

    ns = par.parse_args()
    
    register_endpoint.enable = not ns.no_register

    if ns.db != None:
        db.init(ns.db)

    bottle.TEMPLATES.clear()
    bottle.run(host=ns.host, port=ns.port, debug=ns.debug)
