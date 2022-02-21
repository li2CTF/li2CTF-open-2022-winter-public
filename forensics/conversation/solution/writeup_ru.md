# Conversation writeup
Дан дамп tcp-траффика. Рассматривая данные пакетов (Follow > TCP Stream), обнаруживаем, что это общение плейнтекстом. В диалоге есть такая строчка:

```
NRUTEQ2UIZ5TOQ2QL5RTA3TWGNZDKNBXGEYG4X3XGE3WQMCVG5PV6M2OMNZHS4BXGEYG4PZ7H5PWG4RRNZTTGIJBEF6Q====
What is that?
itz a base32 of secret. i like security.
```

Осталось раскодировать строку - раскодировать base32. Пример решения в [solve.py](solve.py).

Флаг: `li2CTF{7CP_c0nv3r54710n_w17h0U7__3Ncryp710n???_cr1ng3!!!}`