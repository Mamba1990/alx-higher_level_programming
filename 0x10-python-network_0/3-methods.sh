#!/bin/bash
# Displaying all HTTP methods the server of a given URL will accept.
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
