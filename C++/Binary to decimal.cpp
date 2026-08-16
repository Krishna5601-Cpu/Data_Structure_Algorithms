#include <iostream>
using namespace std;

int main()
{
  int binary;
  cout << "Enter the binary number: ";
  cin >> binary;

  int decimal = 0;
  int base = 1;

  while (binary > 0)
  {
    int digit = binary % 10;

    if (digit != 0 && digit != 1)
    {
      cout << "Invalid binary input!" << endl;
      return 1;
    }

    if (digit == 1)
    {
      decimal += base;
    }

    base *= 2;
    binary = binary / 10;
  }

  cout << "Decimal: " << decimal << endl;

  return 0;
}