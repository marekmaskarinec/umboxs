
import bottle
import json

import common


@bottle.get('/api/search/<query>')
def search(query):
    return json.dumps([r[1] for r in common.search(query)])
