#!/bin/bash
# Getting the response body for a given URL for 200 status code responses.
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
