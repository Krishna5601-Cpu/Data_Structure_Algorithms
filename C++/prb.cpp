#include <iostream>
using namespace std;

class Person
{
public:
  string name = "Person";

  void introduce()
  {
    cout << name << endl;
  }
};

class Krishmna : public Person
{
public:
  string name = "Krishna Jii";
};

int main()
{
  Krishmna k1;
  cout << k1.name << endl;

  return 0;
}
