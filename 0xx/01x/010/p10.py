# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17
# Найдите сумму всех простых чисел меньше двух миллионов

def is_prime(n):
  if n == 2: return 1
  if n < 2 or not n & 1: return 0
  d = 3
  while d * d <= n:
    if n % d == 0: return 0
    d += 2
  return 1

print(sum([i for i in range(2, 2*10**6) if is_prime(i)]))