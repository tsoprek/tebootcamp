#!/bin/bash

function eval() {
ls /usr/share/ca-certificates/mozilla | grep -i IdenTrust | while read  certificate; do openssl x509 -text -in /usr/share/ca-certificates/mozilla/$certificate; done | grep 'IdenTrust Commercial Root CA 1' | wc -l
}
reteval=$(eval)
if [ $reteval -ge 1 ] && grep '^mozilla/IdenTrust_Commercial_Root_CA_1.crt' /etc/ca-certificates.conf 1>/dev/null;
then
	echo '0'
else
	echo '1'
fi