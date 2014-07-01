div, nums, attempt, x, y = [], 20, 2, 1, 1

for x in xrange(nums):
  div.append(x+1)

while x <= nums:
  if x <= nums:
    for z in div:
      if attempt % z == 0:
        print "PASS", attempt, "/", z, x
        if x == z:
          x = x + 1
        else:
          x = 1
          break
      else:
        print "FAIL", attempt, "/", z, x
        attempt = attempt + 20
        x = 1
        break
else:
  print attempt, "can be divided by all numbers below", nums+1
