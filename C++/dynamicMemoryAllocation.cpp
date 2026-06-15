#include <iostream>

using namespace std;

int main()
{

  int n;

  cin >> n;

  int *array = new int[n];

  for (int index = 0; index < n; index++)
  {

    cin >> array[index];
  }

  for (int index = 0; index < n; index++)
  {

    cout << array[index];
  }

  delete[] array;

  return 0;
}