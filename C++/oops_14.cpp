// // #include <iostream>
// // using namespace std;

// // class Complex
// // {
// // public:
// //   int real;
// //   int imag;

// //   Complex(int r, int i)
// //   {
// //     real = r;
// //     imag = i;
// //   }

// //   void display()
// //   {
// //     cout << real << " + " << imag << "i" << endl;
// //   }

// //   // Complex operator+(Complex a, Complex b)
// //   // {

// //   // }

// // };

// // int main()
// // {

// //   return 0;
// // };

// #include <iostream>
// using namespace std;

// class Complex
// {
// public:
//   int real;
//   int imag;

//   Complex(int r, int i)
//   {
//     real = r;
//     imag = i;
//   }

//   Complex operator+(const Complex &other)
//   {
//     return Complex(real + other.real,
//                    imag + other.imag);
//   }

//   void display()
//   {
//     cout << real << " + " << imag << "i" << endl;
//   }
// };

// int main()
// {
//   Complex c1(2, 3);
//   Complex c2(4, 5);

//   Complex c3 = c1 + c2;

//   c3.display();
// }

// Complex c1(10, 20);
// Complex c2(1, 2);

// Complex c3 = c1 + c2;
// Complex c4 = c3 + c1;

// c4.display();