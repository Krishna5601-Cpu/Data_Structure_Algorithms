
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

int main()
{
  Student s;

  s.name = "Krishna";
  s.age = 20;
  s.rollNo = 101;

  s.introduce();

  cout << s.rollNo;

  return 0;
};

// #include <iostream>
// using namespace std;

// class Person
// {
// public:
//   string name;
//   int age;

//   void introduce()
//   {
//     cout << name << " " << age << endl;
//   }
// };

// // class Students(Person) {

// //   public:
// //   int rollNo;

// // };

// // class Students extends Person
// // {

// // public:
// //   int rollNo;
// // };

// int main()
// {
//   // Student s;

//   // s.name = "Krishna";
//   // s.age = 20;
//   // s.rollNo = 101;

//   // s.introduce();

//   // cout << s.rollNo;
// }