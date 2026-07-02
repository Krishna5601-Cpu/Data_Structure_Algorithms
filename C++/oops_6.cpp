// Constructors + Encapsulation
#include <iostream>
using namespace std;

class BankAccount
{
private:
  int balance;

public:
  BankAccount(int b)
  {
    if (b >= 0)
    {
      balance = b;
    }
    else
    {
      balance = 0;
      cout << "Invalid Balance" << endl;
    }
  }

  void display()
  {
    cout << balance << endl;
  }
};

int main()
{

  BankAccount account1(5000);
  BankAccount account2(-5000);

  // account.balance = 5000;
  // account.setBalance(5000);

  // account.display();

  return 0;
}