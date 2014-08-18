 
/*
code to begin baba
*/

#include <iostream>
#include "funcs.h"
using namespace std;

int main() {
	cout << "can you see any thing" << endl;
	cout << "this should be the next line!" << endl;
	int x = 0;
	cin >> x;
	cout << "you printed " << x << endl;
	int myarr[5] = {3,4,5,6,7};
	x = somefunc(myarr,5);
	//cout << somefunc() << endl;
	/*
	char chr = 'a';
	char *chrptr = &chr;
	cout << "ptr is " << chrptr << endl;
	cout << "*ptr is " << *chrptr << endl;
	*/
	/*
	cout << "new values are," << endl;
	for (int j=0;j<5;j=j+1) {
		cout << myarr[j] << endl;
	}
	*/
	char *strone = "3.45";
	char strtwo[] = {'3','.','5','\0'};
	//strone[3]="6";
	//*(strtwo+1)="4";
	cout << "one wala is," << strone << endl;
	cout << "two wala is," << strtwo << endl;
	return 1;
}

