# ElectroT writeup

Lets bruteforce flask cookie secret. After some time, we will discover it - `bardzo trudny string do zlamania`.

Then, using sql injection in the 'id' field in cookie...
 
`a' or username = 'admin`

... get the admin access!

Flag: `li2CTF{4ND_n0_4l4rm5__4nd_N0_54rpr1535}`
