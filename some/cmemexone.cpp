#include <stdio.h>

void square(int *num) {
	*num = *num * *num;
}

int main() {
	int x = 4;
	int *xptr;
	xptr = &x;
	square(xptr);
	printf("%d\n", x);
	return 0;
}

