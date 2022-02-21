#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

signed int money;

void setup() {
	alarm(10);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void buy(const char* product, unsigned int cost) {
	signed int number;
	signed int total;
	FILE* f;
	char buf[1024];

	puts("How much do you wish to buy???");
	scanf("%u", &number);
	if (number > 0) {
		total = number * cost;
		if (total <= money) {
			money -= total;
			f = fopen(product, "r");
			memset(buf, 0, 1024);
			fread(buf, 1024, 1, f);
			printf("%s\n", buf);
			fclose(f);
		}
		else {
			puts("Sorry, you don't have enough money for that.");
		}
	}
	else {
		puts("Do you want to buy or not?");
	}
}

void menu() {
	puts("⚸ Welcome to the Grand Bazaar! ⚸");
	printf("Your current amount of money is: %d\n", money);
	puts("  [1] Buy new shoes (10 coins)");
	puts("  [2] Buy a new book (80 coins)");
	puts("  [3] Buy a new lamp (40 coins)");
	puts("  [4] Buy a new flag (1337 coins)");
	puts("  [5] Exit the Bazaar");
}

int main() {
	char choice;
	setup();
	money = 100;
	while (1) {
		menu();
		scanf("%d", &choice);
		switch (choice) {
			case 1: buy("shoes", 10); break;
			case 2: buy("book", 80); break;
			case 3: buy("lamp", 40); break;
			case 4: buy("flag", 1337); break;
			default: goto EXIT;
		}
	}
EXIT:
	exit(0);
	return 0;
}
