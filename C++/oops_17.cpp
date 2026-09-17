#include <iostream>
using namespace std;

class Employee
{

public:
  string name;

  Employee()
  {
    name = "jo bhi apka naam hai: ";
  };

  virtual void work() = 0;
};

class Developer : public Employee
{
public:
  Developer(string naam)
  {
    name = naam;
  };

  void work() override
  {
    cout << "Krishna is writing C++ code: " << endl;
  }
};

class Designer : public Employee
{
public:
  Designer(string naam)
  {
    name = naam;
  };
  void work() override
  {
    cout << "Riya is designing UI: " << endl;
  }
};

int main()
{

  Employee *e1 = new Developer("Krishna");
  Employee *e2 = new Designer("Riya");

  e1->work();
  e2->work();

  return 0;
}