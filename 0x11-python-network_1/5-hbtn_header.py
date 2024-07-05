#!/usr/bin/python3
''' get x-resquest id'''

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    id = requests.get(url).headers.get("X-Request-Id")
    print(f"{id}")
