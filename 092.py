# answer is 8581146
# timed ~ 38 seconds

from collections import defaultdict

cached_results = defaultdict(int)
cached_squares = {digit : digit ** 2 for digit in range(11)}
limit = 10 ** 7

def digit_squares_sum(n):
	digit_sum = 0
	while n:
		digit_sum += cached_squares[n % 10]
		n /= 10
	return digit_sum

def sad(current_number):
	current_chain = [current_number]
	while current_number != 1 and current_number != 89:
		if current_number in cached_results:
			current_number = cached_results[current_number]; break
		digit_sum = current_number = digit_squares_sum(current_number)
		current_chain.append(digit_sum)
	if current_number <= 1:
		for i in current_chain: cached_results[i] = 1
		else: return False
	else:
		for i in current_chain: cached_results[i] = 89
		else: return True

def main():
	total = 0
	for x in range(limit):
		if sad(x+1):
			total += 1
	return total

main()
