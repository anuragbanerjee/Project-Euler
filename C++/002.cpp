#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;

int main ()
{
  int total = 0;
  int limit = 4000000;

  int fib1 = 1;
  int fib2 = 1;

  while (fib2 < limit) {
    if (fib2 % 2 == 0) {
      total += fib2;
    }

    int temp = fib2;
    fib2 = fib1 + fib2;
    fib1 = temp;
  }

  cout << total << endl;
}