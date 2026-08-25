#include <iostream>
using namespace std;

bool search(int arr[], int size, int target)
{
  for (int i = 0; i < size; i++)
  {
    if (arr[i] == target)
    {
      return 1;
    }
  }

  return 0;
}

int main()
{

  int arrSize = 0;
  cout << "Enter array size: " << endl;
  cin >> arrSize;

  int numsArr[100];
  cout << "Enter array elements: " << endl;

  for (int i = 0; i < arrSize; i++)
  {
    cin >> numsArr[i];
  };

  int target;
  cout << "Enter target: ";
  cin >> target;

  bool lSearch = search(numsArr, arrSize, target);

  if (lSearch)
  {
    cout << "Target is present in array" << endl;
  }
  else
  {
    cout << "Target was not found in array" << endl;
  }

  return 0;
}