
#include <stdio.h>
#include "string.h"
#include "stdlib.h"

int main() {
	char *str = (char*) malloc(15*sizeof(char));
	strcpy(str, "hakuna matata!"); // this line should copy "hakuna matata!"
	                         // into our char array
	printf("%s\n", str);
	// Anything else?
	free(str);
	return 1;
}
