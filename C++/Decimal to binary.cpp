#include <iostream>
#include <cmath>
using namespace std;

int main()
{
  int num;
  cout << "Enter number: ";
  cin >> num;

  int i = 0;
  int answer = 0;

  while (num != 0)
  {
    int bit = num & 1;

    answer = (bit * pow(10, i)) + answer;

    num = num >> 1;
    i++;
  }

  cout << "Answer: " << answer << endl;

  return 0;
}