#!/bin/bash

if ! te-agent -v | grep '1.147.0';
then
  apt remove te-agent -y
  apt install /root/.bootcampLab/te-agent_1.147.0-1~focal_amd64.deb
fi

curl -Os https://downloads.thousandeyes.com/agent/install_thousandeyes.sh
chmod +x install_thousandeyes.sh
sudo ./install_thousandeyes.sh -b vv6zzhgrdurk880nw5yf8wzkwp9zfjt5
