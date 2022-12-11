#!/bin/sh

if grep DEBUG /etc/te-agent.cfg && systemctl status te-agent ; then
	echo 'LOG-Level=DEBUG and service is running'
	return 0
elif grep DEBUG /etc/te-agent.cfg &&  ! systemctl status te-agent ; then
	echo 'LOG-Level=DEBUG, but service is not running'
	return 2
elif grep debug /etc/te-agent.cfg && ! systemctl status te-agent ; then
	echo 'LOG-Level=debug and service is not running'
	return 1
fi