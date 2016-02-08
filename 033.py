# Problem 33
# https://projecteuler.net/problem=33
# Question: There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator. If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
# Answer: 100
#
# Approach:
# - Iterate through all valid 2-digit number combinations.
# - Find intersection between numerator and denominator numbers to cancel out.
# - Compare canceled-out fraction value to normal fraction value.
# - Keep a running product and simplify to find final denominator.


# count backwards from the numerator and divide both sides and return the result
# as soon as a common factor is found for both the numerator and the denominator
def simplify(n, d):
  n_simplified = int(n)
  d_simplified = int(d)
  for i in range(n_simplified, 0, -1):
    if n % i == 0 and d % i == 0:
      n_simplified = n / i
      d_simplified = d / i
      break
  return (n_simplified, d_simplified)

def main():
  final_numerator = 1
  final_denominator = 1

  for n in range(1, 10 ** 2):
    for d in range(n + 1, 10 ** 2):
      # remove digits that are on both sides of the fraction line
      n_cancelled = "".join(["0"] + [x for x in str(n) if x not in str(d)])
      d_cancelled = "".join(["0"] + [x for x in str(d) if x not in str(n)])

      # convert numerator and denominator into floats so we can do calculations
      n, d = float(n), float(d)
      n_cancelled, d_cancelled = float(n_cancelled), float(d_cancelled)
      if d_cancelled <= n_cancelled: continue

      # get the decimal value of the fractions
      normal_decimal = n / d
      cancelled_decimal = n_cancelled / d_cancelled

      # check if they lead to the same value, are not equal to each other,
      # and are non-trivial
      if (normal_decimal == cancelled_decimal) and \
         (   n != n_cancelled and    d != d_cancelled) and \
         (n/10 != n_cancelled and d/10 != d_cancelled):

        # calculate the simplified numerator and denominator and keep a running
        # product of these fractions to simplify later to get the answer
        numerator, denominator = simplify(n_cancelled, d_cancelled)
        final_numerator *= numerator
        final_denominator *= denominator

  # simplify the final fraction and print the denominator of it
  print simplify(final_numerator, final_denominator)[1]

if __name__ == '__main__':
  main()