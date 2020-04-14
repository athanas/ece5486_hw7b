#!/bin/bash
export DISPLAY=:0
export HW=/home/packit/ece5486_hw7b
if [[ $1 != 'stop' ]];
then
	exit 0
fi
pydir=`ls -d /tmp/pycore.*`
#kill `pgrep vcmd`
kill `pgrep python`
kill `pgrep mgen`
