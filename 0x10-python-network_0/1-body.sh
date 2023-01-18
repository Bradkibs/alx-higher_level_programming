#!/bin/bash
# sends a GET request and displays the body of respnce only if status is 200
if [ "$(sudo curl -sLI -X GET "$1" | grep "200 OK" | cut -d ' ' -f2)" = '200' ]; then curl -sL "$1"; fi
