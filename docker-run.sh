#!/bin/bash

docker run --rm -it -p 8080:3000 --name $1 --hostname $1 $1
