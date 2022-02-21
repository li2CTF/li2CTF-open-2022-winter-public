import sqlite3
import os

FLAG = "li2CTF{H000000W????_M4n_1'll_b3_b4ck_1n_4_y34r_w17h_MUCH_b3773r__s3cUr1ty!}"

def reinit():
    DATABASE_NAME = "vault.db"

    os.system("rm {} && touch {}".format(DATABASE_NAME, DATABASE_NAME))
    conn = sqlite3.connect(DATABASE_NAME)

    c = conn.cursor()
    c.execute("""CREATE TABLE users
                (id INTEGER PRIMARY KEY,
                username text, 
                password text,
                data text)""")


    users =  [
        ("user", "user", "nothing_here"),
        ("dima", "qwerty123", "D.I.M.A. is that you???"),
        ("vasya", "Yn12xy$5xhaj&4n3", "bye :c"),
        ("admin", "c&azl+1xYqmNtxA#a?q", FLAG),
        ("alex", "1_4M_N07_4_FL4G_L0L", "1_4M_N07_4_FL4G_L0L")
    ]

    c.executemany("INSERT INTO users(username, password, data) VALUES (?,?,?)", users)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    reinit()
