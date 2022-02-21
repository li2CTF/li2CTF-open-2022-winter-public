#!/usr/bin/python3

import os
from time import sleep
import threading, _thread

book_to_order = ""
books = []
LIBDIR = "/books/"


def print_books():
    print("-------- Books --------")
    print("  " + "\n  ".join(os.listdir(LIBDIR)))
    print("-----------------------")


def update_book_to_read():
    global book_to_order
    try:
        while True:
            f = open("order.txt", "r")
            book_to_order = f.read().strip()
            f.close()
            sleep(1)
    except FileNotFoundError:
        print("order.txt is not found by librarian.")
        os._exit(-1)


def order_book():
    global book_to_order
    
    try:
        assert book_to_order in books
    except AssertionError:
        print("There is no such book.")
        return

    if "flag" in book_to_order: 
        print("That seems like f0rb1dd3n literature. It's strictly prohibited in the Library.")
    else:
        ans = input("Want to proceed? [y/n]:")
        if ans != "y":
            return
        try:
            f = open(LIBDIR + book_to_order)
        except FileNotFoundError:
            print("There is no such book.")
            return
        data = f.read()

        print("---- Book contents ----")
        print(data)
        print("-----------------------")
        f.close()

def logic():
    cmd = ""
    while cmd != "q":
        print("Command:")
        cmd = input().strip()
        if cmd == "1":
            print_books()
        elif cmd == "2":
            order_book()
        elif cmd == "q":
            break
        else:
            print("Unknown command")
            continue


def banner():
    print("⚸✤◔ Welcome to the Library ◕✤⚸")
    print("Сhoose the book you want to order and write it in order.txt, our librarian will keep your desire up-to-date (but please don't try to get forbidden literature, it's strictly prohibited).")
    print("Commands:")
    print("   1 - print list of all the books")
    print("   2 - order the book (please provide the name in the 'order.txt')")
    print("   q - quit")


def main():
    global books
    books = os.listdir(LIBDIR)
    updater = threading.Thread(target=update_book_to_read,)
    updater.start()

    banner()
    logic()
    print("توديع - فراق! أتمنى لك يوما جميلا! Goodbye! Have a nice day! (Please press Ctrl+C)")


if __name__ == "__main__":
    main()

