# Problem 39
# https://projecteuler.net/problem=39
# Question: For which value of p <= 1000, is the number of solutions maximised? P is the perimeter of a right triangle.
# Answer: 840
#
# Approach:
# - Iterate through all 2-number permutations under 1000
# - Calculate perimeter from triangle legs and keep a tally of it.
# - Return the maximum based on the number of tallies.

from itertools import permutations
from collections import defaultdict

def get_perimeter(a, b):
  return a + b + (a ** 2 + b ** 2) ** 0.5

def main():
  tally = defaultdict(int)
  triangle_legs = permutations(range(1000), 2)
  for a, b in triangle_legs:
    tally[get_perimeter(a, b)] += 1
  print max(filter(lambda x: x <= 1000, tally.keys()), key=lambda a: tally[a])

if __name__ == '__main__':
  main()