#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  ofstream file("students.txt");

  file << "Krishna 95\n";
  file << "Rahul 88\n";

  file.close();

  cout << "Data Saved!";
}