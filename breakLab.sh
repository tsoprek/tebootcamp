./registryDrop.sh
./c1Drop.sh
./dataDrop.sh
./breakID.sh
sleep 2
./breakTeServ.sh
./breakCAcert.sh
./breakTestSSL.sh
./breakRepo.sh
sleep 10
./breakNTP.sh
./breakDNS.sh
> /var/log/te-agent.log

