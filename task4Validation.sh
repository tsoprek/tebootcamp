#!/bin/bash
sort -u known_registry_ip | while read address;
do
    if iptables -S | grep $address 1>/dev/null;
	then
 	echo '1'
    fi
done
echo '0'