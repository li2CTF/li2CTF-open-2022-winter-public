# Greeter writeup
Eye-catching thing is a buffer overflow vulnerability in `main()` - we can write 18 more bytes to the memory. Our goal to achieve is a `secret()` function which spawns a shell. To jump to this function, we need to overwrite a return address on the stack. Here is a payload structure:

```py
[0-31]: Junk bytes used to fill the array
[32-39]: Junk bytes used to fill the saved rbp
[40-47]: secret()'s address (little endian)
```

Example is [here](solve.py)

Flag: `li2CTF{H3ll0_th3r3,_$username,_1_4m_y0ur_fl4g!}`
