#!/bin/sh -e
cat ./Dockerfile.exec | exec docker build -t sistec-download -
