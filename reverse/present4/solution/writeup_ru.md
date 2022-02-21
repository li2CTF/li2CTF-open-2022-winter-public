# Present 4 writeup
Запустив программу...

```bash
$ ./present4
Get ready...
Get ready...
Get ready...
OH MY GOOOO000000D!
7H3 __b3457 15 4W4K3N! KILL IT!
```

... Мы не увидим ничего ценного. Приступим к изучению в дизассемблере.

Функция `main()`:

```c
int main(int argc, const char **argv, const char **envp) {
	puts("Get ready...");
	sleep(1u);
	puts("Get ready...);
	sleep(1u);
	puts("Get ready...");
	sleep(1u);
	puts("OH MY GOOOO000000D!");
	return sleep(1u);
}
```

Выглядит не очень-то и интересно. Секунду, но где же строчка "7H3 \_\_b3457 15 4W4K3N!"? Давайте посмотрим, есть ли она вообще?

```bash
$ strings present4 | grep '__b3457'
$
```

Странно. Никакие функции более не вызываются, откуда же берется эта строчка? Посмотрим на происходящее в дебаггере:

```bash
gdb ./present4
gdb-peda$ br *0x4010CB
Breakpoint 1 at 0x4010cb
gdb-peda$ r
Starting program: /tmp/present4
Get ready...
Get ready...
Get ready...
OH MY GOOOO000000D!
[-------------------------------------code-------------------------------------]
   0x4010bc <main+73>:	call   0x401010 <puts@plt>
   0x4010c1 <main+78>:	mov    edi,0x1
   0x4010c6 <main+83>:	call   0x401050 <sleep@plt>
=> 0x4010cb <main+88>:	ret    
   0x4010cc <printf>:	push   rbp
   0x4010cd <printf+1>:	mov    rbp,rsp
   0x4010d0 <printf+4>:	sub    rsp,0x8
   0x4010d4 <printf+8>:	xor    edi,edi
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x00000000004010cb in main ()
gdb-peda$ n
[-------------------------------------code-------------------------------------]
   0x401056 <sleep@plt+6>:	push   0x4
   0x40105b <sleep@plt+11>:	jmp    0x401000
   0x401060 <_start>:	call   0x401073 <main>
=> 0x401065 <_start+5>:	call   0x4010cc <printf>
   0x40106a <_start+10>:	xor    eax,eax
   0x40106c <_start+12>:	xor    edi,edi
   0x40106e <_start+14>:	call   0x401040 <exit@plt>
   0x401073 <main>:	lea    rdi,[rip+0x1fc6]        # 0x403040
No argument
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

0x0000000000401065 in _start ()
gdb-peda$
```

Интересно, что инструкция `ret` возвращает нас в функцию `_start()` и уже в ней вызывается `printf()`. Посмотрим на `\_start()` в дизассемблере:

```c
void __fastcall __noreturn start(int a1, const char **a2, const char **a3) {
	main(a1, a2, a3);
	printf();
	exit(0);
}
```

И действительно, после вызова функции `main()` вызывается `printf()`. Но где же аргумент? Проверим функцию `printf()`, возможно там что-то захордкожено:

```c
__int64 printf() {
	  signed __int64 v0;
	  char *dest;
	
	  dest = (char *)mmap(0LL, 0x1F40uLL, 7, 34, -1, 0LL);
	  memcpy(dest, &mgc, 0x4A0uLL);
	  v0 = 0LL;
	  do
	  {
	    *(_DWORD *)&dest[v0] ^= 0xDEADBEEF;
	    v0 += 4LL;
	  }
	  while ( v0 < 1184 );
	  return ((__int64 (__fastcall *)(signed __int64, void *))dest)(1184LL, &mgc);
}
```

Становится интересно. За дефолтным названием скрывается самописная функция. Она выделяет область памяти, выдает ей разрешение **rwx**, копирует туда какие-то данные и расшифровывает их. После происходит прыжок на эти данные, и они выполняются.

Сбавим скорость и разъясним: В программу вшита зашифрованная программа, в момент выполения эти инструкции расшифровываются и выполняются.

Напишем скрипт, декодирующий эту функцию ([extractor.py](extractor.py))

Взглянем на расшифрованные функции (всего их 2, но формально - 3):

```c
void mgc() {
	puts("7H3 __b3457 15 4W4K3N! KILL IT!");
	__asm
	{
		syscall;
		int     1Eh;
	}
	JUMPOUT(1uLL);
}

int mgc1() {
	void *dest;

	dest = mmap(0LL, 0xFA0uLL, 7, 34, -1, 0LL);
	memcpy(dest, mgc2, 0x3C5uLL);
	dest(&byte_4034BD);
	return puts(&byte_4034BD);
}

__int64 __fastcall mgc2(__int64 a1, unsigned __int64 a2) {
	unsigned __int8 v2; // ST1B_1
	unsigned __int8 v3; // ST1B_1
	unsigned __int8 v4; // ST1B_1
	unsigned __int8 v5; // ST1B_1
	unsigned __int8 v6; // ST1B_1
	unsigned __int8 v7; // ST1B_1
	unsigned __int8 v8; // ST1B_1
	unsigned __int8 v9; // ST1B_1
	unsigned __int8 v10; // ST1B_1
	unsigned __int8 v11; // ST1B_1
	unsigned __int8 v12; // ST1B_1
	unsigned __int8 v13; // ST1B_1
	unsigned __int8 v14; // ST1B_1
	unsigned __int8 v15; // ST1B_1
	unsigned __int8 v16; // ST1B_1
	unsigned __int8 v17; // ST1B_1
	unsigned __int8 v18; // ST1B_1
	unsigned __int8 v19; // ST1B_1
	unsigned __int8 v20; // ST1B_1
	unsigned __int8 v21; // ST1B_1
	unsigned __int8 v22; // ST1B_1
	unsigned __int8 v23; // ST1B_1
	unsigned __int8 v24; // ST1B_1
	unsigned __int8 v25; // ST1B_1
	unsigned __int8 v26; // ST1B_1
	unsigned __int8 v27; // ST1B_1
	unsigned __int8 v28; // ST1B_1
	unsigned __int8 v29; // ST1B_1
	unsigned int i; // [rsp+1Ch] [rbp-4h]

	for ( i = 0; a2 > i; ++i ) {
		v2 = (*(_BYTE *)(i + a1) ^ 3) - 59;
		v3 = (((v2 >> 7) | 2 * v2) - 59) ^ 0x2B;
		v4 = ((v3 >> 5) | 8 * v3) + 100;
		v5 = ((((v4 >> 5) | 8 * v4) + 78) ^ 0x99) - 36;
		v6 = (((((v5 >> 6) | 4 * v5) ^ 0x54) + 44) ^ 0x65) + 13;
		v7 = ((v6 >> 5) | 8 * v6) + 23;
		v8 = (((((((v7 >> 3) | 32 * v7) ^ 0xED) + 40) ^ 0x43) + 6) ^ 0xB2) + 9;
		v9 = ((((v8 >> 3) | 32 * v8) - 81) ^ 0x7A) - 26;
		v10 = (((v9 >> 5) | 8 * v9) ^ 0x13) - 96;
		v11 = ((((v10 >> 3) | 32 * v10) + 57) ^ 0xE7) - 22;
		v12 = ((v11 >> 7) | 2 * v11) - 31;
		v13 = ((v12 >> 2) | (v12 << 6)) - 16;
		v14 = ((v13 >> 7) | 2 * v13) - 70;
		v15 = ((((v14 >> 1) | (v14 << 7)) ^ 0xAC) + 20) ^ 0xD5;
		v16 = ((v15 >> 7) | 2 * v15) - 102;
		v17 = ((v16 >> 6) | 4 * v16) + 61;
		v18 = ((v17 >> 6) | 4 * v17) - 105;
		v19 = (((v18 >> 7) | 2 * v18) ^ 0xF3) + 5;
		v20 = (((((((((v19 >> 6) | 4 * v19) ^ 0x76) + 51) ^ 0x5E) - 71) ^ 0xD7) - 76) ^ 0xF3) - 28;
		v21 = (((unsigned __int8)(((v20 >> 1) | (v20 << 7)) + 72) >> 6) | 4 * (((v20 >> 1) | (v20 << 7)) + 72)) - 121;
		v22 = (((((((v21 >> 3) | 32 * v21) + 14) ^ 0xF0) + 83) ^ 0x65) + 98) ^ 0x3D;
		v23 = (((((((v22 >> 7) | 2 * v22) ^ 0xCF) - 74) ^ 0x80) - 104) ^ 0x50) - 61;
		v24 = ((v23 >> 2) | (v23 << 6)) + 68;
		v25 = ((v24 >> 6) | 4 * v24) - 69;
		v26 = ((v25 >> 3) | 32 * v25) + 86;
		v27 = ((v26 >> 2) | (v26 << 6)) ^ 2;
		v28 = ((((((v27 >> 3) | 32 * v27) ^ 0xDA) + 86) ^ 0x6D) - 38) ^ 0xBC;
		v29 = (((v28 >> 6) | 4 * v28) ^ 0x6F) + 115;
		*(_BYTE *)(a1 + i) = (v29 >> 3) | 32 * v29;
	}
	return 0LL;
}
```

`mgc()` печатает строку, которую мы искали и выполняет ассемблерные инструкции.

`mgc1()` выделяет сегмент памяти, копирует туда `mgc2()`, вызывает эту функцию и выводит результат преобразований на экран.

`mgc2()` - обфусцированная функция, трансформирующая строку.

Странным является то, что `mgc()` прекращает выполнение с помощью `sys_exit` и `int`. Без них, `mgc` и `mgc1` были бы одной функцией, печатающей строку, копирующей `mgc2()` на выделенную память и исполняющей эту функцию, после печатающей результат. Выглядит логично, запатчим прерывания программы (`sys_exit`, `int 0xD1E`) `nop`ами и запустим программу снова:

```bash
$ ./present4
Get ready...
Get ready...
Get ready...
OH MY GOOOO000000D!
7H3 __b3457 15 4W4K3N! KILL IT!
[1]    9224 segmentation fault  ./present4
```

Выполнение все еще чем-то прерывается. Изучив код, можно заметить интересные строчки:

```c
xor     rbp, rbp
xor     rsp, rsp
```

Обнуление указателей стека здесь явно не к месту. За**nop**аем и их.

```bash
$ ./present4
Get ready...
Get ready...
Get ready...
OH MY GOOOO000000D!
7H3 __b3457 15 4W4K3N! KILL IT!
[1]    9353 segmentation fault  ./present4
```

На этот раз segfault из-за этих "товарищей" (разыменование нулевого указателя):

```c
xor     eax, eax
mov     rax, [rax]
```

Хорошо, давайте дальше:

```bash
$ ./present4
Get ready...
Get ready...
Get ready...
OH MY GOOOO000000D!
7H3 __b3457 15 4W4K3N! KILL IT!
[1]    9424 segmentation fault  ./present4
```

В этот раз (спойлер: последний) Segmentation Fault мы поймали благодаря:

```c
mov     eax, 1
jmp     rax
```

Затерем и это чудо враждебной техники, запустим:

```bash
$ ./present4
Get ready...
Get ready...
Get ready...
OH MY GOOOO000000D!
7H3 __b3457 15 4W4K3N! KILL IT!
li2CTF{N0_M0r3__b3457_0n_34r7H!}
```

Пример решения в [solve.py](solve.py) (сперва запустите [extractor.py](extractor.py))

Флаг: `li2CTF{N0_M0r3__b3457_0n_34r7H!}`
