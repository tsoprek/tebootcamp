#!/bin/bash
source lab_config
if ! te-agent -v | grep '1.147.0';
then
  apt remove te-agent -y
  apt install $install_dir/te-agent_1.147.0-1~focal_amd64.deb
fi

if ! grep 'auto-updates' /etc/te-agent.cfg;
        then echo 'auto-updates=0' >> /etc/te-agent.cfg
        echo 'No auto updates in cfg, adding auto-updates=0'
elif grep 'auto-updates=1' /etc/te-agent.cfg;
then
        sed -i 's/auto-updates=1/auto-updates=0/g' /etc/te-agent.cfg
        echo 'Auto-updates are set to 1, changing to 0.'
fi

echo > /etc/apt/sources.list.d/thousandeyes.list
echo 'TE repo list empty.'

if apt-key list | grep 8900;
then
  apt-key del 8900
  echo 'TE repo key removed.'
fi

apt update
if ls /etc/apt/sources.list.d/thousandeyes.list~ 1>&2 /dev/null ;
	then
	mv /etc/apt/sources.list.d/thousandeyes.list~ /etc/apt/sources.list.d/thousandeyes.list
fi
