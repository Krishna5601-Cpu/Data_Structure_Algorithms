#include <iostream>
// Bringing the standard namespace into the global scope
using namespace std;

int main()
{
  // 1. A regular variable holding a value
  int age = 25;

  // 2. A pointer variable, declared with an asterisk (*).
  // The '&' (address-of) operator gets the memory address of 'age'.
  int *ptr = &age;

  cout << "--- Pointer Basics ---" << endl;

  // Output the value of the regular variable
  cout << "Value of age: " << age << endl;

  // Output the memory address where 'age' is stored
  cout << "Memory address of age (&age): " << &age << endl;

  // Output the value stored in the pointer (which is the address of 'age')
  cout << "Value stored in ptr (address): " << ptr << endl;

  // 3. Dereferencing: Using the '*' operator on the pointer
  // to get the value stored at that address.
  cout << "Value pointed to by ptr (*ptr): " << *ptr << endl;

  cout << "----------------------" << endl;

  // 4. Modifying the value using the pointer
  *ptr = 30; // Go to the address in ptr, change the value there to 30

  cout << "After modifying via pointer:" << endl;
  cout << "New value of age: " << age << endl;

  return 0;
}