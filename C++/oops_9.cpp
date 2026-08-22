#include <iostream>
using namespace std;

class Person
{
public:
  string name;
  int age;

  void introduce()
  {
    cout << name << " " << age << endl;
  }
};

class Student : public Person
{
public:
  int rollNo;
};

class Monitor : public Student
{
public:
  string section;
};

int main()
{
  Monitor m;

  m.name = "Krishna";
  m.age = 20;
  m.rollNo = 101;
  m.section = "A";

  m.introduce();
  return 0;
};
