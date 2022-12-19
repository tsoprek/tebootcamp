#!/bin/bash

if ! grep 'auto-updates' /etc/te-agent.cfg;
        then echo 'auto-updates=0' >> /etc/te-agent.cfg
        echo 'No auto updates in cfg, adding auto-updates=0'
elif grep 'auto-updates=1' /etc/te-agent.cfg;
then
        sed -i 's/auto-updates=1/auto-updates=0/g' /etc/te-agent.cfg
        echo 'Auto-updates are set to 1, changing to 0.'
fi

echo > /etc/apt/sources.list.d/thousandeyes.list
echo 'TE repo list empty'
if ls /etc/apt/sources.list.d/thousandeyes.list~;
	then
	mv /etc/apt/sources.list.d/thousandeyes.list~ /etc/apt/sources.list.d/thousandeyes.list
fi
if ls /etc/apt/trusted.gpg~;
	then
	mv /etc/apt/trusted.gpg~ /etc/apt/trusted.gpg
fi
if gpg --show-keys /etc/apt/trusted.gpg | grep 'AA5FBA03CE4EF309B7E3D4E1C99A15F5BE7';
	then
	apt-key del AA5FBA03CE4EF309B7E3D4E1C99A15F5BE718900
	echo 'GPG key removed!'
fi