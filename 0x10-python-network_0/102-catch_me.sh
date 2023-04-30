#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sL -X PUT "Origin: HolbertonScholl" -d "user:_id=98" 0.0.0.0:5000/catch_me
