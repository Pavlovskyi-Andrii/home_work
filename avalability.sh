#!/bin/bash
SERVER="dan-it.com.ua"
echo "Check server avalability $SERVER"
ping -c 4 "$SERVER" > /dev/null 2>&1

if [ $? -eq 0 ]; then
	TIME=$(curl -o /dev/null -s -w "%{time_connect}\n" "https://$SERVER")
	echo "responce time from the server: $TIME sec"
else
	echo "there is nom responce $SERVER"
fi
