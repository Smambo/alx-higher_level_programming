#!/bin/bash
# sends POST request to passed URL and displays body of response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
