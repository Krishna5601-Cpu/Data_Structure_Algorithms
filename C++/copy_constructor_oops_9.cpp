#include <iostream>
using namespace std;

class Student
{
public:
  string name;
  int age;

  Student(string n, int a)
  {
    name = n;
    age = a;
  }

  void display()
  {
    cout << name << " " << age << endl;
  }
};

int main()
{
  Student s1("Krishna", 20);

  Student s2 = s1;

  s2.name = "Rahul";

  s1.display();

  s2.display();
}