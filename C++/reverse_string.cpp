#include <iostream>
#include <string>
using namespace std;
int main()
{

  string str;
  getline(cin, str);

  cout << "Original:\n";
  for (int i = 0; i < str.length(); i++)
  {
    cout << str[i] << " ";
  }

  cout << "\nReversed:\n";
  for (int i = str.length() - 1; i >= 0; i--)
  {
    cout << str[i] << " ";
  }

  return 0;
}