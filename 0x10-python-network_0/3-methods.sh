#!/bin/bash
# displays all HTTP methods the server will accept
curl -sX OPTION "$1"
