# Problem 38
# https://projecteuler.net/problem=38
# Question: What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
# Answer: 932718654
#
# Approach: Filter out the only ways to get a 9-digit concatenated product and iterate through to find pandigital numbers.
#

def main():
  candidate = max = 0
  while candidate < 10000:
    if 0 < candidate < 10: # 1-2 digit 9 times = 9-18 digits
      n = 9
    elif 100 < candidate < 334: # 3-4 digits 3 times = 9-12 digits
      n = 3
    elif 1000 < candidate < 100000: # 4-5 digits 2 times = 8 - 10 digits
      n = 2
    else:
      candidate += 1
      continue

    cproduct = concatenated_product(candidate, n)
    if is_pandigital(cproduct) and cproduct > max:
      max = cproduct
    candidate += 1
  print max

def is_pandigital(candidate):
  if len(str(candidate)) != 9: return False
  candidate = str(candidate)
  for n in range(1, 10):
    if str(n) not in candidate:
      return False
  return True

def concatenated_product(integer, n):
  total = ""
  for i in range(1, n + 1):
    total += str(integer * i)
  return total

if __name__ == '__main__':
  main()