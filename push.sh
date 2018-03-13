#!/bin/sh -e
tag='latest'
[[ -n "$1" ]] && tag="$1"
docker login
docker tag simplexpy jmanoel7/simplexpy:$tag
exec docker push jmanoel7/simplexpy:$tag
