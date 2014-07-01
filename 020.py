a, b, c = 1, [], 0
for x in range(1,101):a *= x
for x in str(a):b.append(x)
for x in b:c = c + int(x)
print c
