#!/bin/bash
#get respond body if status code is 200
curl -s -o - -w "%{http_code}" "1" | { read -r body status; [ "$status" -eq 200 ] && echo "$body"; }
