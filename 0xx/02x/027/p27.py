def is_prime(n): 
  if n < 2 or not n & 1: return 0
  d = 3
  while d * d <= n:
    if n % d == 0: return 0
    d += 2
  return 1

def test_formula(a, b):
  t = 0
  while is_prime(t**2 + a*t + b): t += 1
  return t

amax, bmax, tmax = 0, 0, 0
for a in range(-999, 1000):
  for b in range(-1000, 1001):
    t = test_formula(a, b)
    if t > tmax:
      amax, bmax, tmax = a, b, t

print(amax * bmax)