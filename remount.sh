#!/bin/sh

MOUNT_POINT=/nas-photos

while true
do
	if ! mountpoint -q $MOUNT_POINT; then
		sudo mount $MOUNT_POINT
	fi
	
	sleep 5m
done
