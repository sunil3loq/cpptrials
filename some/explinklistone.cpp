
/*
this is my experiment of linked list
*/

#include <iostream>
#include "stdlib.h"

using namespace std;

struct node {
	float value;
	struct node* direction;
};
typedef struct node nodetype;
//basic definitions
int getlength(nodetype* A);
void insertele(nodetype** A,float B);
void getelems(nodetype* A);
void delelement(nodetype** A,int B);

int getlength(nodetype* headpinf) {
	cout << "Getting length " << endl;
	nodetype* moverinlen;
	moverinlen=headpinf;
	int retval;
	retval=0;
	while (moverinlen!=NULL) {
		retval=retval+1;
		moverinlen=moverinlen->direction;
	}
	return retval;
}
	
void insertele(nodetype** headpinf,float inele,int postoin) {
	cout << "inserting" << endl;
	nodetype* moverin;
	nodetype* temp;
	nodetype* tocreate;
	moverin=*headpinf;
	int downthis=postoin;
	temp=NULL;
	while (postoin !=0) {
		//move the position
		postoin=postoin-1;
		temp=moverin;
		moverin=moverin->direction;
	}
	tocreate = (nodetype*) malloc(sizeof(nodetype));
	tocreate->value=inele;
	tocreate->direction=moverin;
	if (downthis>0) {
		temp->direction=tocreate;
	}
	else {
		*headpinf=tocreate;
	}
}

void getelems(nodetype* headpinp) {
	cout << "Printing" << endl;
	nodetype* temp;
	temp=headpinp;
	while (temp!=NULL) {
		cout << temp->value << " ";
		temp=temp->direction;
	}
	cout << endl;
}

void delelement(nodetype** headpind, int postod) {
	int storeit=postod;
	nodetype* moverbd;
	nodetype* temp;
	moverbd=NULL;
	temp=*headpind;
	while (storeit>1) {
		moverbd=temp;
		temp=temp->direction;
		storeit=storeit-1;
	}
	if (postod>1) {
		moverbd->direction=temp->direction;
	}
	else {
		*headpind=temp->direction;
	}
	free(temp);
	cout << "Done" << endl;
}

int main() {
	cout << "This will enable you to create a linked list" << endl;	
	typedef struct node nodetype;
	//create the pointer to the head
	nodetype* headp = NULL;
	nodetype* nextp = NULL;
	/*
	//small experiment with node pointer
	struct node {
		float value;
		int * direction;
	}
	nodetype* tempp = NULL;
	cout << "without * " << tempp << " with * " << tempp << endl;
	tempp = (nodetype*) malloc(sizeof(nodetype));
	cout << "without * " << tempp << " with * " << tempp << endl;
	int myval=5;
	tempp->direction = &myval;
	tempp->value = 99;
	headp=tempp;
	cout << " head val " << headp->value << endl;
	cout << "value is " << tempp->value << "pointer is " << tempp->direction << endl;
	*/
	int cntr=1;
	float tempval;
	float nextval;
	tempval=1;
	while (tempval ==1) {
		cout << "Please enter 1 if you want to add an element--";
		cin >> tempval;
		if (tempval==1) {
			cout << "Enter the element--";
			cin >> nextval;
			if (cntr==1) {
				nextp = (nodetype*) malloc(sizeof(nodetype));
				nextp->value=nextval;
				nextp->direction=NULL;
				headp=nextp;
				cntr=cntr+1;
			}
			else {
			nextp->direction = (nodetype*) malloc(1*sizeof(nodetype));
			nextp->direction->value=nextval;
			nextp->direction->direction=NULL;
			nextp=nextp->direction;
			}
			cout << "address is " << nextp << endl;
		}
	}
	cout << "Thanks for adding the elements" << endl;
	cout << "You have added" << endl;
	nodetype* mover;
	mover = headp;
	while (mover!=NULL) {
		cout << mover->value << endl;
		mover = mover->direction;
	}
	if (headp==NULL) {
		cout << "--No elements--" << endl;
	}
	char option='b';
	int posval;
	int lenoflist;
	float inelem;
	int delpos;
	
	while (option=='a' or option=='b' or option=='c' or option=='d') {
		cout << "     What do you want to do now?" << endl;
		cout << "     a. add an element to the list" << endl;
		cout << "     b. print the list" << endl;
		cout << "     c. delete an element from the list" << endl;
		cout << "     d. Get the length" << endl;
		cout << "     any other" << endl;
		cout << "     Enter the option> ";
		cin >> option;
		if (option=='a') {
			cout << "Enter the position you want to add an element (pos starts from 0)> ";
			cin >> posval;
			lenoflist=getlength(headp);
			//lenoflist=4;
			poscheck: if (posval>lenoflist) {
				cout << "Enter value within the length> ";
				cin >> posval;
				goto poscheck;
			}
			else {
				//cout << "Functionality missing!" << endl;
				cout << "Enter the element to be inserted> ";
				cin >> inelem;
				insertele(&headp,inelem,posval);
			}
		}
		else if(option=='b') {
			getelems(headp);
		}
		else if(option=='c') {
			cout << "Enter the position you want to delete the element (pos starts from 1)> ";
			cin >> delpos;
			lenoflist=getlength(headp);
			delcheck: if (delpos>lenoflist) {
				cout << "Enter the value within length> ";
				cin >> delpos;
				goto delcheck;
			}
			else {
				delelement(&headp,delpos);
			}
		}
		else if(option=='d') {
			lenoflist=getlength(headp);
			cout << "Length is " << lenoflist << endl;
		}
		else {
			cout << "tata"<<endl;
		}
	}
}
