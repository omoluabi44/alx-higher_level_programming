#!/bin/bash
#get respond body if status code is 200
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
