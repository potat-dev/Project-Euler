n = 1001
a = [n**2]
for i in range(n - 1, 0, -2):
  for k in range(4):
    a += [a[-1] - i]

print(sum(a))