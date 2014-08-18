
#include <stdio.h>
#include <iostream>
int main(int argc, char ** argv){
    /*
    for (int i = 1; i < argc; i++) {
        printf("%s\n", argv[i]);
    }
    */
	int i = 0;
	begin: i = i+1;
	std::cout << argv[i] << " ";
	if (i<=argc) goto begin;
	else std::cout << std::endl;
    return 0;
}
