# answer is 748317
# timed ~ 6.3 seconds

def isprime(candidate):
	if candidate == 2: return True
	if candidate <= 1 or candidate % 2 == 0: return False
	i = 3
	while candidate/(i-1) > i:
		if candidate % i == 0: return False
		i += 2
	return True

def islistofprimes(list):
	return all((isprime(x) for x in list))

def getdigits(x):
	digits = []
	while x:
		digits.insert(0, x % 10)
		x /= 10
	return digits

def cutleft(x, digits):
	output = []
	l = len(digits)-1
	while l:
		shift = 10 ** l
		x -= (digits[0] * shift)
		l -= 1
		output += [x]
		del digits[0]
	return output

def cutright(x, digits):
	if not digits: digits = digits(x)
	output = []
	while x / 10 > 0:
	    output += [x / 10]
	    x /= 10
	return output

def istruncatedprime(number):
	digits = getdigits(number)
	part1 = cutright(number, digits)
	if not islistofprimes(part1): return False
	part2 = cutleft(number, digits)
	return islistofprimes(part1 + part2)

def main():
	truncatable_primes, current_number = [], 9
	while len(truncatable_primes) < 11:
		if not isprime(current_number): current_number += 2; continue
		if istruncatedprime(current_number): truncatable_primes.append(current_number)
		current_number += 2
	return sum(truncatable_primes)

print main()
