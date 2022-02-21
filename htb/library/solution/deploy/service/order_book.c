#include <unistd.h>
#include <stdlib.h>

int main() {
	setuid(0);
	system("/usr/local/share/order_book.py");
}

