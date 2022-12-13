#!/bin/bash

if grep '10.48.26.73' /etc/netplan/00-installer-config.yaml 1>/dev/null;
  then
    if dig cisco.com; then
	  echo '0'
	  fi
elif ! grep '10.48.26.73' /etc/netplan/00-installer-config.yaml 1>/dev/null && grep '10.48.26.73' /etc/resolv.conf 1>/dev/null;
  then
    if dig cisco.com; then
	  echo '2'
	  fi
elif grep '10.48.26.74' /etc/netplan/00-installer-config.yaml 1>/dev/null && ! grep '10.48.26.73' /etc/resolv.conf 1>/dev/null;
  then
	echo '1'
fi