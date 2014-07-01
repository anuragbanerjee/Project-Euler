start = 40755
tp = 0
pp = 0
hp = 0

t = []
p = []
h = []

def main():
  global t, p, h, tp, pp, hp
  for x in range(100001):t.append(((tp)*(tp+1))/2); tp += 1
  for x in range(10001):p.append(((pp)*((pp*3)-1))/2);pp += 1
  for x in range(1001):h.append(hp*((2*hp)-1));hp += 1

def recursion():
  global t, p, h
  for x in t:
    if x in p and x in h: print x;
    if x in p and x in h and x > 40755: return x;
    else: main()
  else: recursion()

main()
recursion()
