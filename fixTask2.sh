#!/bin/bash
echo 'Cleaning identity'
if sqlite3 /var/lib/te-agent/te-agent-config.sqlite 'select * from tb_agent_id' ;
  then
  echo 'Identity found'
  if systemctl status te-agent > /dev/null;
    then systemctl stop te-agent > /dev/null
    echo 'Stopping servie'
  fi
  rm -rf /var/lib/te-agent/*.sqlite
  rm -rf /tmp/*
  systemctl start te-agent > /dev/null
  echo 'Identity cleaning done, starting service.'
else
  echo 'Identity not found.'
  if ! systemctl status te-agent > /dev/null;
    then systemctl start te-agent > /dev/null
    echo 'Starting service.'
  fi
fi

