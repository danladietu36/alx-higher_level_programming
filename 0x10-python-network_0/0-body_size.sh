#!/usr/bin/env python3
# Bash script that takes in a URL, sends a request
# to that URL, and displays the size of the body of the response
name=URL
curl -sI $name | grep -i Content-Length 
