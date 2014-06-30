n = 600851475143
primes = []
x = 0
def isprime(candidate):
  a = 2
  while candidate > a :
    if candidate%a==0 and a!=candidate:
      z = 0
      break
    a += 1
  else: # loop not exited via break
    z = 1
  return z

ans, x = 2, 600851475143
while x != ans:
  if x % ans == 0:
    x = x/ans
    ans = 2
  else: ans+=1
print ans


"""
while x < n:
  if isprime(x) == 1 and x!=0:
      primes.append(x)
      print x, str(len(str(x))) + "/" + str(len(str(n))), str((x/n)*100) + "% done"
  x += 1
else:
  for i in primes[::-1]:
    if i != 0:
      if n%i == 0:
        q = i
  print q, "is the largest prime factor of", n
"""
