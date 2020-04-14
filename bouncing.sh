#!/bin/bash
export DISPLAY=:0
export HW=/home/packit/ece5486_hw7b
if [[ $1 != 'run' ]];
then
	exit 0
fi
pydir=`ls -d /tmp/pycore.*`
# Start mgen on node N2
/usr/local/bin/vcmd -c $pydir/n2 -- mgen input $HW/m6.mgen &
# Start gatherer on node N3
/usr/local/bin/vcmd -c $pydir/n3 -- python $HW/gatherer_ipv6.py > $HW/gatherer.log &
