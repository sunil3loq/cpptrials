
// vector::begin/end
#include <iostream>
#include <vector>

int main ()
{
  std::vector<int> myvector;
  for (int i=1; i<=32; i++) {
	std::cout << "index is " << i << std::endl;
	std::cout << "size is " << myvector.size() << std::endl;
	std::cout << "capacity is " << myvector.capacity() << std::endl;
	myvector.push_back(i);
}
  std::cout << "myvector contains:";
  for (std::vector<int>::iterator it = myvector.begin() ; it != myvector.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';

  return 0;
}
