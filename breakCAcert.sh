#!/bin/bash
if ! grep '#mozilla/IdenTrust_Commercial_Root_CA_1.crt' /etc/ca-certificates.conf;
  then
  sed -i 's/^mozilla\/IdenTrust_Commercial_Root_CA_1.crt/#mozilla\/IdenTrust_Commercial_Root_CA_1.crt/g' /etc/ca-certificates.conf
  rm /usr/share/ca-certificates/mozilla/IdenTrust_Commercial_Root_CA_1.crt
  update-ca-certificates
  systemctl restart te-agent
fi
