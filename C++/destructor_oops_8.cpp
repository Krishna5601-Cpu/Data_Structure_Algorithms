#include <iostream>
using namespace std;

class Test
{
public:
  Test()
  {
    cout << "A\n";
  }

  ~Test()
  {
    cout << "B\n";
  }
};

int main()
{
  Test t1;

  {
    Test t2;

    cout << "C\n";
  }

  cout << "D\n";
}

// class Student
// {
// public:
//   Student()
//   {
//     cout << "Constructor Called\n";
//   }

//   ~Student()
//   {
//     cout << "Destructor Called \n";
//   }
// };

// int main()
// {
//   Student s1;

//   cout << "Inside Main\n";

//   return 0;
// }

// class Student
// {
// public:

//     int* marks;

//     Student()
//     {
//         marks = new int[5];
//     }
// };
