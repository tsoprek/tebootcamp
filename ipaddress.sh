#!/bin/bash

ipaddr=`dig +short registry.agt.thousandeyes.com| grep -v thousandeyes.com | sed 's/ /\n/g'`
echo $ipaddr | while read line 
  do 
  echo $line 
  done
