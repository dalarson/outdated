#! /usr/bin/env python3

import json
import os
import sys


def main():

    # load package.json file and extract devDeps and prodDeps
    data = importPackageJson()
    devDeps, deps = data['devDependencies'].keys(
    ), data['devDependencies'].keys()

    outdatedDevDeps = []
    outdatedProdDeps = []

    # create lists of outdated dev and prod dependencies

    for line in sys.stdin:
        print(line[:-1])
        package = line.split(" ")[0]
        if package in devDeps:
            outdatedDevDeps.append(package)
        elif package in deps:
            outdatedProdDeps.append(package)

    if len(outdatedDevDeps) == 0 and len(outdatedProdDeps) == 0:
        print("No outdated dependencies!")
        quit(0)

    print("\nOutdated dev dependencies:\n" + ("\n".join(
        outdatedDevDeps) if len(outdatedDevDeps) > 0 else "None!"))
    print("\nOutdated prod dependencies:\n" + ("\n".join(
        outdatedProdDeps) if len(outdatedProdDeps) > 0 else "None!"))

    print()

    # build the npm install command strings
    devDepsStr = ""
    prodDepsStr = ""

    if len(outdatedDevDeps) > 0:
        devDepsStr = f"""npm install {" ".join([f'{package}@latest' for package in outdatedDevDeps])} --save-dev"""
        print(devDepsStr)
        # os.system(devDepsStr)
    if len(outdatedProdDeps) > 0:
        prodDepsStr = f"""npm install {" ".join([f'{package}@latest' for package in outdatedProdDeps])}  --save"""
        print(prodDepsStr)
        # os.system(prodDepsStr)


def importPackageJson():
    path = sys.argv[1] if len(sys.argv) > 1 else './package.json'
    try:
        with open(path) as f:
            data = json.load(f)
            return data
    except OSError:
        print("Error: package.json file not found. Please pass in as argument or run in folder containing package.json.")
        quit(1)


main()
