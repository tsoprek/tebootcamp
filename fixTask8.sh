#!/bin/bash
  sed -i 's/^#mozilla\/GlobalSign_Root_CA.crt/mozilla\/GlobalSign_Root_CA.crt/g' /etc/ca-certificates.conf
  cp /root/.bootcampLab/GlobalSign_Root_CA.crt /usr/share/ca-certificates/mozilla/
  sed -i 's/^#mozilla\/GTS_Root_R1.crt/mozilla\/GTS_Root_R1.crt/g' /etc/ca-certificates.conf
  cp /root/.bootcampLab/GlobalSign_Root_CA.crt /usr/share/ca-certificates/mozilla/
  cp /root/.bootcampLab/GTS_Root_R1.crt /usr/share/ca-certificates/mozilla/
  update-ca-certificates
  systemctl restart te-agent


