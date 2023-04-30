#!/bin/bash
#Bash script that sends a request to a URL passed as an argument and display only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
