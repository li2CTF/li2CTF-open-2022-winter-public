# ElectroT writeup

Переберем secret у flask cookie. Им окажется `bardzo trudny string do zlamania`.

Воспользуемся sql injection в поле id внутри cookie...
 
`a' or username = 'admin`

... и успешно зайдем от имени админа!

Флаг: `li2CTF{4ND_n0_4l4rm5__4nd_N0_54rpr1535}`
