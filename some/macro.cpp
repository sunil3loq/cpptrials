
/*
this illustrates the macro like features of the cpp
*/

#define varone hatha
#define vartwo vidhi

varone vartwo 

#define dothis(y) y is the parameter while dothis is the function

dothis(3)
dothis(4)

//#define debug

#ifdef debug
	varone
#else
	vartwo
#endif
