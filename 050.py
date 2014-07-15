# answer is 997651
# timed ~ 11 seconds

def isprime(candidate):
    if candidate % 2 == 0: return False
    else:
        i = 3
        while candidate / (i-1) > i:
            if candidate % i == 0: return False
            else: i += 2
        else: return True

primes = [2, 3]
while len(primes) < 1000: primes.extend([n for n in range(primes[-1] + 2, 50 + primes[-1], 2) if isprime(n)])
comb = [ (a, b) for a in xrange(len(primes)) for b in xrange(len(primes)) if a < b ]

z = (0, 0)

for a in comb:
    x = primes[ a[0] : a[1] ]
    l, s = len(x), sum(x)
    if s > 1000000: continue
    elif isprime(s) and l > z[0]: z = (l, s)

print z[1]