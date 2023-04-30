#!/bin/bash
#Bash script that sends a request to a URL passed as an argument and display only status code
curl -s -I "%{http_code}" "$1"
