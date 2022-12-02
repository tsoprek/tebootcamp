#!/bin/bash

#ipaddr=`dig +short c1.thousandeyes.com |grep -v .com`
#addresses=`echo $ipaddr | sed 's/ /,/'`
#iptables -D OUTPUT -d $addresses -p tcp --dport 443 -j DROP

sort -u known_c1_ip | while read address;
do
iptables -D OUTPUT -d $address -p tcp --dport 443 -j DROP
done