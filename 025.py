a = [1, 1, 2]
limit = 1000
i = 3

while len(str(a[2])) != limit:
  a[0] = a[1]
  a[1] = a[2]
  a[2] = a[0] + a[1]
  i += 1
else: print "Fibonacci Term", i, "is", a[2]
