#include <iostream>
using namespace std;

class Vehicle
{
public:
  virtual void start()
  {
    cout << "Vehicle Started" << endl;
  }
};

class Car : public Vehicle
{
  void start()
  {
    cout << "Car Engine Started" << endl;
  }
};

class Bike : public Vehicle
{
  void start()
  {
    cout << "Bike Started" << endl;
  }
};

int main()
{
  Vehicle *v1 = new Car();
  Vehicle *v2 = new Bike();

  v1->start();
  v2->start();

  delete v1;
  delete v2;
}