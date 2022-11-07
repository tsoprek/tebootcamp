#!/bin/bash

ipaddr=`dig +short c1.thousandeyes.com |grep -v .com`
addresses=`echo $ipaddr | sed 's/ /,/'`
iptables -A OUTPUT -d $addresses -p tcp --dport 443 -j DROP
