#!/usr/bin/python3
""" POST method """

import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    enc_data = urllib.parse.urlencode(data).encode('utf-8')

    res_data = urllib.request.Request(url, data=enc_data)

    with urllib.request.urlopen(res_data) as response:
        response_body = response.read().decode('utf-8')
    print(response_body)
