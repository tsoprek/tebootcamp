#!/bin/bash

#Script to change DNS server to one that is not used in topology and apply the config.
# Exercise is to detect incorrectly configured DNS servers as per topology. 
#Inspecting or adding the server to resolve.conf is incorrect as ubuntu uses netplan and this is not persistent.
source lab_config

sed -i "s/$dns_server/10.48.26.74/g" /etc/netplan/50-cloud-init.yaml
netplan apply
if grep '10.48.26.74' /etc/netplan/50-cloud-init.yaml 1>/dev/null ;
  then
  echo 'DNS Broken'
else
  echo 'DNS Break FAILED!'
fi
