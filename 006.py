limit = 100
a = []
b = []
c = 0
d = 0

for x in range(limit):
  a.append(x+1)

for x in a:
  b.append(x*x)
  d = x + d

for x in b:
  c = x + c

print d**2 - c
