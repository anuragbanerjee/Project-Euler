# answer is 142857
# timed ~ 1.09 seconds


def getdigits(n):
	digits = []
	while n:
		digits.append(n % 10)
		n /= 10
	return sorted(digits)

def main():
	done = 0
	n = 1
	while not done:
		digits = getdigits(n)
		for x in range(2, 7):
			if getdigits(n * x) == digits:
				if x == 6: done = n; break
			else: break
		n += 1
	else:
		return done

print main()