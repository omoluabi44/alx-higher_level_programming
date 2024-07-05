#!/usr/bin/python3
""" POST method """

import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    res_data = requests.post(url, data=data)
    print(res_data.text)
