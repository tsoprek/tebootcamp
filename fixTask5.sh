#!/bin/bash
if grep '#mozilla/IdenTrust_Commercial_Root_CA_1.crt' /etc/ca-certificates.conf;
  then
  sed -i 's/^#mozilla\/IdenTrust_Commercial_Root_CA_1.crt/mozilla\/IdenTrust_Commercial_Root_CA_1.crt/g' /etc/ca-certificates.conf
  cp /root/.bootcampLab/IdenTrust_Commercial_Root_CA_1.crt /usr/share/ca-certificates/mozilla/
  update-ca-certificates
  systemctl restart te-agent
fi
