#include <iostream>
using namespace std;

class Student
{
public:
  // Properties / Data Members -
  string name;
  int age;
  int weight;
  int height;

  // Behaviour / Member Functions -
  void running()
  {
    cout << "I am running " << endl;
  }

  void studying()
  {
    cout << name << " is studying" << endl;
  }

  // Default Constructor -
  Student()
  {
    cout << "Object Initialised, I am inside Default Constructor" << endl;
  }

  // Parameterised Constructor -
  Student(string myName, int age, int weight, int height)
  {
    cout << "I am inside Parameter Constructor :) " << endl;
    name = myName;
    age = age;
    weight = weight;
    height = height;

    this->name = myName;
    this->age = age;
    this->weight = weight;
    this->height = height;
  }

  ~Student()
  {
    cout << "I am inside destructor :- " << endl;
  }
};

int main()
{
  // cout << sizeof(Student) << endl; Size of empty class is 1

  // Object Creation :-
  // Static way -
  Student krishna;

  krishna.name = "Kunwar Krishna Singh Chauhan";
  krishna.age = 20;
  krishna.weight = 55;
  krishna.height = 176;
  krishna.running();
  krishna.studying();

  // Dynamic Way -
  Student *ayush = new Student();
  (*ayush).age = 16;
  (*ayush).weight = 50;
  (*ayush).height = 180;
  (*ayush).name = "Ayush";
  (*ayush).running();
  (*ayush).studying();
  ayush->name = "Kunwar Ayush Singh Chauhan"; // (*abc). === abc->

  Student Yash("Yash", 25, 66, 180);
  Student Vansh;

  Student *Gohan = new Student("Gohan", 24, 65, 165);

  //   Student(string myName, int age, int weight, int height)
  //   {
  // using This->
  //     cout << "I am inside Parameter Constructor :) " << endl;
  //     name = myName;
  //     age = age;
  //     weight = weight;
  //     height = height;

  // this->name = myName;
  // this->age = age;
  // this->weight = weight;
  // this->height = height;

  //   }
  // };

  // Calling Destructor
  delete ayush;
  delete Gohan;
  return 0;
}