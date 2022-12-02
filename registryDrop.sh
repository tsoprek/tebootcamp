#!/bin/bash
#
#ipaddr=`dig +short registry.agt.thousandeyes.com |grep -v thousandeyes.com`
#addresses=`echo $ipaddr | sed 's/ /,/'`
#iptables -A OUTPUT -d $addresses -p tcp --dport 443 -j DROP
### IP ADDRESSES OF THE registry.agt.thousandeyes.com change from time to time.
# When this change is done while TSing or machine was powered off and address is changed,
# above script will fail to remove ip as it is not in table. Hence new script that will store ip addresses
dig +short registry.agt.thousandeyes.com |grep -v thousandeyes.com >> known_registry_ip
sort -u known_registry_ip | while read address;
do
iptables -A OUTPUT -d $addresses -p tcp --dport 443 -j DROP
done