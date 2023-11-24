#!/bin/bash
#call lab_config source to import variables
source lab_config
#Run apt update for the first time to create metadata
sudo apt update
#Install Python-pip, Flask, NTP
sudo apt install -y python3-pip
sudo pip install flask_sqlalchemy
sudo apt install -y ntp
sudo apt install sqlite3
#Install TE agent
curl -Os https://downloads.thousandeyes.com/agent/install_thousandeyes.sh
sudo chmod +x install_thousandeyes.sh
sudo ./install_thousandeyes.sh -b -l /var/log k4qcugs8yvi8bmhulm9fflz4al0kt138
#Replace network config file, apply config file and refresh DHCP
sudo cp 50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml
sudo netplan apply
sudo dhclient

#Allow tcp port 5000 in for flask and block 8.8.8.8 pushed from dhcp. We use DHCP from lab_config file
sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
sudo iptables -A OUTPUT -d 8.8.8.8 -p udp --dport 53 -j DROP
#Generate certificate that is required for flask
openssl req -x509 -sha256 -days 1825 -newkey rsa:2048 -keyout te-bootcamp-key.pem -out te-bootcamp.pem
if ! grep install_dir lab_config;
  then
    echo 'install_dir='`pwd` >>lab_config
  else
    echo '***install_dir already set to $install_dir'
fi
