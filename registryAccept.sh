#!/bin/bash

#ipaddr=`dig +short registry.agt.thousandeyes.com |grep -v thousandeyes.com`
#addresses=`echo $ipaddr | sed 's/ /,/'`
#iptables -D OUTPUT -d $addresses -p tcp --dport 443 -j DROP

sort -u known_registry_ip | while read address;
do
iptables -D OUTPUT -d $addresses -p tcp --dport 443 -j DROP
done