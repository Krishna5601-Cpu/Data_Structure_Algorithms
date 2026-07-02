// Constructor overloading 
#include <iostream>
using namespace std;

class Student
{

public:
  string name;
  int age;

  Student()
  {
    name = "Unknown";
    age = 0;
  };

  Student(string naam)
  {
    name = naam;
    age = 0;
  };

  Student(string naam, int umar)
  {
    name = naam;
    age = umar;
  };

  void display()
  {
    cout << "Name: " << name << endl;
    cout << "Age : " << age << endl;
  }
};

int main()
{

  Student s1("Krishna", 20);
  Student s2("Yash");
  Student s3;

  s1.display();
  s2.display();
  s3.display();

  return 0;
}