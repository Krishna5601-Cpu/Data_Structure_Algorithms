#include <iostream>
using namespace std;
void swapAlternate(int arr[], int size)
{
  for (int i = 0; i < size; i += 2)
  {
    if ((i + 1) < size)
    {
      swap(arr[i], arr[i + 1]);
    }
  }
}

int main()
{

  int numsArr[10];
  cout << "Enter array elements: " << endl;

  for (int i = 0; i < 10; i++)
  {
    cin >> numsArr[i];
  }

  cout << "Before swap: " << endl;

  for (int i = 0; i < 10; i++)
  {
    cout << numsArr[i] << endl;
  }

  swapAlternate(numsArr, 10);

  cout << "After swap: " << endl;

  for (int i = 0; i < 10; i++)
  {
    cout << numsArr[i] << endl;
  }

  return 0;
}