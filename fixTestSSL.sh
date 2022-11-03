#!/bin/bash
if grep '#mozilla/GTS_Root_R1.crt' /etc/ca-certificates.conf;
  then
  sed -i 's/^#mozilla\/GTS_Root_R1/mozilla\/GTS_Root_R1/g' /etc/ca-certificates.conf
  cp /root/.bootcampLab/GTS_Root_R1.crt /usr/share/ca-certificates/mozilla/
  update-ca-certificates
  systemctl restart te-agent
fi
if grep '#mozilla/GlobalSign_Root_CA.crt' /etc/ca-certificates.conf;
then
  sed -i 's/^#mozilla\/GlobalSign_Root_CA.crt/mozilla\/GlobalSign_Root_CA.crt' /etc/ca-certificates.conf
  cp /root/.bootcampLab/GlobalSign_Root_CA.crt /usr/share/ca-certificates/mozilla/
  update-ca-certificates
  systemctl restart te-agent
fi
