from itertools import permutations

t = [int("".join([str(k) for k in i])) for n in range(1, 10) \
    for i in permutations(range(1, n + 1))]

def is_prime(n): 
  if n < 2: return 0
  if n > 2 and n & 1 == 0:
    return 0
  d = 3
  while d * d <= n:
    if n % d == 0:
      return 0
    d = d + 2
  return 1

print([i for i in t if is_prime(i)][-1])