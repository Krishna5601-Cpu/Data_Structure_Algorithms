// #include <iostream>
// #include <map>
// #include <vector>

// using namespace std;
// int main()
// {
//   vector<int> input;

//   map<string, int> freq;

//   freq["1"] = 0;
//   freq["2"] = 0;
//   freq["3"] = 0;

//   cout << "Enter the elemenst: " << endl;

//   for (int i = 0; i <= 7; i++)
//   {
//     int x;
//     cin >> x;
//     input.push_back(x);
//   }

//   for (int i = 0; i < input.size(); i++)
//   {
//     if (input[i] == 1)
//     {
//       freq["1"] = freq["1"] + 1;
//     }
//     else if (input[i] == 2)
//     {
//       freq["2"] = freq["2"] + 1;
//     }
//     else if (input[i] == 3)
//     {
//       freq["3"] = freq["3"] + 1;
//     }
//   }

//   cout << "1 => " << freq["1"] << endl;
//   cout << "2 => " << freq["2"] << endl;
//   cout << "3 => " << freq["3"] << endl;

//   return 0;
// }

#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main()
{
  int n;
  cin >> n;

  vector<int> input(n);

  for (int i = 0; i < n; i++)
  {
    cin >> input[i];
  }

  map<int, int> freq;

  // counting
  for (int i = 0; i < n; i++)
  {
    freq[input[i]]++;
  }

  // printing
  for (auto it : freq)
  {
    cout << it.first << " => " << it.second << endl;
  }

  return 0;
}