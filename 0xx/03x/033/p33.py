from numpy import prod
from math import gcd

def check(a, b):
  t = [i for i in range(1, 10) if (str(a) + str(b)).count(str(i)) > 1]
  for i in t:
    a1 = int(str(a).replace(str(i), "", 1))
    b1 = int(str(b).replace(str(i), "", 1))
    if a1 != 0 and b1 != 0:
      if a1 / b1 == a / b:
        return 1 # (a1, b1)
  return 0

arr = []
for b in range(11, 100):
  for a in range(10, b):
    if check(a, b):
      arr.append((a, b))

pa, pb = prod([i[0] for i in arr]), prod([i[1] for i in arr])
k = gcd(pa, pb)

print(arr)
print(pa, "/", pb)
print(pa // k, "/", pb // k, "- answer:", pb // k)