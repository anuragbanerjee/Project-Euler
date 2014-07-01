import time

start_time = time.time()

def semi_armstrongs(power):
  final = []
  for x in range(2, (9**power)*(power+1)):
    b = 0
    for y in str(x): b = b + int(y)**power
    if int(b) == x:
      final.append(x)
      print final[-1]
  return final

final = semi_armstrongs(5)
print "sum is", reduce(lambda x, y: x+y, final)

end_time = time.time()
print ("Elapsed time was %g seconds" % (end_time - start_time))
