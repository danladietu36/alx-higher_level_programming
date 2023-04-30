#!/usr/bin/env python3
# Bash script that takes in a URL, sends a request
curl -s "$1" | wc -c 
