#!/bin/bash
if dig +short registry.agt.thousandeyes.com |grep -v thousandeyes.com;
  then dig +short registry.agt.thousandeyes.com |grep -v thousandeyes.com |  while read address;
  do
        if ! grep $address known_registry_ip;
        then
          echo $address >> known_registry_ip
          echo 'Address added to known_registry_ip'
        else
          echo 'Address already in known_registry_ip'
        fi

	if ! iptables -S | grep $address;
        then
          iptables -A OUTPUT -d $address -p tcp --dport 443 -j DROP
          echo 'Address added to iptables'
        else
          echo 'Address already in iptables'
        fi
  done
fi