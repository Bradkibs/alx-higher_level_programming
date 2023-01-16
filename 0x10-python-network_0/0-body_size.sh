#!/bin/bash
# A script that displays the size of the body of response
curl -s -I "$1" | grep 'Content-Length' | cut -d ' ' -f2
