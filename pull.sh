#!/bin/sh -e
tag='latest'
[[ -n "$1" ]] && tag="$1"
exec docker pull jmanoel7/simplexpy:$tag
