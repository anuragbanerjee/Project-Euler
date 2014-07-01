import time
from itertools import permutations

start_time = time.time()

def isprime(candidate):
  if candidate < 2: return "Neither"
  if candidate % 2 == 0: return False
  else:
    i = 3
    while candidate/(i-1) > i:
      if candidate%i==0: return False
      else: i += 2
    else: return True

def isallperms(thelist):
  num = str(thelist[0])
  perms = ["".join(p) for p in permutations(num)]
  final = 0
  for i in thelist:
    if str(i) in perms:
      final += 1
  if final == len(thelist): return True
  else: return False

primes = [x for x in range(1, 10000, 2) if isprime(x)]

for e in primes:
  for a in range(2, 3333, 2):
    if (e + a) in primes:
      if (e + (2 * a)) in primes:
        if isallperms((e, e + a, e + 2 * a)):
          numbers = (e, e + a, e + 2 * a)
          print numbers, "increase by a factor of " + str(a), "".join(str(n) for n in numbers)


end_time = time.time()
print ("Elapsed time was %g seconds" % (end_time - start_time))