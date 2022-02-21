# January 2022 "منفذ مشبوه" Incident writeup
Given .pcapng file contains TCP traffic dump between some server and local PCs. Some packets contain attempts to talk to the server, but it seems like server ingored them. The only real conversation happens between server and some client on local port `51337`. However, only two messages in this conversation are plain text. Let's take a look at 'em:

```
51337 -> 21019: b'H3LL0!|MTD=XOR|KEYSIZE=\x02|KEY=#\xc5'
21019 -> 51337: b'H3LL0!|MTD=XOR|KEYZISE=\x02|KEY=\xfd\n'
```

Well, it looks like some encryption. MTD stays for "Method" probably, therefore, method of encryption here is xor. Both server and client send their xorkey information to each other. Logically, all the following messages are XORed with these keys. Here is the PoC: [tcp_payload_extractor.py](tcp_payload_extractor.py)

Here is the decoded conversation:

```
51337 -> 21019: b'H3LL0!|MTD=XOR|KEYSIZE=\x02|KEY=#\xc5'
21019 -> 51337: b'H3LL0!|MTD=XOR|KEYZISE=\x02|KEY=\xfd\n'
51337 -> 21019: b'CMD=UPT|ARGSIZE=\x00|ARG='
21019 -> 51337: b' 15:50:46 up 135 days,  2:19,  0 users,  load average: 0.00, 0.07, 0.13\n'
51337 -> 21019: b'CMD=LST|ARGSIZE=\x01|ARG=.'
21019 -> 51337: b'flag.txt\nrequirements.txt\nrunner.sh\nserver.py\n'
51337 -> 21019: b'CMD=LST|ARGSIZE=\x01|ARG=/'
21019 -> 51337: b'bin\nboot\ndev\netc\nhome\nlib\nlib32\nlib64\nlibx32\nmedia\nmnt\nopt\nproc\nroot\nrun\nsbin\nsrv\nsys\ntask\ntmp\nusr\nvar\n'
51337 -> 21019: b'CMD=CAT|ARGSIZE=\x0b|ARG=/etc/passwd'
21019 -> 51337: b'root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\nirc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n_apt:x:100:65534::/nonexistent:/usr/sbin/nologin\n'
51337 -> 21019: b'CMD=CAT|ARGSIZE=\x0b|ARG=/etc/passwd'
21019 -> 51337: b'root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\nirc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n_apt:x:100:65534::/nonexistent:/usr/sbin/nologin\n'
51337 -> 21019: b'CMD=BYE|ARGSIZE=\x00|ARG='
```

So the server waits for handshake, both server and client give their keys. After that, server waits for commands to execute. Here is the table of commands:

| CMD | ARG  | Action                |
|-----|------|-----------------------|
| UPT |      | Executes `uptime`       |
| LST | dir  | Executes `ls <dir>`     |
| CAT | file | Executes `cat <file>`   |
| BYE |      | Closes the connection |

So the server is actually some kind of botnet. We may give a try creating our own client that'll connect to the server and grant us an access to filesystem listing and reading files. Example of a client is in [client.py](src/client.py).

Flag: `li2CTF{_qu173_345Y_7r4fF1c_4N4LY515__70_pR0v3_h3_g07_h4Ck3D}`
