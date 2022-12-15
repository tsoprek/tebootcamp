#!/bin/bash

function eval() {
sort -u known_data_ip | while read address;
do
    if iptables -S | grep $address 1>/dev/null;
	then
 	retval='1'
	echo $retval
     break 2
    fi
done
}
retval=$(eval)
if [ "$retval" == "1" ] ; then
	echo $retval
else
	echo '0'
fi