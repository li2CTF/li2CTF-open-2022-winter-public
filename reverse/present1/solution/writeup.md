# Broken 1 writeup

A program doesn't print anything, `main()` is empty, no other custom functions are presented.

The only thing left to analyse here is data: text, html, encoded strings, etc.:

```bash
$ strings present1 | grep li2CTF
li2CTF{50m371m35_y0u_d0n7_3v3n_N33d_70_RUn_17!}
```

Flag: `li2CTF{50m371m35_y0u_d0n7_3v3n_N33d_70_RUn_17!}`
