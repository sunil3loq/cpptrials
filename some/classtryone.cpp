
/*
Basically trying out my hands with classes
*/

#include <iostream>
#include <stdlib.h>

using namespace std;

class point {
	double xval;
	double yval;

public:
	point(double,double);
	//~point();
	void getdesc() {
		xval=90;
		//yval=10;
		cout << "x,y are " << xval << " " << yval << endl;
	}
	
	double getx() {
		return xval;
	}
	
	double gety() {
		return yval;
	}
};

point::point(double a, double b) {
	xval=a;
	yval=b;
}

class vector {
public:
};	

int main() {
	point pone(19,11);

	//pone.xval=9;
	//pone.yval=10;
	double x, y;
	pone.getdesc();
	x=pone.getx();
	y=pone.gety();
	//x=9;
	cout << "x, y is " << x << " " << y << endl;
	return 1;
}
