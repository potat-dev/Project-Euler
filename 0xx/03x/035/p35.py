from tqdm import trange, tqdm

def is_prime(n): 
  if n < 2: return 0
  if n == 2: return 1
  if not n & 1: return 0
  d = 3
  while d * d <= n:
    if n % d == 0: return 0
    d += 2
  return 1

primes = set([i for i in trange(1000000) if is_prime(i)])

def check_prime(n):
  s = str(n)
  for i in range(len(s)):
    s = s[1:] + s[0]
    if int(s) not in primes:
      return 0
  return 1

a = []
for i in tqdm(primes):
  if check_prime(i):
    a += [i]

print(sorted(a))
print(len(a))