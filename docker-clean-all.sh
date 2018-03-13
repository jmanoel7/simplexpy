#!/bin/bash

IFS=$'\n'

for i in `docker container ls -a | tail -n +2 | sed 's/^\([0-9a-z]\{12\}\)[[:blank:]]\+\([0-9a-z]\{12\}\)[[:blank:]]\+.*$/\1 \2/'`; do

    container=`echo $i | cut -d ' ' -f 1`
    #echo "container=$container"

    image=`echo $i | cut -d ' ' -f 2`
    #echo "image=$image"

    echo -en "\a\n\tclean container: $container ... "
    docker container kill $container 1>/dev/null 2>&1
    exit_kill_container=$?
    docker container rm -f $container 1>/dev/null 2>&1
    exit_rm_container=$?
    if [ $exit_kill_container -eq 0 -a $exit_rm_container -eq 0 ]; then
	    echo "OK"
    else
	    echo "NOT OK"
    fi

    echo -en "\a\n\tclean image: $image ... "
    docker image rm -f $image 1>/dev/null 2>&1
    exit_rm_image=$?
    if [ $exit_rm_image -eq 0 ]; then
	    echo "OK"
    else
	    echo "NOT OK"
    fi

done

for i in `docker image ls -a | tail -n +2 | sed 's/^[^[:blank:]]\+[[:blank:]]\+[^[:blank:]]\+[[:blank:]]\+\([0-9a-z]\{12\}\)[[:blank:]]\+.*$/\1/'`; do

    image=`echo $i`
    #echo "image=$image"

    echo -en "\a\n\tclean image: $image ... "
    docker image rm -f $image 1>/dev/null 2>&1
    exit_rm_image=$?
    if [ $exit_rm_image -eq 0 ]; then
	    echo "OK"
    else
	    echo "NOT OK"
    fi

done

exit 0
