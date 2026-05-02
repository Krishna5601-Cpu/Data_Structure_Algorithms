#include <iostream>
#include <string>
using namespace std;

void greet()
{
  cout << "Hello! Krishna :) " << endl;
}

void add(int a, int b)
{
  cout << a + b << endl;
}

int sum(int a, int b)
{
  return a + b;
}

string myName(string name)
{
  getline(cin, name);
  return name;
}

int maxOfTwo(int a, int b)
{
  if (a > b)
  {
    return a;
  }
  else
  {
    return b;
  }
}

int fact(int n)
{

  int fact = 1, i = 1;

  for (i = 1; i <= n; i++)
  {
    fact = fact * i;
  }

  cout << fact << endl;

  return fact;
}

string evenORodd(int num)
{
  if (num % 2 == 0)
    return "Even";
  else
    return "Odd";
}

int maxOfThree(int a, int b, int c)
{
  if (a >= b && a >= c)
    return a;
  else if (b >= a && b >= c)
    return b;
  else
    return c;
}

string palindrome(string word)
{
  int i = 0, j = word.length() - 1;
  while (i < j)
  {
    if (word[i] != word[j])
    {
      return "No";
    }
    i++;
    j--;
  }

  return "Yes";
}

int main()
{

  //   return_type function_name(parameters)
  // {
  //     // code
  // }

  // greet(); // Function Call
  // add(7, 8);
  // int res = sum(99, 1);
  // cout << res << endl;

  // myName("Krishna");

  // cout << maxOfTwo(67, 69) << endl;

  // fact(6);

  // int num;
  // cin >> num;
  // evenORodd(num);

  // int num, num1, num2;
  // cin >> num >> num1 >> num2;
  // maxOfThree(num, num1, num2);

  // string word;
  // cout << "Enter the word: " << endl;
  // getline(cin, word);
  // string result = (word);
  // cout << result << endl;

  // cout << palindrome("abba");

  return 0;
}