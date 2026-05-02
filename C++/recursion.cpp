#include <iostream>
using namespace std;

void print(int n)
{
  if (n == 0)
  {
    return;
  }

  print(n - 1);
  cout << n << " ";
}

int sumTillNum(int num)
{
  if (num == 1)
  {
    return 1;
  }
  return num + sumTillNum(num - 1);
}

int factorial(int num)
{
  if (num == 0 || num == 1)
  {
    return 1;
  }
  return num * factorial(num - 1);
}

void oddTillNums(int nums)
{
  if (nums == 0)
    return;

  oddTillNums(nums - 1);

  if (nums % 2 == 1)
  {
    cout << nums << " ";
  }
}

int fib(int n)
{

  if (n <= 1)
  {
    return n;
  }

  return fib(n - 1) + fib(n - 2);
}

void reverseString(string word, int i)
{

  if (i == word.length())
  {
    return;
  }

  reverseString(word, i + 1);

  cout << word[i] << " ";
}

bool isPalindrome(string str, int i, int j)
{
  if (i >= j)
    return true;

  if (str[i] != str[j])
    return false;

  return isPalindrome(str, i + 1, j - 1);
}

int main()
{

  //   print(5);
  //   print(5)
  // → print(4)
  // → print(3)
  // → print(2)
  // → print(1)
  // → print(0) (stop)

  // What is Recursion?
  //  Recursion = function calling itself

  // function () {
  //   work
  //   function();
  // }

  // Every recursion must have a base case (condition to stop) and recurscive call(to call function it self)

  // int res = factorial(6);
  // cout << res << endl;

  // int sum = sumTillNum(7);
  // cout << sum << endl;

  // oddTillNums(11);
  // reverseString("Krishna", 0);

  // if (isPalindrome("haah", 0, 3))
  // {
  //   cout << "Yes: " << endl;
  // }
  // else
  // {
  //   cout << "No; " << endl;
  // }

  return 0; // successfully executed :)
}
