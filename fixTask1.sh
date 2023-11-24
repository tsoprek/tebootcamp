#!/bin/bash
if grep debug /etc/te-agent.cfg;
  then
  if systemctl status te-agent > /dev/null;
    then systemctl stop te-agent > /dev/null
    echo 'Service is running.'
    echo 'Stopping service'
    sleep 2
  fi
  echo 'Fixing config file'
  sed -i 's/debug/DEBUG/g' /etc/te-agent.cfg
  echo 'Starting service'
  systemctl start te-agent > /dev/null
else
  echo 'Log level already DEBUG'
  grep DEBUG /etc/te-agent.cfg
fi
