#!/usr/bin/python3
""" POST method """

import sys
import requests
import json

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    resp_data = requests.post(url, data=data)
    try:
        json_data = resp_data.json()
        if json_data:
            id = json_data.get('id')
            name = json_data.get('name')
            if id is None and name is None:
                print("No result")
            else:
                print(f"[{id}] {name}")
    except ValueError:
        print("Not a valid JSON")
