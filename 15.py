import itertools
from math import factorial
from gmpy import comb
import time

start_time = time.time()

w = 4
h = 4

x = ""
y = ""

for a in range(w): x += "r"
for b in range(h): y += "d"

print x,y

print len(list(set(itertools.permutations(x+y))))

print comb(2 * 20, 20)

end_time = time.time()
print ("Elapsed time was %g seconds" % (end_time - start_time))
