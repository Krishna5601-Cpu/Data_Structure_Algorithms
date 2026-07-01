#include <iostream>
using namespace std;

class Student
{
public:
  string name;
  int age;

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

  Student krishna("Krishna", 20);
  Student rahul("Rahul", 19);
  Student aman("Aman", 21);

  krishna.display();
  rahul.display();
  aman.display();

  return 0;
}