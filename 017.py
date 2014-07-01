from num2words import num2words

total = 0
limit = 1000

for x in range(1, limit + 1):
  words = num2words(x)
  words = words.replace(" ", "")
  words = words.replace("-", "")
  words = words.replace(",", "")
  total += len(words)

print total
