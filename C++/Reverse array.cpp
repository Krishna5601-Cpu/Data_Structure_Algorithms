#include <iostream>
using namespace std;

int reverseArray(int arr[], int arrSize)
{
  int i = 0;
  int j = arrSize - 1;

  while (i < j)
  {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    i++;
    j--;
  }

  return 0;
};

int main()
{
  int nums[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  cout << "Array before reversing: " << endl;

  for (int i = 0; i < 10; i++)
  {
    cout << nums[i] << endl;
  }

  reverseArray(nums, 10);

  cout << "Array after reversing: " << endl;

  for (int i = 0; i < 10; i++)
  {
    cout << nums[i] << endl;
  }

  return 0;
}