#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char tmp[4096];
unsigned char s[] = {
    0x92, 0x6d, 0x11, 0x93, 0xaa, 0x90, 0xbf, 0xa3, 
    0x5a, 0x3a, 0x60, 0xc, 0xbd, 0xce, 0x91, 0x28, 
    0x40, 0xe1, 0x2, 0x5f, 0x14, 0xbb, 0x80, 0xdc, 
    0xf3, 0x67, 0xb9, 0xeb, 0xd6, 0x5f, 0x1b, 0x59, 
    0x5a, 0x64, 0xc, 0x8e, 0xe2, 0x5c, 0x66, 0x7, 
    0xb9, 0x6e, 0x12, 0xf4
};

int exist() {
	/*
		Awesome stuff happens here with 's' array
		But that's reverse challenge, so go read code and think what to do!

		Consider this function as the `win()` function that gives you a flag.
	*/
	printf("%s", s);
	return 0;
}


int yes(char* self) {
	puts("Yeah the world is real!");
	exist();
	puts("");
	return 0;
}


int no(char* self) {
	puts("Nah, physics and maths don't work, we can't even exist. Bye-bye!");
	snprintf(tmp + 3, 4000, "%s", self); 
	system(tmp);
	return 0;
}

int main(int argc, char** argv) {
	strcpy(tmp, "rm ");
	puts("Hi! Lets check if math still works in our world or not\n");
	puts("Checking world rules...");
	sleep(1);
	int (*f_ptr)(char *);
	if (strlen(argv[0]) == -123) {
		f_ptr = yes;
	}
	else {
		f_ptr = no;
	}
	f_ptr(argv[0]);
	return 0;
}

