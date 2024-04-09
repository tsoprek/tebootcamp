#!/bin/bash
source lab_config
if grep "$dns_server" /etc/netplan/50-cloud-init.yaml 1>/dev/null;
  then
        echo '0'
elif ! grep "$dns_server" /etc/netplan/50-cloud-init.yaml 1>/dev/null && grep "$dns_server" /etc/resolv.conf 1>/dev/null;
  then
    if dig cisco.com 1>/dev/null; then
	  echo '2'
	  fi
elif grep "$wrong_dns_server" /etc/netplan/50-cloud-init.yaml 1>/dev/null && ! grep "$dns_server" /etc/resolv.conf 1>/dev/null;
  then
	echo '1'
fi