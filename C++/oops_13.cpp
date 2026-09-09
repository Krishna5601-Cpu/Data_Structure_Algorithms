#include <iostream>
using namespace std;

class Printer
{
public:
  void print(int x)
  {

    cout << "Integer: " << x << endl;
  };

  void print(string text)
  {

    cout << "Text: " << text << endl;
  };

  void print(char charac, int times)
  {

    for (int i = 0; i < times; i++)
    {
      cout << charac << "";
    }
  };
};

int main()
{

  Printer p1;
  p1.print(5);
  p1.print("Krishna");
  p1.print('x', 5);

  return 0;
}