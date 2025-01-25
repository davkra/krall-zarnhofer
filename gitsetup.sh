#!/bin/bash

git remote remove origin
git remote add origin git@github.com:davkra/krall-zarnhofer.git

# Main Repository
git remote set-url --add --push origin git@github.com:davkra/krall-zarnhofer.git

# Mirror Repository
git remote set-url --add --push origin git@git-iit.fh-joanneum.at:msd-contdel/techdemo-ws24/krall-zarnhofer.git

git fetch

CURRENT_BRANCH=$(git branch --show-current)
git branch --set-upstream-to=origin/$CURRENT_BRANCH $CURRENT_BRANCH

git remote -v
