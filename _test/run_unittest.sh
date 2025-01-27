#!/bin/bash

SCRIPTDIR="$(dirname "$(readlink -f "$0")")"

docker run --rm -it -u $(id -u):$(id -g) -v "$SCRIPTDIR/../calculator":/app --init -p 8080:3000 --name calculator --hostname calculator calculator sh -c 'python -m unittest discover -s tests/unit'
