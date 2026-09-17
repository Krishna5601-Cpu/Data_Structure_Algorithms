#include <iostream>
using namespace std;

template <typename T>
T swapValues(T a, T b)
{
  T c = a;
  a = b;
  b = c;

  cout << a << " " << b << endl;

}

int main()
{

  int a = 10, b = 20;
  swapValues(a, b);

  string x = "Krishna";
  string y = "Rahul";
  swapValues(x, y);

  return 0;
}