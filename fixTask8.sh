#!/bin/bash
  sed -i 's/^#mozilla\/GTS_Root_R1/mozilla\/GTS_Root_R1/g' /etc/ca-certificates.conf
  cp /root/.bootcampLab/GTS_Root_R1.crt /usr/share/ca-certificates/mozilla/
  update-ca-certificates
  systemctl restart te-agent


