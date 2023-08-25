#!/bin/bash
source lab_config
sed -i "s/10.48.26.74/$dns_server/g" /etc/netplan/50-cloud-init.yaml
netplan apply
if grep '10.48.26.73' /etc/netplan/50-cloud-init.yaml > /dev/null ;
  then
  echo 'DNS Fixed'
else
  echo 'DNS Fix failed'
fi 
