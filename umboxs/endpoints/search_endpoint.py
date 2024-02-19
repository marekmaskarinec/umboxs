
import bottle
import json

from umboxs import common


@bottle.get('/api/search/<query>')
def search(query):
    return common.api_ok([r[1] for r in common.search(query)])
