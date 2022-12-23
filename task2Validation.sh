#!/bin/bash

function evalID() {
sqlite3 /var/lib/te-agent/te-agent-config.sqlite 'select * from tb_agent_id'
}
retval=$(evalID)
if ! [[ $retval == '' ]] 1>/dev/null && grep k4qcugs8yvi8bmhulm9fflz4al0kt237 /etc/te-agent.cfg 1>/dev/null;
  then
  echo '1'
elif ! [[ $retval == '' ]] 1>/dev/null && ! grep k4qcugs8yvi8bmhulm9fflz4al0kt237 /etc/te-agent.cfg 1>/dev/null;
  then
  echo '2'
elif [[ $retval == '' ]] 1>/dev/null && grep k4qcugs8yvi8bmhulm9fflz4al0kt237 /etc/te-agent.cfg 1>/dev/null;
  then
  echo '2'
elif [[ $retval == '' ]] 1>/dev/null && ! grep k4qcugs8yvi8bmhulm9fflz4al0kt237 /etc/te-agent.cfg 1>/dev/null;
  then
  echo '0'
fi