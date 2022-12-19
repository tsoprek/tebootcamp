#!/bin/bash

if grep '^server 10.48.26.73' /etc/ntp.conf 1>/dev/null || grep '^server 10.48.26.66' /etc/ntp.conf 1>/dev/null;
then
  echo '0'
else
  echo '1'
fi