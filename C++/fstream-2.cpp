#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  fstream file("notes.txt", ios::out);

  file << "Hello Krishna";
  file.close();

  return 0;

  // fstream file("notes.txt", ios::in);

  // string text;
  // getline(file, text);

  // cout << text;
}