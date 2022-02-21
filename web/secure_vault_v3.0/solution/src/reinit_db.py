import sqlite3
import os

FLAG = "li2CTF{bruh__7h15_15_n07_s3cur3_700_:c}"

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
        ("vasya", "Zxp0-aD1bMDl", "bye :c"),
        ("admin", "Hx1m&az3!xJa5c_cRs", FLAG),
        ("alex", "1_4M_N07_4_FL4G_L0L", "1_4M_N07_4_FL4G_L0L")
    ]

    c.executemany("INSERT INTO users(username, password, data) VALUES (?,?,?)", users)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    reinit()
