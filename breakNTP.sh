#!/bin/bash
 sed -i 's/^server 10.48.26.73/#server 10.48.26.73/g' /etc/ntp.conf
 sed -i 's/^server 10.48.26.66/#server 10.48.26.66/g' /etc/ntp.conf
systemctl restart ntp
