#!/bin/bash
sudo apt update
sudo apt install -y python3-pip
sudo pip install flask_sqlalchemy
sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
sudo iptables -F
sudo cp 50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml
openssl req -x509 -sha256 -days 1825 -newkey rsa:2048 -keyout te-bootcamp-key.pem -out te-bootcamp.pem
