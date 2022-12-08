#!/bin/bash

if ! grep 'auto-updates' /etc/te-agent.cfg;
        then echo 'auto-updates=0' > /etc/te-agent.cfg
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

if ls /etc/apt/trusted.gpg~;
        then
        mv /etc/apt/trusted.gpg~ /etc/apt/trusted.gpg
fi

echo 'deb https://apt.thousandeyes.com focal main' > /etc/apt/sources.list.d/thousandeyes.list
echo 'TE repo list added'

if ! gpg --show-keys /etc/apt/trusted.gpg | grep 'AA5FBA03CE4EF309B7E3D4E1C99A15F5BE718900';
then
	apt-key add /etc/apt/trusted.gpg.d/thousandeyes-apt-key.pub.gpg
	echo 'GPG key added!'
fi
if ls /etc/apt/sources.list.d/thousandeyes.list~;
        then
        mv /etc/apt/sources.list.d/thousandeyes.list~ /etc/apt/sources.list.d/thousandeyes.list
fi

if ls /etc/apt/trusted.gpg~;
        then
        mv /etc/apt/trusted.gpg~ /etc/apt/trusted.gpg
fi