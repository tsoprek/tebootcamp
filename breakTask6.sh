#!/bin/bash
if dig +short c1.thousandeyes.com |grep -v .com;
  then dig +short c1.thousandeyes.com | grep -v '.com' |  while read address;
  do
        if ! grep $address known_c1_ip;
        then
          echo $address >> known_c1_ip
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