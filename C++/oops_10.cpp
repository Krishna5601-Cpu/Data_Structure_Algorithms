#include <iostream>
using namespace std;

class Person
{
public:
  string name = "Krishna";
};

class Student : private Person
{
};

int main()
{

  Student s;

  // cout << s.name;

  // Monitor m;

  // m.name = "Krishna";
  // m.age = 20;
  // m.rollNo = 101;
  // m.section = "A";

  // m.introduce();

  return 0;
};
