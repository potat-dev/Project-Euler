# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13
# Очевидно, что 6-е простое число - 13
# Какое число является 10001-м простым числом?

def is_prime(n): 
  if n == 2: return 1
  if n < 2 or not n & 1: return 0
  d = 3
  while d * d <= n:
    if n % d == 0: return 0
    d += 2
  return 1

s, n = 0, 0
while n < 10001:
  s += 1
  while not is_prime(s): s += 1
  n += 1

print(s)