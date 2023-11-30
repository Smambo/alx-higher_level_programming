#!/bin/bash
# script displays size of body of response to URL request
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
