lim, sum, f, npos = input("What is the largest acceptable number?"), 0, [1], input("How many Fibonacci numbers do you want?")

if lim == "":
  lim = 10 ** 100
if npos == "":
  npos = 10 ** 100

for x in f: ##gets fibonacci numbers
  z = x + f[f.index(x)-1]
  if f.index(x)+1 < npos + 1:
    if z < lim:
      f.append(z)
      print "Fibonacci #" + str(f.index(x)+1) , "is", x
    else:
      print "Fibonacci #" + str(f.index(x)+1) , "is", x
      break

for y in f:
  if y % 2 == 0:sum = sum + y
print "The sum of all the even Fibonacci numbers under", lim, "is", sum
