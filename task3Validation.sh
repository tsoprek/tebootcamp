#!/bin/bash

if grep '10.48.26.74' /etc/netplan/00-installer-config.yaml 1>/dev/null && nslookup cisco.com 1>/dev/null;
  then
	echo '0'
elif grep '10.48.26.74' /etc/netplan/00-installer-config.yaml 1>/dev/null && ! nslookup cisco.com 1>/dev/null;
  then
	echo '2'
elif ! grep '10.48.26.74' /etc/netplan/00-installer-config.yaml 1>/dev/null && nslookup cisco.com 1>/dev/null;
  then
	echo '2'
elif ! grep '10.48.26.74' /etc/netplan/00-installer-config.yaml 1>/dev/null && ! nslookup cisco.com 1>/dev/null;
  then
	echo '1'
fi