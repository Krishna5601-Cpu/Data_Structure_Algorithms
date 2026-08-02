#include <iostream>
using namespace std;

// // // class Student
// // // {
// // // public:
// // //   int *marks;

// // //   Student()
// // //   {
// // //     marks = new int(95);
// // //   }

// // //   ~Student()
// // //   {
// // //     delete marks;
// // //   }
// // // };

// // class Student
// // {
// // public:
// //   int *marks;

// //   Student(int m)
// //   {
// //     marks = new int(m);
// //   };

// //    Student(const Student &other)
// //   {
// //     *marks = &marks;
// //   }

// // };

// // // class Student
// // // {
// // // public:
// // //   string name;
// // //   int age;

// // //   Student(string n, int a)
// // //   {
// // //     name = n;
// // //     age = a;
// // //   }

// // //   void display()
// // //   {
// // //     cout << name << " " << age << endl;
// // //   }
// // // };

// // int main()
// // {
// //   // Student s1("Krishna", 20);

// //   // Student s2 = s1;

// //   // s2.name = "Rahul";

// //   // s1.display();

// //   // s2.display();

// //   //   Student s1;

// //   // Student s2 = s1;

// //   Student s1(95);

// //   Student s2 = s1;

// //   *s2.marks = 100;

// // }

// #include <iostream>
// using namespace std;

// class Student
// {
// public:
//   int *marks;

//   Student(int m)
//   {
//     marks = new int(m);
//   };

//   Student(const Student &other)
//   {
//     marks = new int(*other.marks);
//   }

//   ~Student()
//   {
//     delete marks;
//   }

//   void display()
//   {
//     cout << *marks << endl;
//   }
// };

// int main()
// {
//   Student s1(95);

//   Student s2 = s1;

//   *s2.marks = 100;

//   cout << "s1 = ";
//   s1.display();

//   cout << "s2 = ";
//   s2.display();
// }

class Student
{
public:
  int *marks;

  Student(int m)
  {
    marks = new int(m);
    cout << "Constructor\n";
  }

  Student(const Student &other)
  {
    marks = new int(*other.marks);
    cout << "Copy Constructor\n";
  }

  ~Student()
  {
    delete marks;
    cout << "Destructor\n";
  }
};

int main()
{
  Student s1(95);

  Student s2 = s1;

  Student s3 = s2;

  *s2.marks = 100;

  cout << *s1.marks << endl;
  cout << *s2.marks << endl;
  cout << *s3.marks << endl;
}