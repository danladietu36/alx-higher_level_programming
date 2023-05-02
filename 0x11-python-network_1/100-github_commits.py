#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line).
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    response = requests.get(url)
    comms = response.json()
    try:
        for x in range(10):
            print("{}: {}".format(
                comms[i].get("sha"),
                comms[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
