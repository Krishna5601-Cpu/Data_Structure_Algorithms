#include <iostream>
#include <string>
using namespace std;
int main()
{

  string word;
  cout << "Enter the word: ";
  getline(cin, word);

  int flag = 0;

  int i = 0;
  int j = word.length() - 1;

  while (i < j)
  {
    if (word[i] != word[j])
    {
      flag = 1;
      break;
    }
    i++;
    j--;
  }

  if (flag == 1)
  {
    cout << "Not Palindrome";
  }
  else
  {
    cout << "Palindrome";
  }

  return 0;
}