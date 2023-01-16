#!/bin/bash
# sends a GET request and displays the body of respnce only if status is 200
if [ "$(curl -sI "$1" | grep "HTTP" | cut -d ' ' -f2)" = '200' ];
then curl -s "$1"; fi
