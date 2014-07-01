import time

start_time = time.time()

def isprime(candidate):
  if candidate < 2: return "Neither"
  else:
    i = 3
    while candidate/(i-1) > i:
      if candidate%i==0: return False
      else: i += 2
    else: return True

def rotate(n):
  a = list(str(n))
  return [int(''.join(a[t:] + a[:t])) for t in range(1, len(a)+1)]

def cprimes_upto(limit):
  circular_primes = []
  for x in range(1, limit, 2):
    z = 0
    for y in rotate(x):
      if y % 2 == 0: break
      if isprime(y): z += 1
      if z == len(rotate(x)): circular_primes.append(x)
  return circular_primes

print len(cprimes_upto(1000000))

end_time = time.time()
print ("Elapsed time was %g seconds" % (end_time - start_time))
