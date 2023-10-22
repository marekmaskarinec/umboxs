#!/usr/bin/env python

import bottle

from endpoints import register_endpoint
from endpoints import package_endpoint

if __name__ == "__main__":
    bottle.run(host='localhost', port=8080, debug=True)
