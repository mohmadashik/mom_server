#!/bin/bash
set -e
NAME='goalder-backend-service'
echo -n "Stopping daemon: $NAME\n"
kill -9 `sudo lsof -t -i:5000` &
echo -n "Stopped daemon: $NAME\n"
exit