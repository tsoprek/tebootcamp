#!/bin/bash
sort -u known_c1_ip | while read address;
do
	while iptables -S | grep $address;
 	do
   	  iptables -D OUTPUT -d $address -p tcp --dport 443 -j DROP
   	echo 'removed' $address
 done
done