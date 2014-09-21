
#include <stdlib.h>
#include <iostream>
using namespace std;
 
// a and b point to integers.  cmp returns -1 if a is less than b, 
// 0 if they are equal, and 1 if a is greater than b.
inline int cmp (const void *a, const void *b)
{
  int aa = *(int *)a;
  int bb = *(int *)b;
  return (aa < bb) ? -1 : (aa > bb) ? 1 : 0;
}
 
// Read a list of integers from stdin
// Sort (c library qsort)
// Print the list
 
int main (int argc, char *argv[])
{
  const int size = 1000;  // array of 1000 integers
  int array [size];
  int n = 0;
  // read an integer into the n+1 th element of array
  while (cin >> array[n++]);
  cout << "done anukunta" << endl;
  n--; // it got incremented once too many times 
 
  qsort (array, n, sizeof(int), cmp);
 
  for (int i = 0; i < n; i++)
    cout << array[i] << "\n";
  return 1;
}
