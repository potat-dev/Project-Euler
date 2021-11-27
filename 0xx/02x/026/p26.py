def period(n):
  if n % 2 != 0 and n % 5 != 0:
    k = 1
    while 10**k % n != 1: k += 1
    return k
  else:
    return 1

m, n = 0, 0
for i in range(2, 1000):
  p = period(i)
  if p > m: n, m = i, p

print(n)