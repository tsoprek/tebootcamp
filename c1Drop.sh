#!/bin/bash

#ipaddr=`dig +short c1.thousandeyes.com |grep -v .com`
#addresses=`echo $ipaddr | sed 's/ /,/'`
#iptables -A OUTPUT -d $addresses -p tcp --dport 443 -j DROP

dig +short c1.thousandeyes.com |grep -v thousandeyes.com >> known_c1_ip
sort -u known_c1_ip | while read address;
do
iptables -A OUTPUT -d $address -p tcp --dport 443 -j DROP
done