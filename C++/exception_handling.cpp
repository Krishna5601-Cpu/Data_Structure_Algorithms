#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  int a, b;
  cin >> a >> b;

  try
  {
    if (b == 0)
      throw "Division by zero!";

    cout << a / b;
  }
  catch (const char *msg)
  {
    cout << msg;
  }

  try
  {
    throw 404;
  }
  catch (int x)
  {
    cout << "Integer Error: " << x;
  }
  catch (...)
  {
    cout << "Unknown Error";
  };

  ifstream file("students.txt");

  if (!file)
  {
    cout << "File not found!";
    return 0;
  }

  return 0;
}