#!/bin/bash
#displays the size of the body of the response
echo $(curl -s -o /dev/null -w "%{size_download}" "$1")
