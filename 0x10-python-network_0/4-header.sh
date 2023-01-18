#!/bin/bash
# sending a get requet with var header "X-School-User-Id = 98"
curl -sL "$1" -X GET -H "X-School-User-Id : 98"
