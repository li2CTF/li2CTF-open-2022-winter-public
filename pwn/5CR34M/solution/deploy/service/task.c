#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void setup(void)
{
	alarm(10);
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
	setvbuf(stderr, 0, 2, 0);
};

void work() {
	char data[32];
	puts("LAST WORDS?");
	gets(data);
	printf(data);
	puts("??");
	gets(data);
	puts(data);
	puts("SOUNDS FUNNY. PREPARE TO DIE.");
}

int HELLO_THERE() {
	puts("	                                     ,--,  ,.-.");
	puts("                ,                   \\,       '-,-`,'-.' | ._");
	puts("               /|           \\    ,   |\\         }  )/  / `-,',");
	puts("               [ '          |\\  /|   | |        /  \\|  |/`  ,`");
	puts("               | |       ,.`  `,` `, | |  _,...(   (      _',");
	puts("               \\  \\  __ ,-` `  ,  , `/ |,'      Y     (   \\_L\\");
	puts("                \\  \\_\\,``,   ` , ,  /  |         )         _,/");
	puts("                 \\  '  `  ,_ _`_,-,<._.<        /         /");
	puts("                  ', `>.,`  `  `   ,., |_      |         /");
	puts("                    \\/`  `,   `   ,`  | /__,.-`    _,   `\\");
	puts("                -,-..\\  _  \\  `  /  ,  / `._) _,-\\`       \\");
	puts("                 \\_,,.) /\\    ` /  / ) (-,, ``    ,        |");
	puts("                ,` )  | \\_\\       '-`  |  `(               \\");
	puts("               /  /```(   , --, ,' \\   |`<`    ,            |");
	puts("              /  /_,--`\\   <\\  V /> ,` )<_/)  | \\      _____)");
	puts("        ,-, ,`   `   (_,\\ \\    |   /) / __/  /   `----`");
	puts("       (-, \\           ) \\ ('_.-._)/ /,`    /");
	puts("       | /  `          `/ \\ V   V, /`     /");
	puts("    ,--\\(        ,     <_/`\\     ||      /");
	puts("   (   ,``-     \\/|         \\-A.A-|     /");
	puts("  ,>,_ )_,..(    )\\          -,,_-`  _--`");
	puts(" (_ \\|`   _,/_  /  \\_            ,--`");
	puts("  \\( `   <.,../`     `-.._   _,-`");
	puts("   `                      ```");
	puts("TIME TO BE DESINTEGRATED.");
}

int main() {
	setup();
	HELLO_THERE();
	work();
	return 0;
}
