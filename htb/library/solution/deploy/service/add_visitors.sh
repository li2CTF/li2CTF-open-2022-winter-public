#!/bin/bash

let i=1
echo "[*] Creating visitors..."
while IFS= read -r line || [[ -n "$line" ]]; do
	user=($(echo $line | tr ":" "\n"))
	currPasswd=${user[1]}
	echo "${user[0]}:${user[1]}"
	currID=$((1400 + ${i}))
	useradd -rm -d "/lobbies/lobby${i}/" -s /bin/bash -u $currID "${user[0]}"
	echo "${user[0]}:${user[1]}" | chpasswd
	echo "example.txt" > "/lobbies/lobby${i}/order.txt"
	chown "root":"root" "/lobbies/lobby${i}/"
	chown "${user[0]}":"${user[0]}" "/lobbies/lobby${i}/order.txt"
	chmod go-rwx "/lobbies/lobby${i}/order.txt"
	i=$(($i+1))
done < "/visitors.txt"

