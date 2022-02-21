# gitshit writeup
We are given a git repository with the **flag.txt**, buf the flag is wrong. Accroding to `git log`, there are 100 commits. Description provides us a regex for the correct flag:

```regex
li2CTF{[a-f0-9]{32}}
```

Not to die while solving this challenge, we can write a simple script which checkouts all the commits and finds a correct flag. The example is [here](solve.py)

Flag: `li2CTF{eb4be8ca3fdeaf33b37f7a6f27b02494}`
