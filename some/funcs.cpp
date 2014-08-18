
#include <iostream>
using namespace std;

int somefunc(int arr[],int length){	
	//cout<< "returning integer" << 5 << endl;
	int x = 5;
	//float y = 5.5;
	for (int i=0;i<length;i=i+1) {
		arr[i] = arr[i]+1;
	}
	return x;
}
