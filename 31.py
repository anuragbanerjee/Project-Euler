import time

start_time = time.time()

c = [1, 2, 5, 10, 20, 50, 100, 200]
ans = []

for x in c:
  for y in range(1, 201):
      if 200 - (y*x) == 0 and [str(y), str(x) + " pence"] not in c: ans.append([str(y), str(x) + " pence"])

for z in c:
  total = 200 - z
  for y in range(1, 201):
    if total - (y*x) == 0 and [str(y), str(x) + " pence"] not in c:
      ans.append([str(y), str(x) + " pence"])

test = 0

for a in xrange(2):
  if (200*a)==200: print [a,0,0,0,0,0,0,0][::-1]; test += 1; break
  for b in xrange(3):
    if (100*b)+(200*a)==200: print [a,b,0,0,0,0,0,0][::-1]; test += 1; break
    for c in xrange(5):
      if (50*c)+(100*b)+(200*a)==200: print [a,b,c,0,0,0,0,0][::-1]; test += 1; break
      for d in xrange(11):
        if (20*d)+(50*c)+(100*b)+(200*a)==200: print [a,b,c,d,0,0,0,0][::-1]; test += 1; break
        for e in xrange(21):
          if (10*e)+(20*d)+(50*c)+(100*b)+(200*a)==200: print [a,b,c,d,e,0,0,0][::-1]; test += 1; break
          for f in xrange(41):
            if (5*f)+(10*e)+(20*d)+(50*c)+(100*b)+(200*a)==200: print [a,b,c,d,e,f,0,0][::-1]; test += 1; break
            for g in xrange(101):
              if (2*g)+(5*f)+(10*e)+(20*d)+(50*c)+(100*b)+(200*a)==200: print [a,b,c,d,e,f,g,0][::-1]; test += 1; break
              for h in xrange(201):
                if (1*h)+(2*g)+(5*f)+(10*e)+(20*d)+(50*c)+(100*b)+(200*a)==200: print [a,b,c,d,e,f,g,h][::-1]; test += 1; break


print test
end_time = time.time()
print ("Elapsed time was %g seconds" % (end_time - start_time))
