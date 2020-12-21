A python script to parse output of npm outdated command and compare with package.json dependencies, then execute proper npm install command.

Usage:

npm outdated | python3 outdated.py ./package.json

Reads npm outdated output in from stdin, must be passed in the location of the project's package.json directory for comparison.
