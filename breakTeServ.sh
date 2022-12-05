#!/bin/bash

# A script that changed DEBUG to debug, which breakes start of te-agent service.
# Exercise is to use journal logs as te-agent.log will be empty and to learn how to manage service status

if grep DEBUG /etc/te-agent.cfg;
  then

  if systemctl status te-agent;
    then systemctl stop te-agent
    echo 'Service is running.'
    echo 'Stopping service'
  fi
  echo 'Breaking config file'
  sed -i 's/DEBUG/debug/g' /etc/te-agent.cfg
  echo 'Starting service'
  systemctl start te-agent
  sleep 2
elif grep debug /etc/te-agent.cfg;
  then
  echo 'Log level is debug, restarting service.'
  systemctl restart te-agent
else
  echo 'Log level is not DEBUG!!! Manual chek.'
fi
