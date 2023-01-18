#!/bin/bash
# Displays all HTTP methods the server will accept
curl -sI "$1" -X OPTIONS | grep "access-control-allow-methods" | cut -d ' ' -f2
