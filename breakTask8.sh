#!/bin/bash
  sed -i 's/^mozilla\/GlobalSign_Root_CA.crt/#mozilla\/GlobalSign_Root_CA.crt/g' /etc/ca-certificates.conf
  rm /usr/share/ca-certificates/mozilla/GlobalSign_Root_CA.crt
  sed -i 's/^mozilla\/GTS_Root_R1.crt/#mozilla\/GTS_Root_R1.crt/g' /etc/ca-certificates.conf
  rm /usr/share/ca-certificates/mozilla/GTS_Root_R1.crt
  update-ca-certificates
  systemctl restart te-agent

