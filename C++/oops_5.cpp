#include <iostream>
using namespace std;

class BankAccount
{
private:
  int balance;

public:
  void setBalance(int b)
  {
    if (b >= 0)
    {
      balance = b;
      cout << "Balance Updated: " << balance << endl;
    }
    else
    {
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

  BankAccount account;

  // account.balance = 5000;
  account.setBalance(5000);

  // account.display();

  return 0;
}