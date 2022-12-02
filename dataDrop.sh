#!/bin/bash

#ipaddr=`dig +short data1.agt.thousandeyes.com |grep -v .com`
#addresses=`echo $ipaddr | sed 's/ /,/'`
#echo $addresses
#iptables -A OUTPUT -d $addresses -p tcp --dport 443 -j DROP 2>&1

dig +short data1.agt.thousandeyes.com |grep -v thousandeyes.com >> known_data_ip
sort -u known_c1_ip | while read address;
do
iptables -A OUTPUT -d $addresses -p tcp --dport 443 -j DROP
done