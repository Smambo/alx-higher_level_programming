#!/bin/bash
# script sends DELETE request to URL passed as 1st arg
# and displays body of the response
curl -sX DELETE "$1"
