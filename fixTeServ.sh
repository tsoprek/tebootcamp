#!/bin/bash
if grep debug /etc/te-agent.cfg;
  then

  if systemctl status te-agent;
    then systemctl stop te-agent
    echo 'Service is running.'
    echo 'Stopping service'
  fi
  echo 'Fixing config file'
  sed -i 's/debug/DEBUG/g' /etc/te-agent.cfg
  echo 'Starting service'
  systemctl start te-agent
else
  echo 'Log level already DEBUG'
  grep DEBUG /etc/te-agent.cfg
fi
