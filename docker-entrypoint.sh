#!/bin/bash

if [ "$(ls -A $/home/user/GitHub)" ]; then
	echo "Using existing git state"
else
	mkdir /home/user/GitHub
    # #clone repositories
    # cd /home/user/GitHub
    # python3  

fi

#manually keep the container running
sleep infinity