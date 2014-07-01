from math import factorial

final = 0

for x in range(3, 1000000):
  sum = 0
  for n in str(x): sum += factorial(int(n))
  if sum == x: final += x

print final
