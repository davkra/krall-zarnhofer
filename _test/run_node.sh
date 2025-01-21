#!/bin/bash

SCRIPTDIR="$(dirname "$(readlink -f "$0")")"
cd "$SCRIPTDIR"

cd ..
docker build -t calculator .

cd "$SCRIPTDIR"

docker run --rm -it --init -p 8080:3000 --name calculator --hostname calculator calculator sh -c 'npm start'
