#!/bin/bash

if ! grep 'auto-updates' /etc/te-agent.cfg;
        then echo 'auto-updates=0' >> /etc/te-agent.cfg
        echo 'No auto updates in cfg, adding auto-updates=0'
elif grep 'auto-updates=0' /etc/te-agent.cfg;
	then
        sed -i 's/auto-updates=0/auto-updates=1/g' /etc/te-agent.cfg
        echo 'Auto-updates are set to 0, changing to 1.'
else
	echo 'Value is already set to 0'
fi

if ls /etc/apt/sources.list.d/thousandeyes.list~;
        then
        mv /etc/apt/sources.list.d/thousandeyes.list~ /etc/apt/sources.list.d/thousandeyes.list
fi

echo 'deb https://apt.thousandeyes.com focal main' > /etc/apt/sources.list.d/thousandeyes.list
echo 'TE repo list added'

if ! apt-key list | grep 8900;
then
  sudo wget -q https://apt.thousandeyes.com/thousandeyes-apt-key.pub -O- | sudo apt-key add -
  echo 'TE repo key added.'
fi

if ls /etc/apt/sources.list.d/thousandeyes.list~;
        then
        mv /etc/apt/sources.list.d/thousandeyes.list~ /etc/apt/sources.list.d/thousandeyes.list
fi