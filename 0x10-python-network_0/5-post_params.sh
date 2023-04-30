#!/bin/bash
# Bash script that takes in a URL,variables and sends a POST request
curl -sX -H POST "email: test@gmail.com, subject:I will always be here for PLD" "$1"
