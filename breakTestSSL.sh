#!/bin/bash
if ! grep '#mozilla/GTS_Root_R1.crt' /etc/ca-certificates.conf;
  then
  sed -i 's/^mozilla\/GTS_Root_R1.crt/#mozilla\/GTS_Root_R1.crt/g' /etc/ca-certificates.conf
  rm /usr/share/ca-certificates/mozilla/GTS_Root_R1.crt
  update-ca-certificates
  systemctl restart te-agent
fi
if ! grep '#mozilla/GlobalSign_Root_CA.crt' /etc/ca-certificates.conf;
then
  sed -i 's/^mozilla\/GlobalSign_Root_CA.crt/#mozilla\/GlobalSign_Root_CA.crt' /etc/ca-certificates.conf
  rm /usr/share/ca-certificates/mozilla/GlobalSign_Root_CA.crt
  update-ca-certificates
  systemctl restart te-agent
fi
