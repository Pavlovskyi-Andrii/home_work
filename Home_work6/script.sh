#!/bin/bash
#

disc_log=${1}
disc_now=$(df / | grep / | awk '{ print $5 } ' | sed 's/%//g')
echo "$disc_now"
echo "$disc_log"

if [[ $disc_now -gt $disc_log ]]; then
	echo "used space disc more than $disc_log " >> /var/log/disc.log
fi
