import time

start_time = time.time()

def isprime(candidate):
  if candidate < 2: return "Neither"
  else:
    i = 3
    while candidate/(i-1) > i:
      if candidate%i==0: return False
      else: i += 2
    else: return True

def sumofprimesunder(number, below = 1, sum = 2):
  for x in range(1, number+below, 2):
    if isprime(x):sum += x
  else:return sum

print sumofprimesunder(2000000)

end_time = time.time()
print ("Elapsed time was %g seconds" % (end_time - start_time))
