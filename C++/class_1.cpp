#include <iostream>
using namespace std;
class Student
{

public:
  string name;
  int age;
};

class Book
{
public:
  string title;
  string author;
  int price;
};

class Laptop
{
public:
  string brand;
  int ram;
  int price;
};

int main()
{

  Student krishna;

  krishna.name = "Kunwar Krishna Singh Chauhan";
  krishna.age = 19;

  cout << "Name: " << krishna.name << ", Age: " << krishna.age << endl;

  Book b1;
  b1.title = "Harry Potter";
  b1.author = "J.K Rowling";
  b1.price = 1500;

  Book b2;
  b2.title = "Song of ice and fire";
  b2.author = "Gorge RR Martin";
  b2.price = 2000;

  cout << "Book1 " << "Title: " << b1.title << ", Author: " << b1.author << ", Price: " << b1.price << endl;

  cout << "Book2 " << "Title: " << b2.title << ", Author: " << b2.author << ", Price: " << b2.price << endl;

  Laptop myLaptop;
  myLaptop.brand = "HP";
  myLaptop.ram = 8;
  myLaptop.price = 35000;

  cout << "My Laptop: " << ", Brand: " << myLaptop.brand << ", Ram: " << myLaptop.ram << ", Price: " << myLaptop.price << endl;

  return 0;
}