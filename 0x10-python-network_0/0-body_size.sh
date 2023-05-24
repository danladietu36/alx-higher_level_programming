#!/bin/bash
# A script thata request to an URL with curl, and displays the size of the body of the response
curl -s "$1" | wc -c
