#!/bin/bash
#Script to remove IdenTrust_Commercial_Root_CA_1 certificate and simulate issue wich we would see if there is a proxy 
# and certificate is not imported. It will cause SSL error with registry.agt.thousandeyes.com.

if ! grep '#mozilla/IdenTrust_Commercial_Root_CA_1.crt' /etc/ca-certificates.conf;
  then
  sed -i 's/^mozilla\/IdenTrust_Commercial_Root_CA_1.crt/#mozilla\/IdenTrust_Commercial_Root_CA_1.crt/g' /etc/ca-certificates.conf
  rm /usr/share/ca-certificates/mozilla/IdenTrust_Commercial_Root_CA_1.crt
  update-ca-certificates 1>/dev/null
  systemctl restart te-agent 1>/dev/null
fi
