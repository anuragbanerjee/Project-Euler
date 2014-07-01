def selfpowersum(limit):
  a, final = [x**x for x in range(1, limit + 1)], 0
  for x in a: final += x
  else: return final

print "".join(list(str(selfpowersum(1000)))[-10:])
