a, x, limit = [1, 2], 1, 10001

def isprime(candidate):
  a = 2
  while candidate > a :
    if candidate%a==0 and a!=candidate:
      z = 0 ##is composite
      break
    a = a + 1
  else:
    z = 1##isprime
  return z

while len(a) <=limit:
  x = x + 2
  if isprime(x) == 1:
    a.append(x)
    print x
else:
  z = a[::-1]
  print z[0], "is the 10001st prime number"
