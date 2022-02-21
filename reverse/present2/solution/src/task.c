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
	for (unsigned int m = 0; m < sizeof(s); ++m)
	{
	    unsigned char c = s[m];
	    c = -c;
	    c += m;
	    c ^= 0x62;
	    c += 0xdd;
	    c ^= 0x2e;
	    c = -c;
	    c -= 0x83;
	    c ^= m;
	    c = ~c;
	    c = -c;
	    c = ~c;
	    c += 0x52;
	    c = ~c;
	    c = (c >> 0x2) | (c << 0x6);
	    c -= 0xf6;
	    c ^= 0x94;
	    c = (c >> 0x2) | (c << 0x6);
	    c += 0xce;
	    c = (c >> 0x6) | (c << 0x2);
	    c = -c;
	    c = (c >> 0x2) | (c << 0x6);
	    c -= m;
	    c = -c;
	    c += 0xdc;
	    c ^= m;
	    c -= 0xff;
	    c ^= m;
	    c = ~c;
	    c = (c >> 0x6) | (c << 0x2);
	    c -= m;
	    c ^= m;
	    c -= m;
	    c = (c >> 0x7) | (c << 0x1);
	    c ^= 0x44;
	    c -= 0x92;
	    c = (c >> 0x2) | (c << 0x6);
	    c -= m;
	    c = (c >> 0x6) | (c << 0x2);
	    c ^= 0xc2;
	    c = -c;
	    c += 0x78;
	    c = (c >> 0x3) | (c << 0x5);
	    c ^= 0x32;
	    c -= 0x6d;
	    c = (c >> 0x7) | (c << 0x1);
	    c += m;
	    c ^= m;
	    c = (c >> 0x5) | (c << 0x3);
	    c = -c;
	    c += 0x11;
	    c = ~c;
	    c = (c >> 0x2) | (c << 0x6);
	    c = ~c;
	    c -= 0xe1;
	    c ^= m;
	    c -= m;
	    c ^= m;
	    c -= 0x5;
	    c = ~c;
	    c -= 0xf5;
	    c ^= 0xf4;
	    c -= m;
	    c = ~c;
	    c -= 0x31;
	    c = (c >> 0x3) | (c << 0x5);
	    c -= m;
	    c = (c >> 0x5) | (c << 0x3);
	    c += 0x78;
	    c ^= 0x14;
	    c -= 0x2a;
	    c ^= 0x7d;
	    c -= m;
	    c = ~c;
	    c -= 0x15;
	    c ^= m;
	    c -= 0xce;
	    c ^= 0xb0;
	    c -= 0xec;
	    c = (c >> 0x3) | (c << 0x5);
	    c = ~c;
	    c -= m;
	    c ^= m;
	    c = ~c;
	    c = -c;
	    c += m;
	    c = (c >> 0x6) | (c << 0x2);
	    c -= m;
	    c = ~c;
	    c += 0xf6;
	    c = ~c;
	    c ^= m;
	    c = ~c;
	    c ^= m;
	    c += m;
	    c = -c;
	    c += m;
	    c = -c;
	    c ^= 0xbc;
	    c = -c;
	    c = (c >> 0x3) | (c << 0x5);
	    s[m] = c;
	}
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

