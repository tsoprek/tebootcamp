#!/bin/bash
source lab_config
sed -i 's/^#mozilla\/GlobalSign_Root_CA.crt/mozilla\/GlobalSign_Root_CA.crt/g' /etc/ca-certificates.conf
cp $install_dir/GlobalSign_Root_CA.crt /usr/share/ca-certificates/mozilla/
sed -i 's/^#mozilla\/GTS_Root_R1.crt/mozilla\/GTS_Root_R1.crt/g' /etc/ca-certificates.conf
cp $install_dir/GlobalSign_Root_CA.crt /usr/share/ca-certificates/mozilla/
cp $install_dir/GTS_Root_R1.crt /usr/share/ca-certificates/mozilla/
update-ca-certificates
systemctl restart te-agent > /dev/null


