##largest palindromic product of two 3-digit numbers
palindromes = []

for x in range(100, 1000):
  for y in range(100, 1000):
    a = list(str(x*y))
    if a == a[::-1] and a!=0:
      palindromes.append("".join(a))
palindromes = [int(x) for x in palindromes]
for i in sorted(palindromes):print i
