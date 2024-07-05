#!/usr/bin/python3
""" POST method """

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    r = requests.post(url, data=data)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
