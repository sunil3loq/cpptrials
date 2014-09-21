
/*
checking more features with classes
*/

#include <iostream>
#include <stdlib.h>

using namespace std;

class pointone {
public:	
	double x, y;
	void getdesc() {
		cout << "x " << x << "y " << y << endl;
	}
};

class vectorone {
public:
	pointone start, end;
	void getdesc() {
		cout << "start is (" << start.x << "," << start.y;
		cout << ") and end is (" << end.x << "," << end.y << ")";
		cout << endl;
	}
};

int main() {
	//many experiments!
	
	//copying classes
	vectorone vecone;
	vecone.start.x=3;
	vecone.start.y=4;
	vecone.end.x=6;
	vecone.end.y=7;

	vectorone vectwo;
	vectwo.start=vecone.end;
	vectwo.end=vecone.start;

	cout << "Vector one desc is " << endl;
	vecone.getdesc();
	cout << "vector two desc is " << endl;
	vectwo.getdesc();

	//references with objects
	vectorone &vecthree=vecone;
	vecone.start.x=13;

	cout << "Vector three desc is " << endl;
	vecthree.getdesc();
}
