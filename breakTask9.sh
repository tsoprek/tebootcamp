#!/bin/bash

#A script that adds # to working NTP servers.
#Other configured NTP servers are not reachable
#Exercise is to detect incorrect NTP servers, and work with ntp commands other then cut /etc/ntp.conf
source lab_config
sed -i "s/^server $ntp_server/#server $ntp_server/g" /etc/ntp.conf
sed -i "s/^pool/#pool/g" /etc/ntp.conf
date_hour_ago=`date -d '5.5 hour ago' "+%Y-%m-%d %H:%M:%S"`
date --set="$date_hour_ago"
systemctl restart ntp
