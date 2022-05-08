# January 2022 "منفذ مشبوه" Incident writeup
Данный .pcapng-файл содержит дамп TCP-траффика между сервером и локальными клиентами. Некоторые пакеты содержат попытки поговорить с сервером, но похоже, что сервер игнорировал их. Единственный диалог был между сервером и клиентом на порту `51337`. Однако, в этом диалоге лишь 2 сообщения являются читаемыми. Взглянем на них:

```
51337 -> 21019: b'H3LL0!|MTD=XOR|KEYSIZE=\x02|KEY=#\xc5'
21019 -> 51337: b'H3LL0!|MTD=XOR|KEYZISE=\x02|KEY=\xfd\n'
```

Похоже на рукопожатие, используемое для дальнейшего шифрования. MTD скорее всего означает метод шифрования, тогда шифруются здесь используя XOR. И сервер, и клиент отправляют свои ключи шифрования. После ручных или автоматических провером можно прийти к выводу, что дальнейшие сообщения поXORены с обоими ключами. PoC: [tcp_payload_extractor.py](tcp_payload_extractor.py)

Раскодированный диалог:

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

Выходит, сервер ожидает валидного рукопожатия, в результате которого происходит обмен ключами, после сервер ждет от клиента команды для выполнения. Таблица команд, составленная на основе имеющихся данных:

| CMD | ARG  | Action                |
|-----|------|-----------------------|
| UPT |      | Исполняет `uptime`       |
| LST | dir  | Исполняет `ls <dir>`     |
| CAT | file | Исполняет `cat <file>`   |
| BYE |      | Закрывает соединение |

Сервер является своего рода ботнетом. Чтобы им воспользоваться, напишем клиент, который правильно поздоровается с сервером и далее будет шифрованно общаться с ним. Мы получаем доступ к чтению файлов на сервере, среди котороых есть **flag.txt**. Пример клиента в [client.py](src/client.py).

Флаг: `li2CTF{_qu173_345Y_7r4fF1c_4N4LY515__70_pR0v3_h3_g07_h4Ck3D}`
