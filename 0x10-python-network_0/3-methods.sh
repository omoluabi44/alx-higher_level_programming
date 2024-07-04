#!/bin/bash
#get respond body if status code is 200
Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
