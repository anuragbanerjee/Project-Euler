import time

start_time = time.time()

def longestcollatzunder(n):
  bestcount, beststart = 0, 0
  for x in range(1, n):
    last, starter, counter = x, x, 1
    while last != 1:
      if last % 2 == 0: last = last / 2
      else: last = (3 * last) + 1
      counter += 1
    else:
      if counter > bestcount: bestcount, beststart = counter, starter
  else: return beststart, bestcount

f = longestcollatzunder(1000000)
print f[0], "has the longest Collatz Sequence", "-->", f[1]

end_time = time.time()
print ("Elapsed time was %g seconds" % (end_time - start_time))
