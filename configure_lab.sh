#!/bin/bash
apt install python3-pip
pip install flask
iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
iptables -F
cp 50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml
openssl req -x509 -sha256 -days 1825 -newkey rsa:2048 -keyout te-bootcamp-key.pem -out te-bootcamp.pem
