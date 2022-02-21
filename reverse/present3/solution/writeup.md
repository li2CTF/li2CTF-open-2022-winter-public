# Present 3 writeup
Segmentation fault occurs during the execution.

`printFlag()` is called in `main()`, however it seems like something causes segfault before the `main()`

Debuggers say that the entrypoint isn't correct. Let's take a look at the headers with `readelf`:

```bash
$ readelf -h present3

ELF Header:
Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
Class:                             ELF64
Data:                              2's complement, little endian
Version:                           1 (current)
OS/ABI:                            UNIX - System V
ABI Version:                       0
Type:                              EXEC (Executable file)
Machine:                           Advanced Micro Devices X86-64
Version:                           0x1
Entry point address:               0xcafebabedeadbeef <--- address is kinda sus
Start of program headers:          64 (bytes into file)
Start of section headers:          15248 (bytes into file)
Flags:                             0x0
Size of this header:               64 (bytes)
Size of program headers:           56 (bytes)
Number of program headers:         11
Size of section headers:           64 (bytes)
Number of section headers:         29
Section header string table index: 28
```

**Entrypoint** is 0xcafebabedeadbeef, which is obviously not valid. Using hex editor we can change entrypoint to `main()` (0x401150) or `_start()` (0x401040) and the program will print the flag. Consider the patch example in [solve.py](solve.py)

Flag: `li2CTF{Ch4ng3_3ntry_po1nt_t0_rul3_th3_c0de!}`
