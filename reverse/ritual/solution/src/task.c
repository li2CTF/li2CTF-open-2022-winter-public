#include <stdio.h>
#include <string.h>

int main() {
	char input[8];
	gets(input);

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
}