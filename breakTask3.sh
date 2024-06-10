#!/bin/bash

#Script to change DNS server to one that is not used in topology and apply the config.
# Exercise is to detect incorrectly configured DNS servers as per topology. 
#Inspecting or adding the server to resolve.conf is incorrect as ubuntu uses netplan and this is not persistent.
source lab_config

sed -i "s/$dns_server/$wrong_dns_server/g" /etc/netplan/50-cloud-init.yaml
netplan apply
if ! iptables -S | grep "udp --sport 53 -j DROP";
  then sudo iptables -A INPUT -p udp --sport 53 -j DROP
fi
if grep "$wrong_dns_server" /etc/netplan/50-cloud-init.yaml 1>/dev/null ;
  then
  echo 'DNS Broken'
else
  echo 'DNS Break FAILED!'
fi
