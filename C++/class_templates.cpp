#include <iostream>
using namespace std;

template <typename T>
class Box
{
public:
  T data;

  Box(T value)
  {
    data = value;
  }

  void show()
  {
    cout << data << endl;
  }
};

int main()
{
  Box<int> marks(95);
  Box<string> name("Krishna");
  Box<double> cgpa(9.42);

  marks.show();
  name.show();
  cgpa.show();
}