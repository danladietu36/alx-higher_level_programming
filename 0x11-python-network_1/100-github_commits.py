#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line).
"""
import requests
import sys

repo_name = sys.argv[1]
owner_name = sys.argv[2]

url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

response = requests.get(url)

if response.status_code == 200:
    commits = response.json()[:10]
    for commit in commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f'{sha}: {author}')
else:
    print(f'Error: {response.status_code}')
