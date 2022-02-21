# Conversation writeup

We are given a tcp traffic dump. Analysing packets data (Follow > TCP Stream), we can see that it's a plaintext conversation. Here is an interesting extract from it:

```
NRUTEQ2UIZ5TOQ2QL5RTA3TWGNZDKNBXGEYG4X3XGE3WQMCVG5PV6M2OMNZHS4BXGEYG4PZ7H5PWG4RRNZTTGIJBEF6Q====
What is that?
itz a base32 of secret. i like security.
```

The only thing left to do is to decode from base32. Example of the solution is in the [solve.py](solve.py).

Flag: `li2CTF{7CP_c0nv3r54710n_w17h0U7__3Ncryp710n???_cr1ng3!!!}`
