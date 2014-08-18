
/*
this calculates the first 100 triangular numbers
*/

#include <iostream>
using namespace std;

int main(void){
	//takes in the number of triangular numbers to calculate
	int a;
	cout << "Print the number of numbers you req" << endl;
	cin >> a;
	for (int i=0;i<a;++i) {
		cout << i*(i+1)/(3-1) << " ";
	}
	cout << endl;
	return 1;
}
