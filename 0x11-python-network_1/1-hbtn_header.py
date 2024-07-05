#!/usr/bin/python3
''' get x-resquest id'''

import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.getheaders()
        id = dict(html).get("X-Request-Id")
    print(f"{id}")
