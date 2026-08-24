#include <iostream>
using namespace std;

int getMax(int arr[], int n)
{

  int max = INT_MIN;
  for (int i = 0; i < n; i++)
  {

    if (arr[i] >= max)
    {
      max = arr[i];
    }
  }

  return max;
}
int getMin(int arr[], int n)
{

  int min = INT_MAX;
  for (int i = 0; i < n; i++)
  {

    if (arr[i] <= min)
    {
      min = arr[i];
    }
  }

  return min;
}

int main()
{

  int size;
  cout << "Enter the array size: " << endl;
  cin >> size;

  int num[100];

  cout << "Enter array elements: " << endl;

  // Taking input in array
  for (int i = 0; i < size; i++)
  {
    cin >> num[i];
  };

  int maximum = getMax(num, size);
  int minimum = getMin(num, size);
  cout << "Max: " << maximum << " " << "Min" << minimum << endl;

  return 0;
}