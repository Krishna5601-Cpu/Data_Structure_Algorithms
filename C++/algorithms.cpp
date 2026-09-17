#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  vector<int> v = {40, 10, 50, 20, 30, 20};

  // 1. Ascending sort
  sort(v.begin(), v.end());

  // 2. Print
  cout << "Ascending sort: ";
  for (int x : v)
    cout << x << " ";
  cout << endl;

  // 3. Descending sort
  sort(v.begin(), v.end(), greater<int>());

  // 4. Print
  cout << "Descending sort: ";
  for (int x : v)
    cout << x << " ";
  cout << endl;

  // 5. Reverse
  reverse(v.begin(), v.end());

  // 6. Print
  cout << "After reverse: ";
  for (int x : v)
    cout << x << " ";
  cout << endl;

  // 7. Find 20
  auto it = find(v.begin(), v.end(), 20);
  if (it != v.end())
    cout << "Found 20 at index: " << (it - v.begin()) << endl;
  else
    cout << "20 not found" << endl;

  // 8. Count 20
  cout << "Count of 20: " << count(v.begin(), v.end(), 20) << endl;

  // 9. Binary search 30 (requires sorted range)
  sort(v.begin(), v.end()); // ensure sorted for binary_search
  if (binary_search(v.begin(), v.end(), 30))
    cout << "30 found (binary search)" << endl;
  else
    cout << "30 not found (binary search)" << endl;

  return 0;
}