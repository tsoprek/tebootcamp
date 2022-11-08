#!/bin/bash

# Script that check if account group token is set to invalid token
# This will generate authentication failure logs and token and identity has to be reset
# Identity should exist but agent is not in portal 

if grep k4qcugs8yvi8bmhulm9fflz4al0kt237 /etc/te-agent.cfg;
  then
  echo 'Acccout token already set to invalid group.'
else
  if systemctl status te-agent;
    then systemctl stop te-agent
    echo 'Service is running.'
    echo 'Stopping service'
  fi
  echo 'Breaking config file'
  sed -i 's/account-token=.*/account-token=k4qcugs8yvi8bmhulm9fflz4al0kt237/g' /etc/te-agent.cfg
  echo 'Starting service'
  systemctl start te-agent
fi
