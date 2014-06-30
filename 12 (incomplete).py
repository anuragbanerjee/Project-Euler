a = []
z = 0

def generate_triangular(start = 1, end = 10):
  z = 0
  for y in range(start, end):
    z += y
    a.append([z,0])
  else: return a

generate_triangular()

def get_divisors(c = 0):
  for b in range(len(a)-c):
    d = 0
    while a[c][0] != d:
      if a[c][0] % (d+1) == 0: a[c][1] += 1
      d += 1
      print a[c][0], a[c][1], c, d
    c += 1
  else: check()

def check():
  e = 0
  for x in a:
    if a[e][1] > 5:
      return a[e]
      break
    else:
      f = len(a)-1
      get_divisors(0)
      generate_triangular(a[f][0], a[f][0]+2)

print check()
