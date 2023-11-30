#!/bin/bash
# script sends GET request and displays body of response
curl -sX GET -H "X-School-User-Id: 98" "$1"
