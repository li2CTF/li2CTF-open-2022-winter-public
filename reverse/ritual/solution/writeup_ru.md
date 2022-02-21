# Ritual writeup
Особо нечего сказать, нужно читать код и разибираться, что он делает. Оригинал алгоритма можно увидеть здесь - [foundations.c](src/foundations.c):

```c
...
int input_length = strlen(input);
if (input_length != 8) {
	goto NO;
}

for (int index = 0; index < input_length - 1; index++) {
	if (input[index] != input[index + 1] - index) {
		goto NO;
	}
}

if (input[0] != 'b') {
	goto NO;
}

goto YES;

NO:
	puts("NO!\n");
	return 1;

YES:
	puts("YES\n");
	return 0;
...
```

Длина строки должна быть равна `8`, `input[i] == input[index + 1] - i` и первый символ строки -  `'b'`. После можно легко написать скрипт, который по заданным условиям сгенерит нам правильную строку (пример в [solve.py](solve.py))

Флаг: `li2CTF{bbcehlqw}`
