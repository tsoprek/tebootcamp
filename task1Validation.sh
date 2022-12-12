#!/bin/sh

if grep DEBUG /etc/te-agent.cfg 1>/dev/null && systemctl status te-agent 1>/dev/null; then
#	echo 'LOG-Level=DEBUG and service is running'
	echo '0'
elif grep DEBUG /etc/te-agent.cfg 1>/dev/null &&  ! systemctl status te-agent 1>/dev/null; then
#	echo 'LOG-Level=DEBUG, but service is not running'
	echo '2'
elif grep debug /etc/te-agent.cfg 1>/dev/null && ! systemctl status te-agent 1>/dev/null; then
#	echo 'LOG-Level=debug and service is not running'
	echo '1'
fi