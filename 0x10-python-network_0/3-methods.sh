#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods
curl -i -L -X "$1"
