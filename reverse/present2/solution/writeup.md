# Present 2 writeup

This program prints something, waits one second and then deletes itself from PC.

```bash
$ ./present2
Hi! Lets check if math still works in our world or not

Checking world rules...
Nah, physics and maths don't work, we don't even exist. Bye-bye!
```

To static analysis. There are `main()`, `yes()`, `no()` functions inside. It is checked in the first function that the length of the first argument (filename) is equal to -123. This condition always returns `false` (I hope it's obvious why), that's why `no()` is always called.

Function `yes()` calls an obfuscated `exist()` function. We can patch the program to reverse the comparison. In other words, I want to turn this:

```C
if (strlen(argv[0]) == -123) {
    f_ptr = yes;
}
else {
    f_ptr = no;
}
```

into this:

```C
if (strlen(argv[0]) != -123) {
    f_ptr = yes;
}
else {
    f_ptr = no;
}
```

So, we have to change `jnz` (the address is 0x40174D, opcode=`0x75`) to `jz` with opcode=`0x74` (using any hex editor). After patch, the program prints the flag. Check out [solve.py](solve.py) to see the patch!

Flag: `li2CTF{d1d_y0u_r34lly_Ch4nG3D_7h3_w0rLd???}`
