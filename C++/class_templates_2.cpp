#include <iostream>
using namespace std;
template <typename T1, typename T2>
class Pair
{
public:
  T1 first;
  T2 second;

  Pair(T1 a, T2 b)
  {
    first = a;
    second = b;
  }

  void show()
  {
    cout << first << " " << second << endl;
  }
};

int main()
{

  return 0;
}