#!/bin/bash
  sed -i 's/^#mozilla\/GlobalSign_Root_CA.crt/mozilla\/GlobalSign_Root_CA.crt/g' /etc/ca-certificates.conf
  cp /root/.bootcampLab/GlobalSign_Root_CA.crt /usr/share/ca-certificates/mozilla/
  update-ca-certificates
  systemctl restart te-agent


