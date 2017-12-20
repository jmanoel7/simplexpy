#!/bin/sh -e
tag='latest'
[[ -n "$1" ]] && tag="$1"
docker login
exec docker pull jmanoel7/sistec-download:$tag
