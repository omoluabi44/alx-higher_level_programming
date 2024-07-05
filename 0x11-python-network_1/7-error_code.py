#!/usr/bin/python3
""" POST method """

import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    res_data = requests.get(url)
    if res_data.status_code >= 400:
        print(f"Error code: {res_data.status_code}")
    else:
        print(res_data.text)
