import time

start_time = time.time()

def divisors(n): return [a for a in range(1, n) if n % a == 0]
def sum(l): return reduce(lambda x, y: x+y, l + [0])

def getamicables(limit):
    y = {x:sum(divisors(x)) for x in range(0, limit)}
    o = y.items()
    l = [c[::-1] for c in o]
    o = [x[0] for x in o if x in (o and l) and x[::-1] != x]
    return sum(o)

print getamicables(10000)

end_time = time.time()
print ("Elapsed time was %g seconds" % (end_time - start_time))