def sumofdigits(x, b = 0):
  for x in str(x): b = b + int(x)
  return b
print sumofdigits(2**1000)