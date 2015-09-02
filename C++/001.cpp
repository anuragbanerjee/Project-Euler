#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;

int main ()
{
  int candidate = 0;
  int sum = 0;
  while (candidate < 1000) {
    bool match = candidate % 5 == 0 || candidate % 3 == 0;
    if (match == true) {
      sum += candidate;
    }
    candidate++;
  }
  cout << sum;
}