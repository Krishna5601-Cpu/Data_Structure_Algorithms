#include <iostream>
using namespace std;
int main()
{
  for (int i = 1; i <= 10; i++)
  {
    cout << i << " ";
  }

  cout << "\n";

  for (int i = 10; i >= 1; i--)
  {
    cout << i << " ";
  }

  cout << "\n";

  int n;
  cin >> n;
  for (int i = 1; i <= 10; i++)
  {
    cout << (n * i) << endl;
  }

  cout << "\n";

  int num, fact = 1;
  cin >> num;

  for (int i = 1; i <= num; i++)
  {
    fact = fact * i;
  }

  cout << "factorial: " << fact;

  return 0;
}