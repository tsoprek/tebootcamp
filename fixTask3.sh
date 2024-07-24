#!/bin/bash
source lab_config
sed -i "s/$wrong_dns_server/$dns_server/g" /etc/netplan/50-cloud-init.yaml
netplan apply
dhclient
while iptables -S | grep "udp --sport 53 -j DROP";
  do sudo iptables -D INPUT -p udp --sport 53 -j DROP
done
if grep "$dns_server" /etc/netplan/50-cloud-init.yaml > /dev/null ;
  then
  echo 'DNS Fixed'
else
  echo 'DNS Fix failed'
fi 
