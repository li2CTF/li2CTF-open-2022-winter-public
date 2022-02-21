# Laba Altakhmine writeup
Not too much to say. That seems like a `base64`-encoded string. After decoding it looks like:

```
6g 69 32 43 54 46 7f 41 31 4j 5j 6f 31 30 5j 54 34 6h 5j 65 54 30 5j 4g 34 62 41 5j 62 41 5j 31 7e 5j 50 34 34 5j 69 4i 24 54 21 74 55 74 34 54 41 7h
```

And that seems like hex values that are.. shifted? We can bruteforce Caesar cipher shift using something like [this](solve.py), and convert the result to the string, which is a flag.

Basically:
```
from base64 -> Caesar -4 -> from hex
```

Flag: `li2CTF{A1O_k10_T4m_eT0_L4bA_bA_1z_P44_iN$T!tUt4TA}`
