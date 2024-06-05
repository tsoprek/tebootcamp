#!/bin/bash
source lab_config
sed -i "s/^#server $ntp_server/server $ntp_server/g" /etc/ntp.conf
systemctl restart ntp > /dev/null
