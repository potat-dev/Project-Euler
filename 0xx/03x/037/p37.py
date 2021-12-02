que = lambda n: \
[int(n[i:]) for i in range(len(n))] + [int(n[:-i]) for i in range(1, len(n))]

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

c, k, s = 0, 10, 0
while c < 11:
  if all([is_prime(i) for i in que(str(k))]):
    print(k)
    c, s = c+1, s+k
  k += 1

print("Answer:", s)