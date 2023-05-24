#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me to gets the message "You got me!". displayed
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "userId=98" 0.0.0.0:5000/catch_me
