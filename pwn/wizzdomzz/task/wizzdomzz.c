#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void setup() {
	alarm(10);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

char quotes[20 * 120];
int _shitty_array[120];
char flag[120];

void init_quotes() {
	strcpy(&quotes[0 * 120], "Love For All, Hatred For None. – Khalifatul Masih III");
	strcpy(&quotes[1 * 120], "Change the world by being yourself. – Amy Poehler");
	strcpy(&quotes[2 * 120], "Every moment is a fresh beginning. – T.S Eliot");
	strcpy(&quotes[3 * 120], "Never regret anything that made you smile. – Mark Twain");
	strcpy(&quotes[4 * 120], "Die with memories, not dreams. – Unknown ");
	strcpy(&quotes[5 * 120], "Aspire to inspire before we expire. – Unknown ");
	strcpy(&quotes[6 * 120], "Everything you can imagine is real. – Pablo Picasso");
	strcpy(&quotes[7 * 120], "Simplicity is the ultimate sophistication. – Leonardo da Vinci");
	strcpy(&quotes[8 * 120], "Whatever you do, do it well. – Walt Disney");
	strcpy(&quotes[9 * 120], "What we think, we become. – Buddha");
	strcpy(&quotes[10 * 120], "All limitations are self-imposed. – Oliver Wendell Holmes");
	strcpy(&quotes[11 * 120], "Tough times never last but tough people do. – Robert H. Schiuller");
	strcpy(&quotes[12 * 120], "Problems are not stop signs, they are guidelines. – Robert H. Schiuller");
	strcpy(&quotes[13 * 120], "One day the people that don’t even believe in you will tell everyone how they met you. – Johnny Depp");
	strcpy(&quotes[14 * 120], "If I’m gonna tell a real story, I’m gonna start with my name. – Kendrick Lamar");
	strcpy(&quotes[15 * 120], "If you tell the truth you don’t have to remember anything. – Mark Twain");
	strcpy(&quotes[16 * 120], "Have enough courage to start and enough heart to finish. – Jessica N. S. Yourko");
	strcpy(&quotes[17 * 120], "Hate comes from intimidation, love comes from appreciation. – Tyga");
	strcpy(&quotes[18 * 120], "I could agree with you but then we’d both be wrong. – Harvey Specter");
	strcpy(&quotes[19 * 120], "Oh, the things you can find, if you don’t stay behind. – Dr. Seuss");
}

void init_flag() {
	FILE* fl = fopen("flag.txt", "r");
	char ch;
	int ind = 0;

	if (fl == NULL) {
		printf("Error: couldn't open flag.txt");
		exit(1);
	}

	fscanf(fl, "%120c", flag);

	fclose(fl);
}

void __init_w() {
	init_flag();
	init_quotes();
}

void printMenu() {
	puts("Commands:");
	puts("  w: Read wisdom");
	puts("  q: Quit");
	printf("> ");
	fflush(stdout);
}

void getWisdom() {
	int id = 0;
	char* ptr;
	puts("Enter wisdom id (1-20):");
	fflush(stdout);
	scanf("%d", &id);
	getchar();
	id = (id - 1) * 120;
	printf("Here is your wisdom: %s\n", (quotes + id));
	fflush(stdout);
}

int main() {
	setup();
	char cmd = '_';
	__init_w();
	printf("Wizzdomzz service: free wisdoms for everyone!\n");
	fflush(stdout);

	while (cmd != 'q') {
		printMenu();
		scanf("%c", &cmd);
		getchar();
		if (cmd == 'w') {
			getWisdom();
		}
		else {
			goto END;
		}
	}
END:
	printf("Hope you became smarter!\n");
	fflush(stdout);
}
