#!/bin/bash
sed -i 's/10.48.26.74/10.48.26.73/g' /etc/netplan/00-installer-config.yaml
netplan apply
if grep '10.48.26.73' /etc/netplan/00-installer-config.yaml > /dev/null ;
  then
  echo 'DNS Fixed'
else
  echo 'DNS Fix failed'
fi 
