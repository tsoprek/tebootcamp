#!/bin/bash

if grep 'auto-updates=1' /etc/te-agent.cfg 1>/dev/null && \
  grep 'deb https://apt.thousandeyes.com focal main' /etc/apt/sources.list.d/thousandeyes.list 1>/dev/null;
  then echo '0'

elif grep 'auto-updates=1' /etc/te-agent.cfg 1>/dev/null || \
  grep 'deb https://apt.thousandeyes.com focal main' /etc/apt/sources.list.d/thousandeyes.list 1>/dev/null;
  then echo '2'

else
  echo '1'
fi