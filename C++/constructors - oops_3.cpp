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
    age = 20;
  }

  void display()
  {
    cout << name << endl;
    cout << age << endl;
  }
};

class Book
{
public:
  string title;
  string author;
  int price;

  Book()
  {
    title = "Unknown";
    author = "Unknown";
    price = 0;
  }

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

  Laptop()
  {
    brand = "Unknown";
    ram = 0;
    price = 0;
  }

  void display()
  {
    cout << brand << endl;
    cout << ram << endl;
    cout << price << endl;
  };
};

int main()
{

  Student random;

  random.display();

  Book b1;
  b1.display();

  Laptop someones;
  someones.display();

  return 0;
}