#!/usr/bin/python3
# get response code

import requests

url = "https://alx-intranet.hbtn.io/status"
html = requests.get(url)
html_type = html.text.__class__
print("Body response:")
print(f"\t- type: {html_type}")
print(f"\t- content: {html.text}")
