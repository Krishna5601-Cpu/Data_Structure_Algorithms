#include <iostream>
#include <vector>
using namespace std;
int main()
{

  // vector<int> v = {1, 2, 3, 4, 5};
  // v.push_back(101); // Adds element in the last
  // v.push_back(102); // Adds element in the last

  // // v.size() - Number of elements

  // for (int i = 0; i < v.size(); i++)
  // {
  //   cout << v[i] << " ";
  // }

  // v.pop_back(); // Remove the last element

  // vector<int> vect(8);

  // for (int i = 0; i < 8; i++)
  // {
  //   cin >> vect[i];
  // }

  // for (int i = 0; i < 8; i++)
  // {
  //   cout << vect[i] << " ";
  // }


  vector<int> vect;

  for (int i = 0; i < 8; i++)
  {
    int x;
    cin >> x;
    vect.push_back(x);
  }

  for (int i = 0; i < vect.size(); i++)
  {
    cout << vect[i] << " ";
  }

  
  return 0;
}