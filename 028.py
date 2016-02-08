# Problem 28
# https://projecteuler.net/problem=28
# Question: What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
# Answer: 669171001
#
# Approach: Determine how the spiral's diagonals can be predicted using a linear formula.

def main():
  size = 1001 * 1001
  sum_of_diagonals = 1
  diagonal = 0
  number = 1
  buffer = 2
  while number < size:
    number += buffer
    diagonal += 1
    sum_of_diagonals += number
    if diagonal % 4 == 0:
      buffer += 2
  print sum_of_diagonals

if __name__ == '__main__':
  main()