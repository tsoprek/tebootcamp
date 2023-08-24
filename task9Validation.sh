#!/bin/bash
source lab_config
if grep "^server $ntp_server" /etc/ntp.conf 1>/dev/null;
then
  echo '0'
else
  echo '1'
fi