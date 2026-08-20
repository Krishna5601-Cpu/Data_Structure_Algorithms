#include <iostream>
#include <limits>
using namespace std;

int main()
{
  double a, b;
  cout << "Enter first number: ";
  cin >> a;

  cout << "Enter second number: ";
  cin >> b;

  char op;
  cout << "Enter the operation (+, -, *, /, %): ";
  cin >> op;

  switch (op)
  {
  case '+':
    cout << a << " + " << b << " = " << (a + b) << endl;
    break;

  case '-':
    cout << a << " - " << b << " = " << (a - b) << endl;
    break;

  case '*':
    cout << a << " * " << b << " = " << (a * b) << endl;
    break;

  case '/':
    if (b == 0)
    {
      cout << "Error: Division by zero is not allowed!" << endl;
    }
    else
    {
      cout << a << " / " << b << " = " << (a / b) << endl;
    }
    break;

  case '%':
  
    if (b == 0)
    {
      cout << "Error: Modulus by zero is not allowed!" << endl;
    }
    else
    {
      cout << static_cast<int>(a) << " % " << static_cast<int>(b)
           << " = " << (static_cast<int>(a) % static_cast<int>(b)) << endl;
    }
    break;

  default:
    cout << "Invalid Input! Please use +, -, *, /, or %" << endl;
    break;
  }

  return 0;
}