// #include <iostream>
// #include <fstream>
// using namespace std;

// int main()
// {
//   int a, b;
//   cin >> a >> b;

//   try
//   {
//     if (b == 0)
//       throw "Division by zero!";

//     cout << a / b;
//   }
//   catch (const char *msg)
//   {
//     cout << msg;
//   }

//   try
//   {
//     throw 404;
//   }
//   catch (int x)
//   {
//     cout << "Integer Error: " << x;
//   }
//   catch (...)
//   {
//     cout << "Unknown Error";
//   };

//   ifstream file("students.txt");

//   if (!file)
//   {
//     cout << "File not found!";
//     return 0;
//   }

//   return 0;
// }

#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>
using namespace std;

int main()
{
  string name;
  double marks;

  // Ask user for name
  cout << "Enter student name: ";
  getline(cin, name);

  // Ask user for marks
  cout << "Enter student marks: ";
  cin >> marks;

  try
  {
    // Check if marks are out of range
    if (marks < 0 || marks > 100)
    {
      throw runtime_error("Invalid Marks");
    }

    // Save student into students.txt
    ofstream file("students.txt", ios::app);
    file << name << "," << marks << endl;
    file.close();

    cout << "Saved Successfully" << endl;
  }
  catch (runtime_error &e)
  {
    // Catch the exception and print the message
    cout << e.what() << endl;
  }

  return 0;
}