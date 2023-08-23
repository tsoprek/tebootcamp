#!/bin/bash
source lab_cnfig
sed -i "s/^#server $ntp_server/server $ntp_server/g" /etc/ntp.conf
systemctl restart ntp
