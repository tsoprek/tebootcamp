#!/bin/bash
sed -i 's/10.48.26.73/10.48.26.74/g' /etc/netplan/00-installer-config.yaml
netplan apply
if grep '10.48.26.74' /etc/netplan/00-installer-config.yaml > /dev/null ;
  then
  echo 'DNS Broken'
else
  echo 'DNS Break FAILED!'
fi
