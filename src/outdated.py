#! /usr/bin/env python3

import json
import os
import sys

def main():

    if (sys.argv[1]):
        data = importPackageJson(sys.argv[1])
        devDeps, deps = data['devDependencies'].keys(), data['devDependencies'].keys()

    devStr = "npm install"
    depStr = "npm install"

    for line in sys.stdin:
        package = line.split(" ")[0]
        if package in devDeps:
            devStr += (' ' + package + '@latest')
        elif package in deps:
            depStr += (' ' + package + '@latest')

    if len(devDeps) > 0:
        os.system(devStr)
    if len(deps) > 0:
        os.system(depStr)
        

    


def importPackageJson(path):
    with open(path) as f:
        data = json.load(f)
        return data


main()


