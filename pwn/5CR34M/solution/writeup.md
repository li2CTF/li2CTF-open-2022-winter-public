# 5CR34M writeup
We are given a binary and a libc version 2.31. There are 2 meaningful functions in executable - `main()` and `work()`. It's PIE, and there is no "win()"-like function, therefore we have to spawn shell ourselves.

First thing we can notice is a controllable format string. This vulnerability grants us an **arbitrary read** here. Second one is a buffer overflow (`gets()`). They both are in `work()`.

Let's leak a libc base firstly (there is no reason to leak a binary base here) via format string vulnerability. On a stack, return to `__libc_start_main` address is stored (it is often called  `__libc_start_main_ret`). Experimenting with the format string, we can find the right index to get it - 13. So, to leak a libc base, we simply send `%13$p`.

There are two options now. First one is a ROP chain, with manual `sys_execve` call. Second one is **one_gadget** - special libc gadget, which spawns a shell. I'll consider here both variants:

---

### 1. ROP chain

Lyrical digression

ROP chain - reliable way of shell spawning, if enough space for return address override is presented. The disadvantage is that, sometimes there is no enough space for it. 

However, in this binary, there are no constraints (`gets()`).

Now let's build a chain. Here are the helpful ROP gadgets:

```
0x0000000000026b72 : pop rdi ; ret
0x0000000000027529 : pop rsi ; ret
0x0000000000162866 : pop rdx ; pop rbx ; ret
0x000000000004a550 : pop rax ; ret
0x000000000002584d : syscall
```

And the "/bin/sh" string offset is `0x1b75aa`

Here is the plan:
1. Send "%13$p"
2. Get the `__libc_start_main_ret`, calculate the libc base
3. Build the ROP chain, adding libc base to all the addresses
4. Enjoy shell

---

### 2. one_gadget

Now to one_gadget. The signifcant advantage of this technique is that it requires minimum space. The disadvantage is that one_gadget has some constraints (most often it requires some registers to be equal to NULL). Therefore, sometimes it may be a bad luck.

In this specific case 1 of the 3 one_gadgets works. So, here is the plan:
1. Send "%13$p"
2. Get the `__libc_start_main_ret`, calculate the libc base
3. Override the return address with one_gadget
4. Enjoy shell

---

Examples are here: [solve_rop.py](solve_rop.py), [solve_og.py](solve_og.py)

P.S. Monster ASCII art is taken from https://ascii.co.uk/art/monster

Flag: `li2CTF{sCr34M1ng_15_7h3_k3y_1n_pwn,_15n'7_17???}`
