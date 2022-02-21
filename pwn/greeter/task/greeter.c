#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void secret() {
	system("/bin/sh");
}

void setup() {
	alarm(5);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

int main(){
	setup();
	struct {
		char name[32];
	} locals;
	puts("Hello there!");
	puts("What is you name?");
	fgets(locals.name, 0x32, stdin);
	printf("Greetings, %s\n", locals.name);
	return 0;
}
