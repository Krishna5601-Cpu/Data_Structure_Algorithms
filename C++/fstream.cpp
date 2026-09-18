// #include <iostream>
// #include <fstream>
// using namespace std;

// // int main()
// // {
// //   ofstream file("students.txt");

// //   file << "Krishna 95\n";
// //   file << "Rahul 88\n";

// //   file.close();

// //   cout << "Data Saved!";

// // }

// #include <iostream>
// #include <fstream>
// using namespace std;

// int main()
// {
//   ifstream file("students.txt");

//   string name;
//   int marks;

//   while (file >> name >> marks)
//   {
//     cout << name << " " << marks << endl;
//   }

//   file.close();
// };

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
  ofstream file("result.txt");

  string name;
  int marks;

  cout << "Enter students data:\n";

  for (int i = 1; i <= 3; i++)
  {
    cout << "\nStudent " << i << endl;

    cout << "Name: ";
    getline(cin >> ws, name);

    cout << "Marks: ";
    cin >> marks;

    file << name << " " << marks << endl;
  }

  file.close();

  cout << "\nData saved successfully!";
}