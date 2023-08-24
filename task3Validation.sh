#!/bin/bash
source lab_config
if grep "$dns_server" /etc/netplan/00-installer-config.yaml 1>/dev/null;
  then
    if dig cisco.com 1>/dev/null; then
	  echo '0'
	  fi
elif ! grep "$dns_server" /etc/netplan/00-installer-config.yaml 1>/dev/null && grep "$dns_server" /etc/resolv.conf 1>/dev/null;
  then
    if dig cisco.com 1>/dev/null; then
	  echo '2'
	  fi
elif grep '10.48.26.74' /etc/netplan/00-installer-config.yaml 1>/dev/null && ! grep "$dns_server" /etc/resolv.conf 1>/dev/null;
  then
	echo '1'
fi