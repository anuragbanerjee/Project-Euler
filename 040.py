a = ""; i = 1
while len(a) <= 1000000:a += str(i); i += 1
print reduce(lambda x, y: x * y, [int(a[q-1]) for q in [10 ** x for x in range(0, 7)]])
