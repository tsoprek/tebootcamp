#!/bin/bash

#ipaddr=`dig +short data1.agt.thousandeyes.com |grep -v .com`
#echo $ipaddr | sed 's/ /\n/' | while read line;
#  do
#  echo $line
#  iptables -D OUTPUT -d $line -p tcp --dport 443 -j DROP
#  done

sort -u known_data_ip | while read address;
do
iptables -D OUTPUT -d $address -p tcp --dport 443 -j DROP
done