#!/bin/bash
function eval() {
ls /usr/share/ca-certificates/mozilla | grep -i GlobalSign | while read  certificate;
do
  openssl x509 -text -in /usr/share/ca-certificates/mozilla/$certificate;
  done | grep 'GlobalSign' | wc -l
}
reteval=$(eval)
if [ $reteval -ge 1 ] && grep '^mozilla/GlobalSign_Root_CA.crt' /etc/ca-certificates.conf 1>/dev/null;
then
	echo '0'
else
	echo '1'
fi