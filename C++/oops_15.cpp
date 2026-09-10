#include <iostream>
using namespace std;

class Vehicle
{

public:
  virtual void start()
  {
    cout << "Vehicle started: " << endl;
  }
};

class Car : public Vehicle
{

public:
  void start()
  {
    cout << "Car Engine Started: " << endl;
  }
};

class Bike : public Vehicle
{

public:
  void start()
  {
    cout << "Bike Started: " << endl;
  }
};

int main()
{

  Vehicle *v1 = new Car();
  Vehicle *v2 = new Bike();

  v1->start();
  v2->start();

  return 0;
}