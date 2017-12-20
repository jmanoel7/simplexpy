#!/bin/sh -e
tag='latest'
[[ -n "$1" ]] && tag="$1"
docker login
docker tag sistec-download jmanoel7/sistec-download:$tag
exec docker push jmanoel7/sistec-download:$tag
