#!/bin/bash
function eval() {
ls /usr/share/ca-certificates/mozilla | grep -i gts | while read  certificate;
do
  openssl x509 -text -in /usr/share/ca-certificates/mozilla/$certificate;
  done | grep 'GTS Root R1' | wc -l
}
reteval=$(eval)
if [ $reteval -ge 1 ] && grep '^mozilla/GTS_Root_R1' /etc/ca-certificates.conf 1>/dev/null;
then
	echo '0'
else
	echo '1'
fi