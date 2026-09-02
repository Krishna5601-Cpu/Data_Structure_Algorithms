#include <vector>
#include <iostream>
using namespace std;

int findDuplicate(vector<int> &arr)
{
  int ans = 0;

  for (int i = 0; i < arr.size(); i++)
  {
    cout << "Ans: " << ans << endl;
    ans = ans ^ arr[i];
  };

  // cout << "Ans: " << ans << endl;

  for (int j = 0; j < arr.size(); j++)
  {
    // cout << "Ans: " << ans << endl;
    ans = ans ^ j;
  }
  // cout << "Ans: " << ans << endl;

  return ans;
}

int main()
{

  vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 6};
  findDuplicate(arr);

  return 0;
}