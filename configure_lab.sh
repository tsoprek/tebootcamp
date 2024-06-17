#!/bin/bash
#call lab_config source to import variables
source lab_config

#Install TE agent
curl -Os https://downloads.thousandeyes.com/agent/install_thousandeyes.sh
chmod +x install_thousandeyes.sh
sudo ./install_thousandeyes.sh -l /var/log -b k4qcugs8yvi8bmhulm9fflz4al0kt138

#Run apt update for the first time to create metadata
sudo apt update

#Install Python-pip, Flask, NTP
sudo apt install -y python3-pip ntp sqlite3 traceroute te-agent-utils snmp
sudo pip install flask flask_sqlalchemy livereload

#Replace network config file, apply config file and refresh DHCP
sudo cp 50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml

#Change of MAC address to in yaml file for match mac address
macaddr=`ip a show dev ens2 scope link | grep link`
sudo sed -i "s/52:54:00:13:85:fd/${macaddr:15:18}/g" /etc/netplan/50-cloud-init.yaml

#Change of default DNS server to configured DNS server
sudo sed -i "s/8.8.8.8/$dns_server/g" /etc/netplan/50-cloud-init.yaml

# This got outdated by adding additional DNS servers with DHCP >> Last version is permit
# only DNS server from lab_config file

#dg_raw=`ip route show default`
#dg=$(echo $dg_raw| cut -d' ' -f3)
#if ! iptables -S | grep $dg;
#  then
sudo iptables -A INPUT -s $dns_server -p udp --sport 53 -j ACCEPT
sudo iptables -A INPUT -s $dns_server -p tcp --sport 53 -j ACCEPT
#  sudo iptables -A INPUT -p udp --sport 53 -j DROP
#fi

#Apply config and refresh
sudo netplan apply
sudo dhclient

#add tetraining user/home/bash, set password, and add to wheel
sudo useradd -m -s /bin/bash tetraining
sudo chown -R tetraining:tetraining /home/tetraining
sudo chmod 700 /home/tetraining
echo -e 'Krakow123\nKrakow123\n' | sudo passwd tetraining
sudo usermod -aG sudo tetraining

#Allow tcp port 5000 in for flask
if ! iptables -S | grep 5000;
  then
  sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
fi

#Generate certificate that is required for flask
openssl req -x509 -nodes -sha256 -days 1825 -newkey rsa:2048 -keyout te-bootcamp-key.pem -out te-bootcamp.pem -subj "/CN=te-bootcamp.com"
if ! grep install_dir lab_config;
  then
    echo 'install_dir='`pwd` >>lab_config
  else
    echo "*** install_dir already set to $install_dir VALIDATE MANUALLY ***"
fi
