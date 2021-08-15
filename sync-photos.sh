#!/bin/sh

FROM_DIR=/nas-photos/frame/
TO_DIR=/home/pi/Pictures/
RSYNC_OPTIONS="-av --del"

if rsync ${RSYNC_OPTIONS} ${FROM_DIR} ${TO_DIR}; then
	echo "Last Sync: $(date)" > /home/pi/bin/sync-photos.txt
else
	echo "Failed Sync: $(date)" > /home/pi/bin/sync-photos.txt
fi
