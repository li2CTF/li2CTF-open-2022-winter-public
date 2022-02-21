# Ritual writeup
Noting to say, to solve this challenge, we have to understand what this program does. Original source code - [task.c](src/task.c)

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

Input length has to be `8`, `input[i] == input[index + 1] - i` and the first symbols is `'b'`. 

Example of the solution is [here](solve.py)

Flag: `li2CTF{bbcehlqw}`
