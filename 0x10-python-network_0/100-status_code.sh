#!/bin/bash
# script sends request to url passed as argument, displays status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
