# Problem 23
# https://projecteuler.net/problem=23
# Question: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
# Answer:
#
# Approach: Find all abundant numbers below limit, brute force combinations.

from collections import defaultdict
from itertools import combinations_with_replacement

cache = defaultdict(set)

def main():
  limit = 28123
  abundant = defaultdict(int)
  for i in set(range(1, limit + 1)) - set(abundant.keys()):
    f = sum(get_factors(i))
    if f > i:
      for j in range(i, limit, i):
        abundant[j] = f
  abundant_sums = set(x + y for x, y in combinations_with_replacement(abundant.keys(), 2))
  print sum(set(range(limit + 1)) - abundant_sums)

def get_factors(number):
  i = number/2
  factors = set([1])
  total = 1
  while i > 1 and total <= number: # end quickly if abundant
    if i in factors:
      i -= 1
      continue
    if number % i == 0:
      factors.add(i)
      factors.add(number / i)
      total += i + (number / i) # to check for abundance
      if i in cache.keys() or (number / i) in cache.keys():
        factors = factors | cache[i]
    i -= 1
  cache[number] = factors
  return factors

if __name__ == '__main__':
  main()