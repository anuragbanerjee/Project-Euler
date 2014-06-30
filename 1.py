sum = 0
for x in range(1000):
  if x % 3 == 0 and x % 5 == 0:
    sum = sum + x
  else:
    if x % 3 == 0:
      sum = sum + x
    if x % 5 == 0:
      sum = sum + x
print sum
