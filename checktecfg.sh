#!/bin/sh
if grep k4qcugs8yvi8bmhulm9fflz4al0kt138 /etc/te-agent.cfg > /dev/null ;
  then
   echo 'Token is not changed'
fi
if grep debug /etc/te-agent.cfg > /dev/null ;
  then
   echo 'DEBUG level is incorrect'
fi
