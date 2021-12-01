
from math import factorial
fsum = lambda n: sum([factorial(int(i)) for i in str(n)])

a = []
for n in range(10, 1000000):
  if fsum(n) == n:
    a += [n]
  n += 1

print(a)
print(sum(a))