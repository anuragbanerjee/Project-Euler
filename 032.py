# Problem 32
# https://projecteuler.net/problem=32
# Question: Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# Answer: 45228
#
# Approach: Deduce how many digits can multiply and produce a 9-digit identity, check if pandigital, and compute sum.


def main():
  pandigital_chars = [str(x) for x in range(1, 10)]
  products = set()
  for i in range(10 ** 2): # up to 2 digits
    for j in range(i, 10 ** (5-len(str(i)))): # up to 4 digits, making up to a 5-digit number
      # check for and save pandigital identities
      identity = str(i) + str(j) + str(i * j)
      if sorted(identity) == pandigital_chars:
        products.add(i * j)
  print sum(products)

if __name__ == '__main__':
  main()