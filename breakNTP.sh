#!/bin/bash

#A script that adds # to working NTP servers.
#Other configured NTP servers are not reachable
#Exercise is to detect incorrect NTP servers, and work with ntp commands other then cut /etc/ntp.conf

sed -i 's/^server 10.48.26.73/#server 10.48.26.73/g' /etc/ntp.conf
sed -i 's/^server 10.48.26.66/#server 10.48.26.66/g' /etc/ntp.conf
date --set="2022-11-30 10:05:59.990"
systemctl restart ntp
