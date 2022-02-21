# El Ephant's Tool writeup
We are given [archive](https://drive.google.com/file/d/1IBVHlHpqFqcIWWVffuEHVsWKwJqoaunA/view?usp=sharing) with **.vmem** file inside. Let's open it in **volatility**:

```bash
$ vol.py -f el_ephant.vmem imageinfo 
Volatility Foundation Volatility Framework 2.6.1
INFO     : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/tmp/el_ephant.vmem)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002bf4120L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002bf6000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2021-10-18 19:00:29 UTC+0000
     Image local date and time : 2021-10-18 22:00:29 +0300
```

It's a Windows dump, which makes our life easier. List of the processes:

```bash
$ vol.py -f el_ephant.vmem --profile=Win7SP1x64 pstree
Volatility Foundation Volatility Framework 2.6.1
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xfffffa8008bd53c0:csrss.exe                         308    300      9    601 2021-10-18 18:38:07 UTC+0000
 0xfffffa8006cffb00:wininit.exe                       356    300      3     74 2021-10-18 18:38:07 UTC+0000
. 0xfffffa8008c4ab00:services.exe                     440    356     11    208 2021-10-18 18:38:08 UTC+0000
.. 0xfffffa8008d5db00:svchost.exe                     640    440      9    278 2021-10-18 18:38:10 UTC+0000
.. 0xfffffa8008d2fb00:svchost.exe                     576    440     12    355 2021-10-18 18:38:09 UTC+0000
.. 0xfffffa8008c76060:spoolsv.exe                    1132    440     16    271 2021-10-18 18:38:15 UTC+0000
.. 0xfffffa8006ee8b00:sppsvc.exe                     1932    440      4    144 2021-10-18 18:40:22 UTC+0000
.. 0xfffffa8009042130:taskhost.exe                   3888    440      5     94 2021-10-18 18:58:25 UTC+0000
.. 0xfffffa8006e6ab00:svchost.exe                    2464    440     13    365 2021-10-18 18:40:22 UTC+0000
.. 0xfffffa80081e4b00:svchost.exe                     816    440     21    453 2021-10-18 18:38:11 UTC+0000
... 0xfffffa8008c12060:dwm.exe                       1076    816      3     87 2021-10-18 18:38:15 UTC+0000
.. 0xfffffa8008309b00:SearchIndexer.                 1320    440     14    725 2021-10-18 18:38:27 UTC+0000
... 0xfffffa8006fc3060:SearchFilterHo                 964   1320      5     82 2021-10-18 19:00:16 UTC+0000
... 0xfffffa8008e3f2d0:SearchProtocol                3412   1320      5    217 2021-10-18 19:00:00 UTC+0000
.. 0xfffffa8008d91b00:svchost.exe                     688    440     29    575 2021-10-18 18:38:10 UTC+0000
... 0xfffffa8007914890:audiodg.exe                   3916    688      7    133 2021-10-18 18:56:31 UTC+0000
.. 0xfffffa8008556b00:wmpnetwk.exe                   2120    440     12    263 2021-10-18 18:38:38 UTC+0000
.. 0xfffffa80086785c0:svchost.exe                     844    440    176    886 2021-10-18 18:38:11 UTC+0000
.. 0xfffffa8008d5a060:svchost.exe                    1360    440     10    146 2021-10-18 18:38:17 UTC+0000
.. 0xfffffa8008c78060:svchost.exe                    1240    440     27    361 2021-10-18 18:38:16 UTC+0000
.. 0xfffffa8006e6e930:mscorsvw.exe                   1888    440      6     77 2021-10-18 18:40:22 UTC+0000
.. 0xfffffa8006d695f0:svchost.exe                    1872    440      6     94 2021-10-18 18:38:22 UTC+0000
.. 0xfffffa8008f41470:svchost.exe                     872    440     22    511 2021-10-18 18:38:14 UTC+0000
.. 0xfffffa8008e709b0:svchost.exe                     876    440     50   1003 2021-10-18 18:38:11 UTC+0000
.. 0xfffffa8008392060:svchost.exe                    1832    440     26    345 2021-10-18 18:38:32 UTC+0000
.. 0xfffffa8008cb4060:taskhost.exe                   1148    440      9    301 2021-10-18 18:38:15 UTC+0000
. 0xfffffa8008c5d8e0:lsass.exe                        448    356      6    612 2021-10-18 18:38:08 UTC+0000
. 0xfffffa8008c608e0:lsm.exe                          456    356     11    144 2021-10-18 18:38:08 UTC+0000
 0xfffffa8006cf8710:System                              4      0     79    537 2021-10-18 18:38:03 UTC+0000
. 0xfffffa8007f33b00:smss.exe                         228      4      2     29 2021-10-18 18:38:03 UTC+0000
 0xfffffa8008c35060:explorer.exe                     1092   1068     28    805 2021-10-18 18:38:15 UTC+0000
. 0xfffffa80079b56c0:iexplore.exe                     272   1092     13    550 2021-10-18 18:49:16 UTC+0000
.. 0xfffffa80083f8b00:iexplore.exe                   2976    272     99   1301 2021-10-18 18:55:14 UTC+0000
. 0xfffffa8006fdc350:notepad.exe                      280   1092      1     62 2021-10-18 18:56:11 UTC+0000
. 0xfffffa8006e11060:wmpnscfg.exe                    3148   1092      1      0 2021-10-18 19:00:28 UTC+0000
 0xfffffa8008c04b00:winlogon.exe                      408    348      3    113 2021-10-18 18:38:08 UTC+0000
 0xfffffa8008377b00:csrss.exe                         368    348      9    307 2021-10-18 18:38:07 UTC+0000
```

**notepad.exe** (pid=280) and **iexplore.exe** (pid=272) seem like something to explore.

```bash
$ vol.py -f /tmp/el_ephant.vmem --profile=Win7SP1x64 procdump -p 280 -D .
Volatility Foundation Volatility Framework 2.6.1
Process(V)         ImageBase          Name                 Result
------------------ ------------------ -------------------- ------
0xfffffa8006fdc350 0x00000000ff120000 notepad.exe          Error: ImageBaseAddress at 0xff120000 is unavailable (possibly due to paging)

$ vol.py -f /tmp/el_ephant.vmem --profile=Win7SP1x64 procdump -p 272 -D .
Volatility Foundation Volatility Framework 2.6.1
Process(V)         ImageBase          Name                 Result
------------------ ------------------ -------------------- ------
0xfffffa80079b56c0 0x000000013f2b0000 iexplore.exe         Error: ImageBaseAddress at 0x13f2b0000 is unavailable (possibly due to paging)
```

Bad luck :c

May be [memdump](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference#memdump)?

```bash
$ vol.py -f /tmp/el_ephant.vmem --profile=Win7SP1x64 memdump -p 280 -D .
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing notepad.exe [   280] to 280.dmp

$ vol.py -f /tmp/el_ephant.vmem --profile=Win7SP1x64 memdump -p 272 -D .
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing iexplore.exe [   272] to 272.dmp
```

This one worked! Now we possess two process dumps. What can we find in 'em? There are several **telegram bot** references in the description. Let's give a try finding telegram handles (I mean something like "@sultanowskii"):

```bash
$ strings 280.dmp | grep -oE "@[a-zA-Z0-9 _]{3,}"
@ABCDEFGHIJKLMNOPQRSTUVWXYZ
@ABCDEFGHIJKLMNOPQRSTUVWXYZ
@0tL
@PtL
@0rL
@PrL
@PyL
@pyL
@ tL
@PhJ
@ rL
@phJ
@FLFFF
@rArBrCrDrErFrGrHrIrJq
@pApBpCpDpEpFpGpHpIpJpKpLpMpNpOpPpQpRpSpTpUpVpWpXpYpZp
@1A1B1C1D1F1E1H1G1I1J1K1L1M1N1O1
@1P1Q1R1S1T1U
@1A1B1C1D1E1F1G1H1I1J1K1L1
@OFOLOFOROXO
@PTN
@PZN
@FLFFF
@H9CP
@H9CPs
@H9CP
@H9CPsK
@H9CP
@H9CP
@A_A
...
```

Too much garbage. Adding "bot" in the end of regex (because we can only create telegram bots with "bot" in the end, according to [BotFather](https://t.me/BotFather)) helps us:

```bash
$ strings 280.dmp | grep -oE "@[a-zA-Z0-9 _]{3,}[bB][oO][tT]"
@ControllerBot
@ControllerBot is a great bot
@YTranslateBot
@iLyricsBot
@Elephant431TheCLIBot
@YTranslateBot
@GroupHelpBot
@FunctionsRobot
@Cryptowhalebot
```

After googling all the bots, we can conclude that the only not popular one is [@Elephant431TheCLIBot](https://t.me/Elephant431TheCLIBot).

Now it's time to play with this bot:

```bash
$ hello
Syntax error
hello
$ 2 + 2
4
```

Seems like some interactive mode. The most popular languages with this feature - **python**, **php**, **js**. Keep figuring out:

```bash
$ 'q' * 8
Syntax error
0
$ '1' == '1'
1
$ print("hi")
Syntax error
$ print('hi')
hi1
$ print(hi)
Syntax error
hi1
```

Aha! The `print()` function prints text even without brackets! A significant feature of php[^1]. The proof is here:

```bash
$ phpversion()
7.4.3
```

Not much work is left to do: 

```php
$ shell_exec('ls')
bot.py
flag.txt
requirements.txt
$ shell_exec('cat flag.txt')
li2CTF{El_Ephant's_p37_15_1nv1nc1bl3_70_rm_-rf!!!}
```

Flag: `li2CTF{El_Ephant's_p37_15_1nv1nc1bl3_70_rm_-rf!!!}`

[^1]: Bot's and challenge's name also refer to **php**:
<img src="https://quaded.com/data/php-logo.png"  width="400" />
