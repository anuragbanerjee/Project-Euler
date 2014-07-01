import time

start_time = time.time()

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def generate_triangular_number(i = 1, c = 1):
  return c, i = c + i + 1, i + 1

def has_factors(limit, answer = "", b = {}):
  i = 1
  c = 1
  while answer == "":
    generate_triangular_number(i, c)
    b[c] = factors(c)
    if len(b[c]) >= limit:
      answer = len(b[c])
      return str(c) + " has " +str(answer) + " factors"

print has_factors(500)

end_time = time.time()
print ("Elapsed time was %g seconds" % (end_time - start_time))
