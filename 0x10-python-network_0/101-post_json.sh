#!/bin/bash
# script sends JSON post request to a url, displays body of response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
