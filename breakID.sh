#!/bin/bash
if grep k4qcugs8yvi8bmhulm9fflz4al0kt138 /etc/te-agent.cfg;
  then
  echo 'Acccout token already set to Tihomir - AG'
else
  if systemctl status te-agent;
    then systemctl stop te-agent
    echo 'Service is running.'
    echo 'Stopping service'
  fi
  echo 'Breaking config file'
  sed -i 's/account-token=.*/account-token=k4qcugs8yvi8bmhulm9fflz4al0kt138/g' /etc/te-agent.cfg
  echo 'Starting service'
  systemctl start te-agent
fi
