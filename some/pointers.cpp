
/*
some experiments with pointers
*/

#include <iostream>
using namespace std;
#include "string.h"
#include "stdlib.h"

int main(int argc,char* argv[]) {
	/*
	//checking the arguements given
	cout << "Number of arguements given is," << endl;
	cout << argc-1 << endl;
	cout << "The arguements are " << endl;
	for (int i=1;i<argc;++i) {
		cout << argv[i]<<endl;
	}
	*/
	/*
	//basic pointers
	int *x;
	int xnum=10;
	x=&xnum;
	cout << *x << endl;

	//basic references
	int &y=xnum;
	y=y+1;
	cout << "after incrementing y " << *x << endl;
	*/
	/*
	//playing around with strings
	char* astrptr;
	char* bstrptr;
	char astr = 'p';
	char bstr[] = "aname";
	bstrptr = bstr;
	astrptr = &astr;
	cout << "pname, " << *astrptr << endl;
	cout << "aname, " << bstr << endl;
	cout << "aname smaller is, " << *(bstrptr) << endl;
	char** xy;
	char **zx;
	char ** zz;
	xy = &astrptr;
	zx = xy;//&&bstr;
	zz = &bstrptr;
	cout << **xy << " " << **zx << " " << **zz << endl;
	cout << "now starts" << endl;
	while (**zz != '\0') {
		cout << **zz << endl;
		*zz = *zz+1;
	}
	*/
	/*
	//arrays and pointers
	int normarr[5] = {5,6,7,8,9};
	int *pptr;
	pptr = normarr;
	cout << "third el in normarr " << normarr[1+1] << endl;
	cout << "third through pointer " << *(pptr+1+1) << endl;
	cout << "another array " << *(normarr+1+1) << endl;
	cout << "pointer with arra " << pptr[1+1] << endl;
	*/
	
	//exploring dynamic allocation
	char* dynptrone = (char*) malloc(5*sizeof(char));
	strcpy(dynptrone,"four");
	cout << "allocated for " << dynptrone << endl;
	int* dynptrtwo = (int*) malloc(sizeof(int));
	*dynptrtwo = 5;
	cout << "alloca " << *dynptrtwo << endl;
	int dynptrthree[3] = {4,5,6};
	cout << "int array is " << *dynptrthree << endl;
	return 1;
}
