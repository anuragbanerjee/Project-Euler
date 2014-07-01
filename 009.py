x = []

for a in range(1,1000):
  for b in range(1,1000):
    for c in range(1,1000):
      if a < b and b < c:
        if a**2 + b**2 == c**2:
          print a**2, "+", b**2, "=", c**2
          d = []
          d.append(a)
          d.append(b)
          d.append(c)
          x.append(d)

for e in range(len(x)):
  if x[e][0] + x[e][1] + x[e][2] == 1000:
    print "abc =",x[e][0]*x[e][1]*x[e][2]
