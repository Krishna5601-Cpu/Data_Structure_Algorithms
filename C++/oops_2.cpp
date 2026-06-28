#include <iostream>
using namespace std;

class Student
{
public:
  // Data Members or Attributes -
  string name;
  int age;

  // Member Functions or Methods
  void display()
  {
    cout << name << endl;
    cout << age << endl;
  };
};

class Book
{
public:
  string title;
  string author;
  int price;

  void display()
  {
    cout << title << endl;
    cout << author << endl;
    cout << price << endl;
  };
};

class Laptop
{
public:
  string brand;
  int ram;
  int price;

  void display()
  {
    cout << brand << endl;
    cout << ram << endl;
    cout << price << endl;
  };
};

class Employee
{
public:
  string company = "Haha Hehe Company";

  void display()
  {
    cout << "Company: " << company << endl;
  };
};

int main()
{

  Student krishna;
  krishna.name = "Kunwar Krishna Singh Chauhan";
  krishna.age = 20;

  krishna.display(); // Calling display method, which is declared in Student class.

  Book b1;
  b1.title = "Harry Potter";
  b1.author = "J.K Rowling";
  b1.price = 1500;

  Book b2;
  b2.title = "Song of ice and fire";
  b2.author = "Gorge RR Martin";
  b2.price = 2000;

  b1.display();
  b2.display();

  Laptop myLaptop;
  myLaptop.brand = "HP";
  myLaptop.ram = 8;
  myLaptop.price = 35000;

  myLaptop.display();

  Employee random;

  random.display(); // Member function called but no value is assigned in object, so it uses the default name give in class - Default Member Initializer

  return 0;
}