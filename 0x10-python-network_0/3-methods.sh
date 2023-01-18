#!/bin/bash
# displays all HTTP methods the server will accept
sudo curl -sI "$1" -X OPTIONS | grep "access-control-allow-methods" | cut -d' ' -f2
